import winreg
from tkinter import messagebox

def disable_cam():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\usbvideo', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
        winreg.CloseKey(key)
        messagebox.showinfo("Webcam service disabled successfully.")
    except Exception as e:
        messagebox.showinfo(f"Failed to disable webcam service: {e}")

def enable_cam():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\usbvideo', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 3)
        winreg.CloseKey(key)
        messagebox.showinfo("Webcam service enabled successfully.")
    except Exception as e:
        messagebox.showinfo(f"Failed to enable webcam service: {e}")

def check_cam():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\usbvideo', 0, winreg.KEY_QUERY_VALUE)
        start, _ = winreg.QueryValueEx(key, 'Start')
        winreg.CloseKey(key)
        return start == 3
    except Exception:
        return False