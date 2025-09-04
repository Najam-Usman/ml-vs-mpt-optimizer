Assets selected:
    - AAPL
    - MSFT
    - AMZN
    - META
    - NVDA
    - SPY
    - TLT
    - GLD

Reasoning: Selected a mix of tech (growth), index (market baseline), bond (defensive) and gold (hedge) to keep a diverse portfolio. 


Timeframe: Jan 2018 - present

Reasoning:  ~6 years of daily data. Includes volatile periods (COVID crash, post-COVID boom, inflation cycle). This timeframe is enough to show how strategies behave across regimes (bull, bear, inflation).

Constraints:
    - Long-only: based off real-world trading and keeps things simple
    - Fully invested: keeps the math clean
    - 2% Risk-free rate assumption: needed for sharpe ratio calculation
    - Monthly Rebalancing : markets change; rebalancing lets you adapt. 


Looking at Adjusted Closing Price instead of regular closing price.

Reasoning: Regular close price can fluctuate due to stock splits or dividends. Adjusted close smooths that out and gives us a true comparable series for returns. Without this, our return calculations could be misinterpretated. For example, Apple's 4-for-1 split in 2020 would look like a crash. 

