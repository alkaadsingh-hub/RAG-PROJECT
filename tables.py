#Extracting tables

import pdfplumber
import os
import pandas as pd

def extract_tables(pdf_path):
    os.makedirs("data/tables", exist_ok=True)

    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            tables = page.extract_tables()

            for table_index, table in enumerate(tables):
                df = pd.DataFrame(table)

                # Clean table
                df.dropna(how="all", inplace=True)
                df.fillna("", inplace=True)

                # Save CSV
                csv_path = f"data/tables/page_{page_num}_table_{table_index}.csv"
                df.to_csv(csv_path, index=False)

                # Convert to markdown text
                table_text = f"Table from page {page_num}:\n" + df.to_markdown(index=False)

                all_tables.append({
                    "content": table_text,
                    "metadata": {
                        "type": "table",
                        "page": page_num,
                        "table_id": table_index
                    }
                })

    return all_tables