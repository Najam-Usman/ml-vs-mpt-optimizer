from __future__ import annotations
import time
from pathlib import Path
import pandas as pd
import yfinance as yf


TICKERS = ["AAPL", "MSFT", "AMZN", "META", "NVDA", "SPY", "TLT", "GLD"]
START = "2018-01-01"
END = None               
MAX_RETRIES = 3
SLEEP_BETWEEN = 1.0     


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
COMBINED_PATH = BASE_DIR / "data" / "combined_prices.csv"
RAW_DIR.mkdir(parents=True, exist_ok=True)
COMBINED_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Saving per-ticker CSVs to:", RAW_DIR)
print("Saving combined CSV to   :", COMBINED_PATH)

def fetch_one(ticker: str, start: str, end: str | None) -> pd.DataFrame:
  
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            df = yf.download(ticker, start=start, end=end,
                             progress=False, auto_adjust=True)
            if df.empty:
                raise ValueError(f"No data for {ticker}")

        
            if "Close" not in df.columns:
                raise KeyError(f"'Close' not in columns for {ticker}: {list(df.columns)}")

            one = df[["Close"]].rename(columns={"Close": ticker})
            one.index.name = "Date"
            one.columns.name = None
            return one
        except Exception:
            if attempt == MAX_RETRIES:
                raise
            time.sleep(SLEEP_BETWEEN * attempt)

def main():
    frames = []
    for t in TICKERS:
        one = fetch_one(t, START, END)   

        # --- CLEANUP  ---
        if isinstance(one.columns, pd.MultiIndex):
            one = one.copy()
            one.columns = one.columns.get_level_values(-1)
        one = one.rename(columns={one.columns[0]: t})
        one.columns.name = None        
        one.index.name = "Date"          


        # Save per-ticker CSV (clean)
        out_path = RAW_DIR / f"{t}.csv"
        one.to_csv(out_path, header=[t], index_label="Date")
        print(f"Wrote clean per-ticker CSV: {out_path}")

        frames.append(one)
        time.sleep(SLEEP_BETWEEN)

    # Combine all tickers into one DataFrame
    combined = pd.concat(frames, axis=1).sort_index()

    if isinstance(combined.columns, pd.MultiIndex):
        combined.columns = combined.columns.get_level_values(-1)
    combined.columns.name = None
    combined.index.name = "Date"

    combined_ffill = combined.ffill().dropna(how="any")
    combined_ffill.to_csv(COMBINED_PATH)

    print(f"\nSaved per-ticker CSVs in: {RAW_DIR}")
    print(f"Saved combined matrix at : {COMBINED_PATH}")



if __name__ == "__main__":
    main()

