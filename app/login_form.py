# app/login_form.py
import tkinter as tk
from app.database import validate_credentials
from tkinter import messagebox
from app.tables import TablesPage


class LoginForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#ececec")
        self.master = master
        self.successful_login = False  # Flag to track successful login
        self.pack(expand=True, fill="both")
        self.create_widgets()


    def create_widgets(self):
        # Create a frame for the login form with a blue background and border
        login_frame = tk.Frame(self, bg="#3498db", bd=2, relief=tk.GROOVE)  # Set background color, border width, and relief
        login_frame.pack(padx=20, pady=20)

        # Big Label inside the login_frame
        big_label = tk.Label(login_frame, text="Welcome to Your App!", font=("Helvetica", 16), bg="#3498db", fg="white")
        big_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Image inside the login_frame
        img_path = "images/hos.png"  # Specify the correct path to your image
        img = tk.PhotoImage(file=img_path)
        img_label = tk.Label(login_frame, image=img, bg="#3498db")
        img_label.image = img  # Reference to prevent garbage collection
        img_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Username Label and Entry
        self.username_label = tk.Label(login_frame, text="Username:", font=("Helvetica", 12), bg="#3498db", fg="white")
        self.username_entry = tk.Entry(login_frame, font=("Helvetica", 12))

        # Password Label and Entry
        self.password_label = tk.Label(login_frame, text="Password:", font=("Helvetica", 12), bg="#3498db", fg="white")
        self.password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))  # Entry for password, characters shown as '*'

        # Grid layout for widgets inside login_frame
        self.username_label.grid(row=2, column=0, pady=5, padx=10, sticky=tk.E)
        self.username_entry.grid(row=2, column=1, pady=5, padx=10, sticky=tk.W)
        self.password_label.grid(row=3, column=0, pady=5, padx=10, sticky=tk.E)
        self.password_entry.grid(row=3, column=1, pady=5, padx=10, sticky=tk.W)

        # Center the login button below the fields
        self.login_button = tk.Button(login_frame, text="Login", command=self.handle_login, font=("Helvetica", 14), bg="#2ecc71", fg="white")
        self.login_button.grid(row=4, columnspan=2, pady=10)  # Centered below the fields

        # Calculate x and y positions for the frame to be centered
        x = (self.master.winfo_screenwidth() - login_frame.winfo_reqwidth()) // 2
        y = (self.master.winfo_screenheight() - login_frame.winfo_reqheight()) // 2

        # Place the frame at the center
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Database validation
        if validate_credentials(username, password):
            # Show a pop-up message for successful login
            messagebox.showinfo("Login Success", "Login successful!")
            print("Login Success", "Login successful!")

            # Set the flag for successful login
            self.successful_login = True

            # Remove the login frame
            self.destroy()

            # Open the tables page in the same window
            self.open_tables_window()

        else:
            # Show a pop-up message for invalid credentials
            messagebox.showerror("Login Failed", "Invalid username or password")
            print("Login Failed", "Invalid username or password")

    def open_tables_window(self):
        # Create a new instance of the TablesPage class within the same window
        tables_page = TablesPage(self.master)
        tables_page.pack(expand=True, fill="both")