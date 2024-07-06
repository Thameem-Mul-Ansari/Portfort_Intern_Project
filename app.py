import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess

conn = sqlite3.connect('portfort.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, password TEXT, random_number INTEGER)''')
conn.commit()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.title("PORTFORT")
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    
        self.header_frame = tk.Frame(self, bg='gold')
        self.header_frame.grid(row=0, column=0, sticky='ew')

        self.content_frame = tk.Frame(self, bg='white')
        self.content_frame.grid(row=1, column=0, sticky='nsew')

        self.register_frame = tk.Frame(self.content_frame, bg='white')
        self.login_frame = tk.Frame(self.content_frame, bg='white')

        for frame in (self.register_frame, self.login_frame):
            frame.grid(row=0, column=0, sticky='nsew')

        self.initialize_widgets()

        self.show_frame(self.register_frame)

    def initialize_widgets(self):
        btn_close = tk.Button(self.header_frame, text="X", command=self.close_window, bg="gold", fg="black", font=("Helvetica", 12))
        btn_close.pack(side='right', padx=5)

        btn_maximize = tk.Button(self.header_frame, text="□", command=self.maximize_window, bg="gold", fg="black", font=("Helvetica", 12))
        btn_maximize.pack(side='right', padx=5)

        btn_minimize = tk.Button(self.header_frame, text="_", command=self.minimize_window, bg="gold", fg="black", font=("Helvetica", 12))
        btn_minimize.pack(side='right', padx=5)

        label_title = tk.Label(self.header_frame, text="PORTFORT", bg="gold", fg="black", font=("Helvetica", 18))
        label_title.pack(side='left', padx=10)

        left_canvas_register = tk.Canvas(self.register_frame, bg='black', width=self.winfo_screenwidth() // 2, height=self.winfo_screenheight())
        left_canvas_register.pack(side='left', fill='both', expand=True)

        right_canvas_register = tk.Canvas(self.register_frame, bg='white', width=self.winfo_screenwidth() // 2, height=self.winfo_screenheight())
        right_canvas_register.pack(side='right', fill='both', expand=True)

        label_create_account = tk.Label(right_canvas_register, text="Create new Account", font=("Helvetica", 24), fg="black", bg="white")
        label_create_account.place(x=60, y=100)

        label_already_registered = tk.Label(right_canvas_register, text="Already Registered? Login", font=("Helvetica", 12), fg="gold", bg="white", cursor="hand2")
        label_already_registered.bind("<Button-1>", lambda e: self.show_frame(self.login_frame))
        label_already_registered.place(x=60, y=150)

        label_name = tk.Label(right_canvas_register, text="Enter your name", font=("Helvetica", 14), fg="black", bg="white")
        label_name.place(x=60, y=200)
        self.entry_name = tk.Entry(right_canvas_register, font=("Helvetica", 14), bg="white", fg="blue", insertbackground="black")
        self.entry_name.place(x=60, y=230, width=400, height=30)

        label_email = tk.Label(right_canvas_register, text="Enter Email", font=("Helvetica", 14), fg="black", bg="white")
        label_email.place(x=60, y=270)
        self.entry_email = tk.Entry(right_canvas_register, font=("Helvetica", 14), bg="white", fg="blue", insertbackground="black")
        self.entry_email.place(x=60, y=300, width=400, height=30)

        label_password = tk.Label(right_canvas_register, text="Enter password", font=("Helvetica", 14), fg="black", bg="white")
        label_password.place(x=60, y=340)
        self.entry_password = tk.Entry(right_canvas_register, font=("Helvetica", 14), show='*', bg="white", fg="blue", insertbackground="black")
        self.entry_password.place(x=60, y=370, width=400, height=30)

        label_re_password = tk.Label(right_canvas_register, text="Re-enter password", font=("Helvetica", 14), fg="black", bg="white")
        label_re_password.place(x=60, y=410)
        self.entry_re_password = tk.Entry(right_canvas_register, font=("Helvetica", 14), show='*', bg="white", fg="blue", insertbackground="black")
        self.entry_re_password.place(x=60, y=440, width=400, height=30)

        btn_register = tk.Button(right_canvas_register, text="SIGN UP", font=("Helvetica", 18), fg="white", bg="blue", command=self.register)
        btn_register.place(x=70, y=540, width=380, height=40)
        self.bind('<Return>', lambda event=None: btn_register.invoke())

        image_file_path = "icons/lingo_logo.png"  

        image = Image.open(image_file_path)
        image = image.resize((300, 300), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)

        image_item = left_canvas_register.create_image(self.winfo_screenwidth() // 4, self.winfo_screenheight() // 2, image=image_tk)
        left_canvas_register.image = image_tk  

        left_canvas_login = tk.Canvas(self.login_frame, bg='black', width=self.winfo_screenwidth() // 2, height=self.winfo_screenheight())
        left_canvas_login.pack(side='left', fill='both', expand=True)

        right_canvas_login = tk.Canvas(self.login_frame, bg='white', width=self.winfo_screenwidth() // 2, height=self.winfo_screenheight())
        right_canvas_login.pack(side='right', fill='both', expand=True)

        label_login_title = tk.Label(right_canvas_login, text="Login", font=("Helvetica", 24), fg="black", bg="white")
        label_login_title.place(x=60, y=100)

        label_back_to_register = tk.Label(right_canvas_login, text="Back to Register", font=("Helvetica", 12), fg="gold", bg="white", cursor="hand2")
        label_back_to_register.bind("<Button-1>", lambda e: self.show_frame(self.register_frame))
        label_back_to_register.place(x=60, y=150)

        label_login_email = tk.Label(right_canvas_login, text="Enter Email", font=("Helvetica", 14), fg="black", bg="white")
        label_login_email.place(x=60, y=200)
        self.entry_login_email = tk.Entry(right_canvas_login, font=("Helvetica", 14), bg="white", fg="blue", insertbackground="black")
        self.entry_login_email.place(x=60, y=230, width=400, height=30)

        label_login_password = tk.Label(right_canvas_login, text="Enter password", font=("Helvetica", 14), fg="black", bg="white")
        label_login_password.place(x=60, y=270)
        self.entry_login_password = tk.Entry(right_canvas_login, font=("Helvetica", 14), show='*', bg="white", fg="blue", insertbackground="black")
        self.entry_login_password.place(x=60, y=300, width=400, height=30)

        btn_login = tk.Button(right_canvas_login, text="LOGIN", font=("Helvetica", 18), fg="white", bg="blue", command=self.login)
        btn_login.place(x=70, y=380, width=380, height=40)
        self.bind('<Return>', lambda event=None: btn_login.invoke())

        image_file_path = "icons/lingo_logo.png"  

        image = Image.open(image_file_path)
        image = image.resize((300, 300), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)

        image_item = left_canvas_login.create_image(self.winfo_screenwidth() // 4, self.winfo_screenheight() // 2, image=image_tk)
        left_canvas_login.image = image_tk 

    def register(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        re_password = self.entry_re_password.get()

        if not name or not email or not password or not re_password:
            messagebox.showerror("Error", "All fields are required")
            return

        if password != re_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        cursor.execute('SELECT * FROM users WHERE email=?', (email,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Email already registered")
            return

        random_number = random.randint(1000, 9999)
        user_data = (name, email, password, random_number)

        cursor.execute('INSERT INTO users (name, email, password, random_number) VALUES (?, ?, ?, ?)', user_data)
        conn.commit()

        self.send_welcome_email(email, random_number)

        messagebox.showinfo("Success", "Registration successful!")
        self.clear_fields()
        self.show_frame(self.login_frame)

    def send_welcome_email(self, email, random_number):
        smtp_server = 'smtp.gmail.com'  
        smtp_port = 587  
        smtp_user = 'your_mail@gmail.com' 
        smtp_password = 'your_app_password' 

        subject = 'Welcome to PORTFORT'
        body = (f'Dear User,\n\n'
                f'Thank you for registering with PORTFORT. We are excited to have you on board!\n\n'
                f'Your verification code is {random_number}. Please use this code to complete your registration.\n\n'
                f'Best regards,\n'
                f'The PORTFORT Team')

        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, email, msg.as_string())
            server.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send welcome email: {str(e)}")

    def login(self):
        email = self.entry_login_email.get()
        password = self.entry_login_password.get()

        cursor.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
        if cursor.fetchone():
            messagebox.showinfo("Success", "Login successful!")
            self.destroy()
            subprocess.run(['python', 'portfort.py']) 
        else:
            messagebox.showerror("Error", "Invalid email or password")

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_re_password.delete(0, tk.END)
        self.entry_login_email.delete(0, tk.END)
        self.entry_login_password.delete(0, tk.END)

    def show_frame(self, frame):
        frame.tkraise()

    def close_window(self):
        self.destroy()

    def maximize_window(self):
        if self.state() == 'normal':
            self.state('zoomed')
        else:
            self.state('normal')

    def minimize_window(self):
        self.iconify()

if __name__ == "__main__":
    app = App()
    app.mainloop()