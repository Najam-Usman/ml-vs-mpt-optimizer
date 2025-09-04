# Exploratory Data Analysis (EDA)

## 1. Price Trends
- *Plot:* Price history (2018–present).
- *Insights:*
  - Tech stocks (AAPL, NVDA, META) show strong growth, especially post-2020.
  - Bonds (TLT) and Gold (GLD) are much flatter — lower growth, but more stable.

## 2. Normalized Growth
- *Plot:* Prices scaled to 1.0 at Jan 2018.
- *Insights:*
  - NVDA grew ~4–5x since 2018, the strongest performer.
  - SPY roughly doubled, consistent with broad market growth.
  - GLD and TLT barely moved, confirming their defensive role.

## 3. Correlation Heatmap
- *Plot:* Daily returns correlation matrix.
- *Insights:*
  - SPY highly correlated with AAPL/MSFT (as expected).
  - GLD and TLT have low correlation with equities — useful diversifiers.
  - Within tech, correlations are strong (they move together).

## 4. Volatility Comparison
- *Plot:* Annualized volatility bar chart.
- *Insights:*
  - NVDA and META are the riskiest assets.
  - Bonds (TLT) are the least volatile.
  - SPY sits in between — less risky than individual tech names but riskier than bonds.
