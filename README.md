# 📈 GainerStreamX

**Multi-source scraper for top stock gainers with modular design and data merging utilities.**

---

## 🚀 Overview

**GainerStreamX** is a stock momentum scanner designed to track **top gainers** in **pre-market and regular trading hours.** It **scrapes live data** from **multiple sources** and merges critical trading metrics into a single dataset for further analysis.

In its **current version**, GainerStreamX scrapes from:

* **StockTitan** (top gainers + detailed stock info)
* **StockAnalysis** (top gainers + price & volume)

🔄 **Upcoming releases** will expand to include APIs like **TD Ameritrade, Webull, and more.**

---

## 🛠️ Current Features

✅ **Top Gainers Scraping:**

* **StockTitan:**

  * Top gainers list
  * Stock fundamentals: market cap, float, short % interest, industry, sector, country
  * News sentiment: news link, impact stars, sentiment stars
* **StockAnalysis:**

  * Top gainers list
  * Price & volume for individual stocks

✅ **Data Utilities:**

* **Deduplication:** Removes duplicate stock entries (keeps the one with the highest % change)
* **Top K Filter:** Extracts the top *K* gainers based on % change
* **Data Merging:** Merges up to three DataFrames (on the `name` column)

✅ **Parallel Execution:**

* Runs **scraping tasks in parallel** using Python's `ThreadPoolExecutor` for speed

✅ **Output:**

* Merged DataFrame saved as `merged_df.csv`

---

## 🚧 Roadmap & Upcoming Features

🚀 **Planned Enhancements:**

* **New Data Sources:**

  * TD Ameritrade API (gap %, live quotes)
  * Webull (DOM & order flow scraping)
  * TradeStation & other brokers

* **Momentum Filters & Auto-Grading:**

  * Custom filters (e.g., price range, float cap, RVOL ≥ 5x)
  * Stock grading (A/B/C/D) based on momentum criteria

* **Visualization:**

  * **Dash/React Bookmap-style UI:**

    * Real-time bid/ask heatmaps
    * Order flow and time & sales visualizations

* **Alerts & Notifications:**

  * Real-time momentum alerts (Discord, Telegram)

---

## ⚙️ Technical Architecture

### ✅ Current Modules

* **Scraper Module:**

  * `scrape_stocktitan()`
  * `scrape_stockanalysis()`
  * `get_price_volume_stockanalysis()`
  * `get_details_stocktitan()`

* **Utilities Module:**

  * `remove_duplicates_keep_highest()`
  * `get_top_k_df()`
  * `merge_dataframes_on_key()`

### 📡 Current Data Pipeline

1️⃣ **Scrape top gainers** from StockTitan & StockAnalysis (parallelized)

2️⃣ **Deduplicate** (keep the highest % change)

3️⃣ **Get top K gainers** (configurable)

4️⃣ **Scrape details:**

* Price & volume (StockAnalysis)
* Fundamentals & news (StockTitan)

5️⃣ **Merge all data** and export to CSV

---

## 🔧 Tech Stack

| **Area**         | **Stack**                                |
| ---------------- | ---------------------------------------- |
| Backend          | Python (requests, BeautifulSoup, pandas) |
| Parallelism      | ThreadPoolExecutor (concurrent.futures)  |
| Data Output      | CSV export                               |
| Planned Frontend | Dash (Python) / React (JavaScript)       |

---

## 🚀 How to Run

1️⃣ **Install requirements:**

```bash
pip install -r requirements.txt
```

2️⃣ **Run the script:**

```bash
python main.py
```

3️⃣ **Output:**

* Top gainers + detailed info saved in `merged_df.csv`

---

## 🙌 Contributions

✅ We welcome help with:

* Adding new **data sources** (APIs or scrapers)
* Improving **performance** (parallelism, speed)
* Implementing **visualization modules**
* Enhancing the **alert system**

Feel free to submit issues or pull requests 🚀.

---

## 📢 Notes

* This project currently **focuses on scraping + merging data only.**
* Features like **alerts, auto-grading, visualization, and more advanced API integrations** are **planned but not yet implemented.**
* Always respect **site terms of use** when scraping third-party data.

---

# 🚀 Happy Trading!

