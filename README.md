# IP Address Analysis Tool

This tool allows you to analyze IP addresses using various online tools. It automates the process of opening a web browser, navigating to specific websites, and pasting the IP addresses for analysis.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/ip-address-analysis-tool.git

    Install the required Python packages:

    bash

    pip install -r requirements.txt

Usage

    Make sure you have a file named addresses.txt containing the IP addresses you want to analyze, with each IP address on a new line.

    Run the script:

    bash

    python main.py

    Follow the on-screen instructions to choose the tool you want to use for IP address analysis (Symantec, AbuseIP, or VirusTotal).

    The script will open a web browser and automatically navigate to the selected tool's website. It will then paste each IP address from the addresses.txt file for analysis.

    Sit back and let the tool do the work! It will automatically analyze each IP address and display the results.

Tools Used

    webbrowser: Library for automating web browser actions.
    pyperclip: Library for copying and pasting in Python.
    pyautogui: Library for automating keyboard and mouse actions.
    time: Library for handling time-related operations.
    colorama: Library for adding colors to the terminal output.

Disclaimer

This tool is intended for educational purposes only. Use it responsibly and respect the terms of service of the websites you are accessing.