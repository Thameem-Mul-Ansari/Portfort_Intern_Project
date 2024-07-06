import sys
import ctypes
import subprocess

from is_admin import is_admin

def run_as_admin():
    if is_admin():
        return True
    else:
        try:
            params = ' '.join([f'"{param}"' for param in sys.argv])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
            sys.exit(0)
        except Exception as e:
            print(f"Failed to elevate to administrative privileges: {e}")
            return False