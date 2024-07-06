from tkinter import messagebox
import subprocess

def disable_wifi():
    try:
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'disabled'])
        messagebox.showinfo("Success", "WiFi has been disabled successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disable WiFi: {e}")

def enable_wifi():
    try:
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'enabled'])
        messagebox.showinfo("Success", "WiFi has been enabled successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to enable WiFi: {e}")

def check_wifi():
    try:
        result = subprocess.run(['netsh', 'interface', 'show', 'interface', 'Wi-Fi'], capture_output=True, text=True)
        return "Enabled" in result.stdout
    except Exception:
        return False