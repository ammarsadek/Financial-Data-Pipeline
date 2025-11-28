from fetch_data import fetch_all_stock_data
from clean_data import clean_df
from indicators import add_indicators
from generate_report import generate_excel_report
from config import SYMBOLS

def main():
    print("Fetching stock data...")
    data = fetch_all_stock_data(SYMBOLS)

    processed = {}

    print("Cleaning + calculating indicators...")
    for symbol, df in data.items():
        df = clean_df(df)
        df = add_indicators(df)
        processed[symbol] = df

    print("Generating Excel report...")
    generate_excel_report(processed)

    print("Done! Pipeline completed successfully.")

if __name__ == "__main__":
    main()