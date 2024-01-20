# app/crud_form.py
import tkinter as tk
from tkinter import messagebox





class CrudForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()


    def create_widgets(self):

        # Label and Entry for "Ref No."
        ref_label = tk.Label(self, text="Ref No.:")
        ref_label.grid(row=0, column=0, padx=5, pady=5)

        ref_entry = tk.Entry(self)
        ref_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for "Time"
        time_label = tk.Label(self, text="Time:")
        time_label.grid(row=1, column=0, padx=5, pady=5)

        time_entry = tk.Entry(self)
        time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label and Entry for "Date/s"
        date_label = tk.Label(self, text="Date/s:")
        date_label.grid(row=2, column=0, padx=5, pady=5)

        date_entry = tk.Entry(self)
        date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Label and Entry for "No. of visit"
        visit_label = tk.Label(self, text="No. of visit:")
        visit_label.grid(row=3, column=0, padx=5, pady=5)

        visit_entry = tk.Entry(self)
        visit_entry.grid(row=3, column=1, padx=5, pady=5)

        # Label and Entry for "Patient Name"
        name_label = tk.Label(self, text="Patient Name:")
        name_label.grid(row=4, column=0, padx=5, pady=5)

        name_entry = tk.Entry(self)
        name_entry.grid(row=4, column=1, padx=5, pady=5)

        # Label and Entry for "S/o D/o W/o"
        s_d_w_label = tk.Label(self, text="S/o D/o W/o:")
        s_d_w_label.grid(row=5, column=0, padx=5, pady=5)

        s_d_w_entry = tk.Entry(self)
        s_d_w_entry.grid(row=5, column=1, padx=5, pady=5)

        # Label and Entry for "Address"
        address_label = tk.Label(self, text="Address:")
        address_label.grid(row=6, column=0, padx=5, pady=5)

        address_entry = tk.Entry(self)
        address_entry.grid(row=6, column=1, padx=5, pady=5)

        # Label and Entry for "Cnic"
        cnic_label = tk.Label(self, text="Cnic:")
        cnic_label.grid(row=7, column=0, padx=5, pady=5)

        cnic_entry = tk.Entry(self)
        cnic_entry.grid(row=7, column=1, padx=5, pady=5)

        # Label and Entry for "Allergies"
        allergies_label = tk.Label(self, text="Allergies:")
        allergies_label.grid(row=8, column=0, padx=5, pady=5)

        allergies_entry = tk.Entry(self)
        allergies_entry.grid(row=8, column=1, padx=5, pady=5)

        # Label and Entry for "Presenting Complaints"
        complaints_label = tk.Label(self, text="Presenting Complaints:")
        complaints_label.grid(row=9, column=0, padx=5, pady=5)

        complaints_entry = tk.Entry(self)
        complaints_entry.grid(row=9, column=1, padx=5, pady=5)

        # Label and Entry for "History"
        history_label = tk.Label(self, text="History:")
        history_label.grid(row=10, column=0, padx=5, pady=5)

        history_entry = tk.Entry(self)
        history_entry.grid(row=10, column=1, padx=5, pady=5)

        # Label and Entry for "Findings"
        findings_label = tk.Label(self, text="Findings:")
        findings_label.grid(row=11, column=0, padx=5, pady=5)

        findings_entry = tk.Entry(self)
        findings_entry.grid(row=11, column=1, padx=5, pady=5)

        # Label and Entry for "Provision/ Diagnosis"
        diagnosis_label = tk.Label(self, text="Provision/ Diagnosis:")
        diagnosis_label.grid(row=12, column=0, padx=5, pady=5)

        diagnosis_entry = tk.Entry(self)
        diagnosis_entry.grid(row=12, column=1, padx=5, pady=5)

        # Label and Entry for "Remarks"
        remarks_label = tk.Label(self, text="Remarks:")
        remarks_label.grid(row=13, column=0, padx=5, pady=5)

        remarks_entry = tk.Entry(self)
        remarks_entry.grid(row=13, column=1, padx=5, pady=5)

        # Save button
        save_button = tk.Button(self, text="Save", command=self.save_record)
        save_button.grid(row=14, column=0, columnspan=2, pady=10)

    def save_record(self):
        # Replace this with your logic for saving the record
        print("Saving record...")
        # You can add database logic here

        # Close the form after saving
        self.destroy()

    def add_new(self):
        # Replace this with your logic for adding new records
        messagebox.showinfo("Add New", "Adding new record...")
        # You can add further logic to interact with the database or perform other actions
        print("Add New", "Adding new record...")

    def open_form_as_modal(self):
        # Set the form to be a dialog window, blocking interactions with the parent window
        self.grab_set()

        # Wait for the form to be closed
        self.wait_window(self)
