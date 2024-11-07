import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    invoice_name = Path(filepath).stem
    invoice_nr = f'Invoice nr. {invoice_name.split("-")[0]}'
    invoice_date = f'Date {invoice_name.split("-")[1]}'
    invoice_pdf = FPDF(orientation='P', unit='mm', format='A4')
    invoice_pdf.set_auto_page_break(auto=False, margin=0)

    # Add invoice information
    invoice_pdf.add_page()
    invoice_pdf.set_font(family="Times", style="B", size=24)
    invoice_pdf.cell(w=0, h=12, txt=invoice_nr, align='L', ln=1)
    invoice_pdf.cell(w=0, h=12, txt=invoice_date, align='L', ln=1)
    invoice_pdf.cell(w=0, h=12, align='L', ln=1)

    # Add table header
    invoice_df = pd.read_excel(filepath, sheet_name='Sheet 1')
    invoice_columns = list(invoice_df.columns)
    invoice_pdf.set_font(family="Times", size=12, style='B')
    invoice_pdf.cell(w=35, h=8, txt=invoice_columns[0], border=1)
    invoice_pdf.cell(w=60, h=8, txt=invoice_columns[1], border=1)
    invoice_pdf.cell(w=39, h=8, txt=invoice_columns[2], border=1)
    invoice_pdf.cell(w=30, h=8, txt=invoice_columns[3], border=1)
    invoice_pdf.cell(w=30, h=8, txt=invoice_columns[4], border=1, ln=1)

    # Add table values
    for index, row in invoice_df.iterrows():
        invoice_pdf.set_font(family="Times", size=12)
        invoice_pdf.cell(w=35, h=8, txt=str(row["product_id"]), border=1)
        invoice_pdf.cell(w=60, h=8, txt=row["product_name"], border=1)
        invoice_pdf.cell(w=39, h=8, txt=str(row["amount_purchased"]), border=1)
        invoice_pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        invoice_pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)


    invoice_pdf.output(f'PDFs/{invoice_name}.pdf')
