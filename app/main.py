# app/main.py
import tkinter as tk
from app.login_form import LoginForm  # Corrected import path

def main():
    root = tk.Tk()
    root.title("POS")
    root.state('zoomed')

    login_form = LoginForm(root)
    login_form.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
