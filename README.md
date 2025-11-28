# Financial Data Pipeline (AlphaVantage API)
A complete end-to-end automated financial data pipeline written in Python.
This project downloads stock price data from AlphaVantage, cleans it, computes technical indicators, and generates a multi-sheet Excel report.

Perfect for learners, analysts, and automated trading workflows.

## Features
### Fetch Stock Data
Uses the AlphaVantage TIME_SERIES_DAILY endpoint to download daily historical price data for selected stocks.

### Clean + Standardize Data
* Converts date column
* Converts numeric columns
* Removes invalid rows
* Fills missing values with forward/backward fill

### Technical Indicators Included

** The pipeline automatically adds: **

Category	Indicators
Returns	Daily % returns
Volatility	30-day, 60-day rolling volatility
SMA	20, 50, 200 period simple moving averages
EMA	20, 50 period exponential moving averages


### Excel Report
Generates a clean Excel file:
```
Financial_Report.xlsx
```
Each stock appears in its own sheet with all processed columns included.

### Project Structure
```bash
financial_pipeline/
│
├── config.py               # API key, stock list, base URL
├── fetch_data.py           # Fetch stock data from AlphaVantage
├── clean_data.py           # Clean and standardize the dataset
├── indicators.py           # Add technical indicators
├── generate_report.py      # Create the Excel report
└── main.py                 # Main pipeline runner
```
### Installation & Setup
#### 1. Clone the repository
```bash
git clone <your-repo-url>
cd financial_pipeline
```
#### 2. Create a virtual environment
```bash
python -m venv .venv
```
#### 3. Activate the environment
##### Windows:
```bash
.venv\Scripts\activate
```
#### Mac/Linux:
```bash
source .venv/bin/activate
```
### 4. Install dependencies
```bash
pip install pandas requests xlsxwriter
```

### Configure Your API Key
Create a free AlphaVantage account:
👉 https://www.alphavantage.co/

Edit config.py:
```python
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
BASE_URL = "https://www.alphavantage.co/query?"
SYMBOLS = ["AAPL", "MSFT", "GOOGL", "TSLA", "META"]
```

### Running the Pipeline
Run:
```bash
python main.py
```
Expected output:
```
Report generated: Financial_Report.xlsx
Done! Pipeline completed successfully.
```

### Requirements
* Python 3.8+
* pandas
* requests
* xlsxwriter

### How It Works
1. 	** main.py ** loads stock symbols
2. ** fetch_all_stock_data ** downloads prices from AlphaVantage
3. ** clean_df() ** handles missing/invalid values
4. ** add_indicators() ** calculates SMA, EMA, volatility, etc.
5. ** generate_excel_report() ** creates a multi-sheet Excel file

### Contributions
Contributions are welcome!
Feel free to open issues or submit pull requests.
