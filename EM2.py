#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: EM
# GNU Radio version: 3.9.8.0

# from distutils.version import StrictVersion
from packaging import version as packaging_version

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
import argparse
import os



from gnuradio import qtgui

class EM(gr.top_block, Qt.QWidget):

    def __init__(self,samp_rate, cent_freq,file):
        # self.samp_rate = samp_rate
        # self.cent_freq = cent_freq
        print("Inside EM")
        gr.top_block.__init__(self, "EM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("EM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "EM")

        try:
            if packaging_version.parse(Qt.qVersion()) < packaging_version.parse("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        # self.samp_rate = samp_rate = 20e6
        self.samp_rate = samp_rate
        self.cent_freq = cent_freq
        self.file = file

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        # print("Sample rate: "+str(self.samp_rate))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_center_freq(self.cent_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, self.file, False)
        self.blocks_file_sink_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "EM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
       self.samp_rate = samp_rate
       self.osmosdr_source_0.set_sample_rate(self.samp_rate)
       self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate) 

    # def get_cent_freq(self):
    #     return self.cent_freq

    # def set_cent_freq(self, cent_freq):
    #    self.cent_freq = cent_freq

    # def get_file(self):
    #     return self.file

    # def set_file(self, file):
    #    self.file = file
    #    self.blocks_file_sink_0.open(file)   

    # def close_file(self):
    #     self.blocks_file_sink_0.close()     


            

# Time period variable
# time_period = 10000
# def check_hackrf():
#     available_devices = osmosdr.source().get_gain_names()
#     print(available_devices)

def check_hackrf_connection():
    # Try to create an osmosdr source block for the HackRF
    source = osmosdr.source().get_gain_names()
    if 'RF' in source:
        return True
    else:
        print("NO HACKRF ONE::")
        return False

def main(top_block_cls=EM, samp_rate='20e6',cent_freq='288e6',time='10',file='env_signals.cfile'):

    

    print("Inside File 2")
    print("Sampling rate: "+samp_rate)
    print("Center Frequency: "+cent_freq)
    print("Time duration of capture: "+time)
    print("Output file name: "+file)

    qapp = Qt.QApplication(sys.argv)

    if not check_hackrf_connection():
        return "No Hack RF"
    tb = top_block_cls(samp_rate=float(samp_rate),cent_freq=float(cent_freq),file=file)
    

    tb.start()

    tb.show()

    
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()   

    Qt.QApplication.quit()

    # Additional cleanup if needed
    # sys.exit(0)

    print("Before signal")
    # signal.signal(signal.SIGINT, sig_handler)
    # signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.timeout.connect(lambda: sig_handler())
    timer.start(int(time) * 1000)

    
    
    # stop_thread = threading.Thread(target=stop_after_duration,args=(tb,))
    # stop_thread.start()

    qapp.exec_()
    

if __name__ == '__main__':
    main()
