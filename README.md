# PortFort_Intern_Project
**Unleash the Power to Control Your Ports!**

# Project Overview
  PortFort is a user-friendly desktop application designed to empower users with granular control over their computer's ports (USB, Wi-Fi, Ethernet, Webcam). It offers a graphical user interface (GUI) for enabling and disabling these ports, along with a robust authentication and verification system to ensure secure port management.

# Key Features
Intuitive GUI: PortFort presents a visually appealing and easy-to-navigate interface with clear icons representing each port type (USB, Wi-Fi, Ethernet, Webcam).
Granular Control: Users can effortlessly enable or disable individual ports based on their preferences and security requirements.
Secure Authentication: A secure login system safeguards unauthorized access to PortFort's functionalities.
Verification Mechanism: Upon login, a 4-digit code sent via email is required for verification, adding an extra layer of security.

# Installation
**Prerequisites**
tkinter
PIL (Pillow)
sqlite3
random
subprocess

**Additional libraries for specific port control functionalities (e.g., pywinusb for Windows USB control) may be required. Refer to their respective documentation for installation instructions.**

# Download
  Clone or download the PortFort repository from GitHub (link to your repository).

# Run the Application
Navigate to the downloaded directory in your terminal.
Execute the main Python script using the following command:
      **python main.py**

# Usage
Launch PortFort: Double-click the main.py file or execute the command mentioned above.
Login: Enter your registered email address and password on the login screen.
Verification: Check your email for a 4-digit code sent from PortFort. Enter the code in the verification prompt displayed within the application.
Port Management: Upon successful verification, you'll be presented with the main UI. Click the corresponding icons to enable or disable desired ports.

# Additional Notes
For enhanced security, consider implementing two-factor authentication (2FA) using libraries like pyotp.
Refer to the documentation of the additional port control libraries for specific usage instructions.
This application is intended for educational purposes. For production environments, consult with IT security professionals for guidance on implementing robust port control mechanisms.

# Disclaimer
Modifying port configurations can potentially impact applications or system functionality. Use PortFort with caution and at your own risk. Back up your system before making significant changes.
