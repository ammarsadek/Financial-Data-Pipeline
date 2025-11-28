import pandas as pd

def generate_excel_report(stock_data, file_name="Financial_report.xlsx"):
    writer = pd.ExcelWriter(file_name, engine="xlsxwriter")

    for symbol, df in stock_data.items():
        df.to_excel(writer, sheet_name=symbol, index=False)

    writer.close()
    print(f"Report generated: {file_name}")

