import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    filename = Path(filepath).stem
    invoice_no, date = filename.split("-")

    pdf.add_page()
    pdf.set_font("times", style="B", size=25)
    pdf.cell(w=50, h=10, txt=f" Invoice No. {filename}", align="L", ln=1, border=0)

    pdf.set_font("times", style="B", size=25)
    pdf.cell(w=50, h=10, txt=f" Date- {date}", align="L", ln=1, border=0)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = [item.replace("_", " ").title() for item in df.columns]


    pdf.set_font("times", style="B", size=13)
    pdf.cell(w=30, h=10, txt=columns[0], align="L", border=1)
    pdf.cell(w=50, h=10, txt=columns[1], align="L", border=1)
    pdf.cell(w=40, h=10, txt=columns[2], align="L", border=1)
    pdf.cell(w=40, h=10, txt=columns[3], align="L", border=1)
    pdf.cell(w=30, h=10, txt=columns[4], align="L", ln=1, border=1)

    for index, row in df.iterrows():
        pdf.set_font("times", size=10)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), ln=1, border=1)

    pdf.output(f"PDFs/{invoice_no}.pdf")
