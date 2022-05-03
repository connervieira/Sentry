# Documentation

This document explains how to download, install, configure, and use Sentry.


## Installation

1. Download Sentry.
    - Stable versions of Sentry can be downloaded from the V0LT website.
    - Unstable versions of Sentry can be downloaded straight from the git repository.
2. Install dependencies.
    - Sentry's critical dependencies are installed by default on the vast majority of Linux distributions, but it's worth confirming they're working properly.
        - Python3
        - NetworkManager (nmcli)
    - To use the 'airodump' backend, install `aircrack-ng`. AirCrack should come packaged with `airomon-ng` and `airodump-ng`


## Configuration

In order to get the most out of Sentry, you should configure it to meet your needs.

1. Open `config.json` in the Sentry directory.
    - This file is simply a plain text JSON file, so any plain text editor should work.
2. Modify configuration values as appropriate.
    - All configuration values are described in the CONFIGURATION.md document.


### Running

After setting up Sentry, you can run it for the first time.

1. Open the Sentry folder in a shell.
    - Example: `cd ~/Software/Sentry/`
2. Run Sentry with Python3
    - Example: `python3 main.py`


### Hardware

After you get Sentry up and running, it may be worth considering your hardware setup, and ways to improve it's performance.

1. Processor
    - Sentry is extremely lightweight, so a high performance processing device isn't inherently necessary.
    - A single-board computer, like a Raspberry Pi 4, should work great, despite it's low cost.
2. Wireless Adapter
    - Nearly all commercially available drones operate on 2.4 GHz, 5 GHz, or 5.8 GHz. A wireless adapter that can receieve these frequencies is ideal.
3. Antenna
    - When installed in a building or vehicle, installing an external antenna is recommended to prevent obstructions from limiting range.
