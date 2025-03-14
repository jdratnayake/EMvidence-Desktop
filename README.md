# EMvidence Data Acquiring Application

This software application is designed for forensic purposes, enabling the acquisition of Electromagnetic (EM) data from the [HackRF One](https://greatscottgadgets.com/hackrf/one/) device. Tailored for forensic investigations, it provides a reliable platform for collecting EM signals for analysis and evidence gathering.

## Features

- Captures EM data using the HackRF One device.
- Optimized for forensic use cases.
- Supports both Windows and Linux operating systems.

## Prerequisites

Before installing the application, ensure the following requirements are met based on your operating system:

### Windows

- [Miniconda](https://docs.anaconda.com/free/miniconda/) installed.
- Conda added to your system PATH environment variables.

### Linux

- [Python 3](https://www.python.org/downloads/) installed.
- [GNURadio](https://www.gnuradio.org/) library packages installed.

## Installation

Follow these steps to install the application:

### Windows

1. Clone the repository.
2. Run the `run.bat` file.

### Linux

1. Clone the repository.
2. Run the Installer

```bash
chmod +x install.sh
./install.sh
```

3. Execute the application

   - Execute the script:

   ```bash
   chmod +x run.sh
   ./run.sh
   ```

   - Or run directly: `python3 main.py`
