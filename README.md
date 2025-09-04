# ml-vs-mpt-optimizer

**Can Machine Learning Beat Modern Portfolio Theory (MPT)?**

## 🚀 Overview
This project explores whether **machine learning (ML)** can outperform the classical **Modern Portfolio Theory (MPT)** in portfolio optimization.  
It combines a **modular Python toolkit** with an **interactive Streamlit dashboard** to compare traditional finance methods against ML-driven strategies.

## 🔑 Features
- **Data Pipeline:** Fetch historical stock/ETF data (Yahoo Finance).  
- **Classical Optimization (MPT):**
  - Minimum Volatility Portfolio
  - Maximum Sharpe Ratio Portfolio
  - Efficient Frontier visualization
- **Machine Learning Models:**
  - Predict next-day returns with Linear Regression, Random Forest, and LSTM.
  - Use forecasts as inputs for portfolio allocation.
- **Backtesting & Metrics:**
  - Portfolio growth, Sharpe ratio, volatility, max drawdown.
  - Rolling performance analysis for stability checks.
- **Visualization:**
  - Allocation breakdowns, efficient frontier, equity curves.
- **Streamlit Dashboard:**
  - User-provided tickers → allocations + comparative plots.

## 👥 Audience
- **Recruiters & Interviewers:** Demonstrates applied quant + ML knowledge.  
- **Data Science Peers:** End-to-end project with finance + ML integration.  
- **Investors & Enthusiasts:** Learn how ML might (or might not) improve portfolios.

## 📂 Deliverables
- Modular Python code (`data/`, `optimize/`, `backtest/`, `viz/`).  
- Streamlit app for interactive exploration.  
- Reports summarizing each stage (MPT baseline, ML experiments, backtests).  
- Blog post: *Can ML Beat Modern Portfolio Theory?*  

---

## 📊 Progress So Far
- **EDA:** Cleaned and analyzed asset returns, volatilities, and correlations.  
- **Classical MPT:**  
  - Built Min Vol and Max Sharpe portfolios.  
  - Found corner solutions (e.g., 63% GLD + 33% NVDA).  
  - Added 30% cap → more diversification, lower Sharpe.  
  - Introduced stability metric (Effective N_assets).  
  - **Insight:** MPT is mathematically optimal but unstable in practice → perfect baseline for ML comparison.  

---

> ⚡ **Next Steps:** Implement ML-based optimizers and compare Sharpe, stability, and robustness against classical MPT.  
