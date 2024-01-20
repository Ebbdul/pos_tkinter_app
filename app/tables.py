# app/tables3.text
import tkinter as tk
from tkinter import ttk, messagebox
from app.database import fetch_data
from tkinter.ttk import Treeview
from app.crud_form import CrudForm
from app.report import generate_pdf_report


class TablesPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill="both")
        self.table = None  # Initialize self.table
        self.crud_form = CrudForm(master=self)  # Create an instance of the CRUDForm
        self.create_widgets()
        self.refresh_interval = 5000  # Set the refresh interval in milliseconds

    def create_widgets(self, data=None):
        # Add a big label at the top
        big_label = tk.Label(self, text="Patient Data", font=("Helvetica", 20))
        big_label.pack(pady=10)

        # Add a Refresh button
        refresh_button = tk.Button(self, text="Refresh", command=self.manual_refresh, bg="blue", fg="white")
        refresh_button.pack(side=tk.TOP, padx=5, pady=5)

        # Add an Add New button
        add_new_button = tk.Button(self, text="Add New", command=self.crud_form.add_new, bg="green",
                                   fg="white")
        add_new_button.pack(side=tk.TOP, padx=5, pady=5)
        # Add a View Report button
        view_report_button = tk.Button(self, text="View Report", command=self.view_report, bg="orange", fg="white")
        view_report_button.pack(side=tk.TOP, padx=5, pady=5)

        # Create a Treeview widget for the table
        table = Treeview(self, columns=(
            "Ref No.", "Time", "Date/s", "No. of visit", "Patient Name", "S/o D/o W/o", "Address", "Cnic", "Allergies",
            "Presenting Complaints", "History", "Findings", "Provision/ Diagnosis", "Remarks", "Action"),
                         show="headings",height=15)

        # Set column headings
        for column in table["columns"]:
            table.heading(column, text=column, anchor=tk.CENTER)
            if column == "Action":
                table.column(column, anchor=tk.CENTER, width=150)  # Adjust width for the Action column
            else:
                table.column(column, anchor=tk.CENTER, width=120,
                             stretch=True)  # Adjust width as needed, set stretch=True

            # Enable sorting on the column headers
            table.heading(column, command=lambda col=column: self.sort_table(table, col, False))

        if data is None:
            data = fetch_data()

        # Populate the table with data
        for row in data:
            values = [row['ref_no'], row['appointment_time'], row['appointment_date'], row['no_of_visit'],
                      row['patient_name'], row['so_do_wo'], row['address'], row['cnic'], row['allergies'],
                      row['presenting_complaints'], row['history'], row['findings'], row['provision_Diagnosis'],
                      row['Remarks']]
            table.insert("", tk.END, values=values)

        # Pack the table into the frame and assign it to self.table
        table.pack(expand=True, fill="both")
        self.table = table

        # Configure styles
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))  # Increase font size and make header bold

        # Create vertical scrollbar
        v_scrollbar = ttk.Scrollbar(self, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=v_scrollbar.set)
        v_scrollbar.pack(side="right", fill="y")

        # Create horizontal scrollbar
        h_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=table.xview)
        table.configure(xscrollcommand=h_scrollbar.set)
        h_scrollbar.pack(side="bottom", fill="x")

        # Pack the table into the frame
        table.pack(expand=True, fill="both")

        # Add pagination controls
        pagination_frame = tk.Frame(self)
        pagination_frame.pack(pady=10)

        prev_button = tk.Button(pagination_frame, text="Previous", command=lambda: self.show_page(table, -1))
        prev_button.grid(row=0, column=0, padx=5)

        next_button = tk.Button(pagination_frame, text="Next", command=lambda: self.show_page(table, 1))
        next_button.grid(row=0, column=1, padx=5)

        # Add icons for edit, delete, and view in the "Action" column
        for i in range(10):
            edit_icon = tk.PhotoImage(file="images/edit.png")  # Replace with your edit icon
            delete_icon = tk.PhotoImage(file="images/delete.png")  # Replace with your delete icon
            view_icon = tk.PhotoImage(file="images/view.png")  # Replace with your view icon

            edit_button = ttk.Button(table, image=edit_icon, command=lambda i=i: self.perform_action("Edit", i))
            delete_button = ttk.Button(table, image=delete_icon, command=lambda i=i: self.perform_action("Delete", i))
            view_button = ttk.Button(table, image=view_icon, command=lambda i=i: self.perform_action("View", i))

            table.window_create(table.index(f"#0:{i}"), window=edit_button)
            table.window_create(table.index(f"#0:{i+1}"), window=delete_button)
            table.window_create(table.index(f"#0:{i+2}"), window=view_button)

            # Save references to the images to prevent garbage collection
            edit_button.image = edit_icon
            delete_button.image = delete_icon
            view_button.image = view_icon

    def show_page(self, table, direction):
        current_page = int(table.index(table.focus())) + direction
        table.selection_set(table.get_children()[current_page])
        table.yview_moveto(current_page / len(table.get_children()))

    def perform_action(self, action, row_index):
        # Replace this with your logic for handling the actions (Edit, Delete, View)
        print(f"Performing {action} on row {row_index + 1}")

    def sort_table(self, treeview, col, reverse):
        # Sorting function for the column headers
        data = [(treeview.set(child, col), child) for child in treeview.get_children('')]
        data.sort(reverse=reverse)

        for index, item in enumerate(data):
            treeview.move(item[1], '', index)

        # Reverse the sort order for the next click
        treeview.heading(col, command=lambda: self.sort_table(treeview, col, not reverse))




    # Add a method for manual refresh
    def manual_refresh(self):
        # Call the fetch_data function to get the latest data
        data = fetch_data()
        print("Manual Refresh - New Data:", data)

        # Clear the existing content in the table
        if self.table:
            for child in self.table.get_children():
                self.table.delete(child)

            # Populate the table with the latest data
            for row in data:
                values = [row['ref_no'], row['appointment_time'], row['appointment_date'], row['no_of_visit'],
                          row['patient_name'], row['so_do_wo'], row['address'], row['cnic'], row['allergies'],
                          row['presenting_complaints'], row['history'], row['findings'], row['provision_Diagnosis'],
                          row['Remarks']]
                self.table.insert("", tk.END, values=values)

    def view_report(self):
        # Fetch data from the table
        sample_data = [
            {'Ref No.': 1, 'Time': '10:00 AM', 'Date/s': '2023-01-01', 'Patient Name': 'John Doe'},
            {'Ref No.': 2, 'Time': '02:30 PM', 'Date/s': '2023-01-02', 'Patient Name': 'Jane Doe'},
        ]
        data = []
        for item in self.table.get_children():
            values = self.table.item(item, 'values')  # No need for list here
            data.append(dict(zip(self.table['columns'], values)))

        # Generate the PDF report
        output_filename = "patient_data_report.pdf"
        generate_pdf_report(data, output_filename)

        # Show a message box indicating that the report has been generated
        messagebox.showinfo("Report Generated", f"The report has been generated and saved as {output_filename}")

