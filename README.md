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

# Output
![IMG-20240706-WA0011](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/b8312f3e-1fc1-4b5c-b85f-f3bb7f1e494b)
![IMG-20240706-WA0008](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/0073e995-fd6f-44a5-96e1-c6ea05753db4)
![IMG-20240706-WA0010](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/43b0fde8-a369-4d8f-bd5d-5b0a2fa45046)
![IMG-20240706-WA0012](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/fc9f4414-7bab-497a-bbb9-f0c909846bf6)
![IMG-20240706-WA0013](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/c8a75263-e6ba-4ec3-823a-66a350ca92f1)
![IMG-20240706-WA0009](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/f2349adb-d838-49bf-81bc-efb583232e85)
![IMG-20240706-WA0007](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/ce23672d-99e0-498e-b21b-18c7f6e24dad)
![IMG-20240706-WA0006](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/5375bf0b-f0b0-4333-935f-ebb9bd1ffc36)
![IMG-20240706-WA0014](https://github.com/Thameem-Mul-Ansari/Portfort_Intern_Project/assets/131378878/218c1ce9-4c6c-426a-87a5-ef2d3eaa1e64)

# Additional Notes
For enhanced security, consider implementing two-factor authentication (2FA) using libraries like pyotp.
Refer to the documentation of the additional port control libraries for specific usage instructions.
This application is intended for educational purposes. For production environments, consult with IT security professionals for guidance on implementing robust port control mechanisms.

# Disclaimer
Modifying port configurations can potentially impact applications or system functionality. Use PortFort with caution and at your own risk. Back up your system before making significant changes.
