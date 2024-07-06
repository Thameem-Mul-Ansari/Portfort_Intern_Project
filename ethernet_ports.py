from tkinter import messagebox
import subprocess

def disable_ethernet_port():
    try:
        result = subprocess.run(['netsh', 'interface', 'set', 'interface', 'Ethernet', 'disabled'], check=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", "Ethernet has been disabled successfully.")
        else:
            messagebox.showerror("Error", "Failed to disable Ethernet. Exit status 1.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to disable Ethernet: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def enable_ethernet_port():
    try:
        result = subprocess.run(['netsh', 'interface', 'set', 'interface', 'Ethernet', 'enabled'], check=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", "Ethernet has been enabled successfully.")
        else:
            messagebox.showerror("Error", "Failed to enable Ethernet. Exit status 1.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to enable Ethernet: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def check_ethernet_port():
    try:
        result = subprocess.run(['netsh', 'interface', 'show', 'interface', 'Ethernet'], capture_output=True, text=True)
        return "Enabled" in result.stdout
    except Exception:
        return False