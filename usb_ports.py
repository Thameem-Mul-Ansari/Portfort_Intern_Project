import winreg as reg
from tkinter import messagebox

def disable_usb_ports():
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "Start", 0, reg.REG_DWORD, 4)
        reg.CloseKey(key)
        messagebox.showinfo("Success", "USB ports have been disabled successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disable USB ports: {e}")

def enable_usb_ports():
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "Start", 0, reg.REG_DWORD, 3)
        reg.CloseKey(key)
        messagebox.showinfo("Success", "USB ports have been enabled successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to enable USB ports: {e}")

def check_usb_ports():
    try:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, reg.KEY_QUERY_VALUE)
        start, _ = reg.QueryValueEx(key, "Start")
        reg.CloseKey(key)
        return start == 3
    except Exception:
        return False