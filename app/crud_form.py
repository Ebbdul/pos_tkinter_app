# app/crud_form.py
import tkinter as tk
from tkinter import messagebox


class CrudForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add your CRUD form widgets here
        pass

    def add_new(self):
        # Replace this with your logic for adding new records
        messagebox.showinfo("Add New", "Adding new record...")
        print("Addedddd")

