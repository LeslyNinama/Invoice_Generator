import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name= "Sheet 1")

    pdf = FPDF(orientation = "P", unit = "mm", format= "A4")
    filename = Path(filepath).stem
    invoice_no, date = filename.split("-")

    pdf.add_page()
    pdf.set_font("times", style= "B", size= 25 )
    pdf.cell(w = 50, h= 10, txt=f" Invoice No. {filename}", align = "L", ln=1, border = 0 )

    pdf.set_font("times", style= "B", size= 25 )
    pdf.cell(w = 50, h= 10, txt=f" Date- {date}", align = "L", ln=1, border = 0)

    pdf.output(f"PDFs/{invoice_no}.pdf")


