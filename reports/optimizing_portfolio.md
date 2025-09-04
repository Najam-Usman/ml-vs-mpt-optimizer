# Day 3 — Classical Portfolio Optimization

## Overview
In this stage, we implemented **Modern Portfolio Theory (MPT)** as the classical baseline for portfolio construction.  
Our goals were:
- Build the **Minimum Volatility Portfolio** and **Maximum Sharpe Ratio Portfolio**.  
- Examine the limitations of unconstrained optimization.  
- Add a **30% position cap** to show how practical constraints change results.  
- Introduce **stability metrics** beyond Sharpe ratio.  

This report summarizes the results, insights, and the motivation for exploring ML-based approaches.

---

## Methodology
- **Inputs:**  
  - Assets: AAPL, MSFT, AMZN, META, NVDA, SPY, TLT, GLD  
  - Period: 2018–present daily adjusted close prices  
  - Annualized returns (μ) and covariance (Σ) from Day 2  

- **Optimizer:**  
  - Objective: maximize Sharpe ratio or minimize volatility  
  - Constraints:  
    - Long-only (weights ≥ 0)  
    - Fully invested (Σ weights = 1)  
  - Extension: position cap (≤ 30% per asset)  

- **Metrics:**  
  - Return, volatility, Sharpe ratio  
  - Effective number of assets (N_eff)  

---

## Results

### 1. Minimum Volatility Portfolio
- Heavy allocation to defensive assets (TLT, GLD, SPY).  
- Lowest risk profile.  
- Sharpe ratio relatively modest.  

### 2. Maximum Sharpe Portfolio (Unconstrained)
- Extremely concentrated: ~63% GLD, ~33% NVDA.  
- Achieved Sharpe ≈ **1.72**.  
- Effective N_assets ≈ **2.1** → effectively a two-asset portfolio.  
- Corner solution: unstable, highly sensitive to inputs.

### 3. Maximum Sharpe Portfolio (Cap 30%)
- More diversified: spread across GLD, NVDA, AAPL, MSFT, TLT.  
- Sharpe fell to ≈ **1.61**.  
- Effective N_assets higher → more robust portfolio.  
- Demonstrates trade-off: some efficiency sacrificed for stability.

---

## Stability Metrics
- **Effective Number of Assets (N_eff):**
  - Unconstrained: ~2 (overly concentrated).  
  - Cap 30%: higher, more diversified.  
- **Takeaway:** Stability improves with constraints, even though raw Sharpe falls.  

(Turnover to be measured when we do rolling backtests.)

---

## Key Insights
- **Plain MPT** produces mathematically optimal portfolios but impractical allocations.  
- **Constraints** reduce efficiency but yield portfolios closer to real-world practice.  
- **Stability metrics** reveal the true cost of corner solutions.  
- This highlights a fundamental tension in quant finance:  
  > *Efficiency vs Robustness.*  

---

## Bridge to ML
- MPT is **backward-looking** (historical averages).  
- Sensitive to estimation error and produces unstable weights.  
- In practice, advanced models (Black-Litterman, shrinkage covariance, robust optimization) improve this — but for this project, we benchmark against plain MPT.  
- **Next step:** Test whether ML forecasts and adaptive approaches can improve Sharpe and stability while avoiding corner solutions.
