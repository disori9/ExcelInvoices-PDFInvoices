import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    invoice_df = pd.read_excel(filepath, sheet_name='Sheet 1')
    invoice_nr = filepath[9:14]
    invoice_date = filepath[15:24]