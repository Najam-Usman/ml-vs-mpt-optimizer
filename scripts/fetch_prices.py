import os 
from datetime import date
import time
import numpy as np
import pandas as pd
import yfinance as yf

TICKERS = ["AAPL", "MSFT", "AMZN", "META", "NVDA", "SPY", "TLT", "GLD"]
START = "2018-01-01"
END = None
RAW_DIR = "data/raw"
COMBINED_PATH = "data/combined_prices.csv"
MAX_RETRIES = 3
SLEEP_BETWEEN = 1.0

os.makedirs(RAW_DIR, exist_ok=True)

def fetch_one(ticker, start, end):

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            df = yf.download(ticker, start=start, end=end, progress=False)
            if df.empty:
                raise ValueError(f"No data for {ticker}")

            col = "Adj Close" if "Adj Close" in df.columns else "Close"
            if col not in df.columns:
                raise KeyError(f"Neither Adj Close or Close found for {ticker}. Columns: {list(df.columns)}")

            out = df[[col]].rename(columns={col: ticker})
            out.index.name = "Date"
            return out
        
        except Exception:
            if attempt == MAX_RETRIES:
                raise 
            time.sleep(SLEEP_BETWEEN * attempt)
        

def main():
    per_ticker = []

    for t in TICKERS:
        df = fetch_one(t, START, END)

        out_path = os.path.join(RAW_DIR, f"{t}.csv")
        df.to_csv(out_path)
        per_ticker.append(df)
        time.sleep(SLEEP_BETWEEN)

    combined = pd.concat(per_ticker, axis = 1).sort_index()
    combined_ffill = combined.ffill().dropna(how="any")

    os.makedirs(os.path.dirname(COMBINED_PATH), exist_ok=True)
    combined_ffill.to_csv(COMBINED_PATH)

    print("\n=== Data Quality Summary ===")
    print(f"Tickers: {TICKERS}")
    print(f"Date range (combined): {combined_ffill.index.min().date()} → {combined_ffill.index.max().date()}")
    print(f"Rows: {len(combined_ffill):,}")

    missing_counts = combined.isna().sum()
    total_rows = len(combined)
    
    for t in TICKERS:
        miss = int(missing_counts.get(t, 0))
        pct = (miss / total_rows * 100) if total_rows else 0.0
        print(f"- {t}: missing {miss} rows before ffill ({pct:.2f}%)")
    
    print("\nSaved per-ticker CSVs in data/raw/ and combined matrix at data/combined_prices.csv")



if __name__ == "__main__":
    main()

