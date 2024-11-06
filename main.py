import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    invoice_df = pd.read_excel(filepath, sheet_name='Sheet 1')
    invoice_name = Path(filepath).stem
    invoice_nr = f'Invoice nr. {invoice_name.split("-")[0]}'
    invoice_date = f'Date {invoice_name.split("-")[1]}'
    invoice_pdf = FPDF(orientation='P', unit='mm', format='A4')
    invoice_pdf.set_auto_page_break(auto=False, margin=0)

    invoice_pdf.add_page()
    invoice_pdf.set_font(family="Times", style="B", size=24)
    invoice_pdf.cell(w=0, h=12, txt=invoice_nr, align='L', ln=1)
    invoice_pdf.cell(w=0, h=12, txt=invoice_date, align='L', ln=1)
    invoice_pdf.output(f'PDFs/{invoice_name}.pdf')