import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import subprocess
import sqlite3
import random

from usb_ports import disable_usb_ports, enable_usb_ports, check_usb_ports
from ethernet_ports import disable_ethernet_port, enable_ethernet_port, check_ethernet_port
from webcam import disable_cam, enable_cam, check_cam
from wifi import disable_wifi, enable_wifi, check_wifi

class PortFort:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PortFort")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="white")
        
        self.conn = sqlite3.connect('portfort.db')
        self.cursor = self.conn.cursor()

        self.button_frame = tk.Frame(self.root, bg="white")
        self.button_frame.place(relx=0.95, rely=0.2, anchor=tk.NE)

        self.icon_size = 100  
        self.icon_paths = ["icons/wifi_icon.png", "icons/camera_icon.png", "icons/usb_icon.png", "icons/ethernet_icon.png"]
        self.icons = []

        for path in self.icon_paths:
            image = Image.open(path)
            image = image.resize((self.icon_size, self.icon_size), Image.LANCZOS)
            self.icons.append(ImageTk.PhotoImage(image))

        self.disable_funcs = [disable_wifi, disable_cam, disable_usb_ports, disable_ethernet_port]
        self.enable_funcs = [enable_wifi, enable_cam, enable_usb_ports, enable_ethernet_port]
        self.check_funcs = [check_wifi, check_cam, check_usb_ports, check_ethernet_port]

        for i in range(2):
            for j in range(2):
                canvas = tk.Canvas(self.button_frame, width=250, height=250, highlightthickness=0, bg="white")
                canvas.grid(row=i, column=j, padx=20, pady=20)
                
                icon_index = i * 2 + j
                is_enabled = self.check_funcs[icon_index]()
                initial_color = "green" if is_enabled else "red"
                
                button_id = self.create_rounded_rect(canvas, 5, 5, 250-5, 250-5, 40, fill=initial_color)
                
                canvas.create_image(250//2, 250//2, image=self.icons[icon_index])
                
                canvas.tag_bind(button_id, "<Button-1>", lambda event, c=canvas, b=button_id, d=self.disable_funcs[icon_index], e=self.enable_funcs[icon_index]: self.button_click(event, c, b, d, e))

        self.create_title_and_header()

        self.root.mainloop()

        self.conn.close()

    def verify_code(self, button_id, disable_func, enable_func, canvas):
        def check_code():
            entered_code = code_entry.get()
            try:
                entered_code_int = int(entered_code)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid 4-digit number.")
                return
            
            self.cursor.execute('SELECT * FROM users WHERE random_number=?', (entered_code_int,))
            if self.cursor.fetchone():
                current_color = canvas.itemcget(button_id, "fill")
                if current_color == "green":
                    disable_func()
                    new_color = "red"
                else:
                    enable_func()
                    new_color = "green"
                canvas.itemconfig(button_id, fill=new_color)
                popup.destroy()
            else:
                messagebox.showerror("Error", "Incorrect code. Please try again.")
        
        popup = tk.Toplevel(self.root)
        popup.title("Enter Code")
        popup.geometry("300x150")
        popup.configure(bg="white")
        
        tk.Label(popup, text="Enter the 4-digit code:", bg="white").pack(pady=10)
        code_entry = tk.Entry(popup, font=("Arial", 24), width=4, justify='center', show='*')
        code_entry.pack(pady=10)
        tk.Button(popup, text="Submit", command=check_code, bg="gold", fg="black", font=("Arial", 12)).pack(pady=10)

    def button_click(self, event, canvas, button_id, disable_func, enable_func):
        self.verify_code(button_id, disable_func, enable_func, canvas)

    def create_rounded_rect(self, canvas, x1, y1, x2, y2, r, **kwargs):
        points = [x1+r, y1,x2-r, y1,x2, y1,x2, y1+r,x2, y2-r,x2, y2,x2-r, y2,x1+r, y2,x1, y2,x1, y2-r,x1, y1+r,x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def create_title_and_header(self):
        title_frame = tk.Frame(self.root, bg="white")
        title_frame.place(relx=0.1, rely=0.45, anchor=tk.NW) 

        title_font = font.Font(family="Arial", size=48, weight="bold")
        tagline_font = font.Font(family="Arial", size=24, slant="italic")

        title_label = tk.Label(title_frame, text="PORTFORT", font=title_font, bg="white", fg="#F5B041")
        title_label.pack(pady=10)

        tagline_label = tk.Label(title_frame, text="Unleash the Power to Control Your Ports!", font=tagline_font, bg="white", fg="black")
        tagline_label.pack(pady=5)

        def create_gradient(canvas, width, height, color1, color2, steps):
            r1, g1, b1 = self.root.winfo_rgb(color1)
            r2, g2, b2 = self.root.winfo_rgb(color2)
            
            r_ratio = (r2 - r1) / steps
            g_ratio = (g2 - g1) / steps
            b_ratio = (b2 - b1) / steps
            
            for i in range(steps):
                nr = int(r1 + (r_ratio * i))
                ng = int(g1 + (g_ratio * i))
                nb = int(b1 + (b_ratio * i))
                
                color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
                canvas.create_rectangle(0, i * (height / steps), width, (i + 1) * (height / steps), outline="", fill=color)

        header_frame = tk.Frame(self.root, bg="white", height=100)
        header_frame.pack(fill=tk.X, pady=10)

        header_canvas = tk.Canvas(header_frame, bg="white", height=100, highlightthickness=0)
        header_canvas.pack(fill=tk.X)

        screen_width = self.root.winfo_screenwidth()

        create_gradient(header_canvas, screen_width, 100, "blue", "purple", 100)

        logo_size = 80  
        logo_left_image = Image.open("icons/supraja_logo.png") 
        logo_left_image = logo_left_image.resize((logo_size, logo_size), Image.LANCZOS)
        self.logo_left = ImageTk.PhotoImage(logo_left_image)  

        logo_left_label = tk.Label(header_canvas, image=self.logo_left) 
        logo_left_label.place(relx=0.05, rely=0.5, anchor=tk.W)

        header_text_font = font.Font(family="Arial", size=24, weight="bold")
        header_canvas.create_text(screen_width/2, 50, text="Intern Project", font=header_text_font, fill="white", anchor=tk.CENTER)

        def close_window():
            self.root.destroy()

        def maximize_window():
            if self.root.state() == 'normal':
                self.root.state('zoomed')
            else:
                self.root.state('normal')

        def minimize_window():
            self.root.iconify()

        btn_close = tk.Button(header_frame, text="X", command=close_window, bg="gold", fg="black", font=("Helvetica", 12))
        btn_close.place(relx=0.98, rely=0.02, anchor=tk.NE)

        btn_maximize = tk.Button(header_frame, text="□", command=maximize_window, bg="gold", fg="black", font=("Helvetica", 12))
        btn_maximize.place(relx=0.96, rely=0.02, anchor=tk.NE)

        btn_minimize = tk.Button(header_frame, text="_", command=minimize_window, bg="gold", fg="black", font=("Helvetica", 12))
        btn_minimize.place(relx=0.94, rely=0.02, anchor=tk.NE)

        def logout():
            self.root.destroy()
            subprocess.run(['python', 'app.py']) 

        btn_logout = tk.Button(header_frame, text="Logout", command=logout, bg="gold", fg="black", font=("Helvetica", 12))
        btn_logout.place(relx=0.92, rely=0.02, anchor=tk.NE)

if __name__ == "__main__":
    PortFort()
