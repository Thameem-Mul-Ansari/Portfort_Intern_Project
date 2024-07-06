import sys
from run_as_admin import run_as_admin
from app import App
from is_admin import is_admin

def main():
    if not is_admin():
        run_as_admin()
        return

    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
