from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(data, output_filename):
    # Create a PDF document
    pdf_canvas = canvas.Canvas(output_filename, pagesize=letter)
    pdf_canvas.setTitle("Patient Data Report")

    # Set font and size for the title
    pdf_canvas.setFont("Helvetica-Bold", 16)
    pdf_canvas.drawCentredString(300, 750, "Patient Data Report")

    # Set font and size for the table header
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.setFillColorRGB(0.6, 0.6, 0.6)  # Set gray color for headers

    # Define column widths and heights
    col_widths = [80, 80, 80, 120]
    col_height = 20

    # Draw the table headers
    headers = ["Ref No.", "Time", "Date/s", "Patient Name"]
    x_position = 40
    for header, width in zip(headers, col_widths):
        pdf_canvas.drawString(x_position, 720, header)
        x_position += width

    # Set font and size for the table content
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.setFillColorRGB(0, 0, 0)  # Set black color


    # Draw the table content
    y_position = 700
    for row in data:
        x_position = 40
        for key in headers:
            value = row.get(key, "")
            pdf_canvas.drawString(x_position, y_position, str(value))
            x_position += col_widths[headers.index(key)]

        y_position -= col_height

    # Draw a line for the footer
    pdf_canvas.line(40, 50, 560, 50)

    # Set font and size for the date and time in the footer
    pdf_canvas.setFont("Helvetica", 10)
    pdf_canvas.setFillColorRGB(0, 0, 0)  # Set black color


    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Draw the date and time below the footer line
    pdf_canvas.drawString(40, 30, f"Report generated on: {current_datetime}")

    # Save the PDF document
    pdf_canvas.save()


