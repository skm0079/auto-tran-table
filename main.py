import os
import pandas as pd
from docx import Document
from docx.shared import Inches

# Path to the folder containing CSV files and Word document template
csv_folder = r"I:\MAINDRIVE\Work\auto_tran_table\utils\output"
doc_template = r"I:\MAINDRIVE\Work\auto_tran_table\template\Bank of india.docx"

# Iterate over the CSV files in the folder
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith(".csv"):
        # Load the CSV data into a pandas DataFrame
        data = pd.read_csv(os.path.join(csv_folder, csv_file))

        # Create a new Word document from the template
        doc = Document(doc_template)

        # Select the table in the Word document (assuming it's the first table in the document)
        table = doc.tables[0]

        # Add a new row for each row in the CSV data
        for i, row in data.iterrows():
            # Add a new row to the table
            new_row = table.add_row()

            # Set the values for each cell in the new row
            new_row.cells[0].text = str(row["Date"])
            new_row.cells[1].text = str(row["transactions"])
            new_row.cells[2].text = str(row["cheque_no"])
            new_row.cells[3].text = str(row["debit"])
            new_row.cells[4].text = str(row["credit"])
            new_row.cells[5].text = str(row["balance"])
            # Repeat for each column in your CSV file

        # Save the updated Word document with a new filename based on the CSV filename
        doc_filename = os.path.splitext(csv_file)[0] + ".docx"
        doc.save(os.path.join(csv_folder, doc_filename))
