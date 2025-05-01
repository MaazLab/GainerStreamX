# 📈 GainerStreamX

**Real-time multi-source scraper for top stock gainers, with integrated data visualization and analysis tools.**

---

## 🚀 Overview

**GainerStreamX** is a **real-time stock momentum scanner** designed to track **top gainers** in **pre-market and regular market hours**. It scrapes data from **multiple sources** (e.g., TD Ameritrade, Webull, StockTitan) and compiles critical trading metrics for **small-cap stocks**, such as:

- **Gap percentage**
- **Price & volume**
- **Float & relative volume**
- **Short interest**
- **Fundamentals & news impact**

GainerStreamX is built for **momentum day traders** who need actionable data and alerts to spot high-potential trading opportunities—fast.

---

## 🛠️ Scope & Key Features

- **📊 Real-Time Top Gainers Scanner:**  
  Scrapes and tracks top movers live from **multiple data sources**:
  - TD Ameritrade API
  - Webull (via screen scraping)
  - StockTitan for news & catalyst data
  - Optional: TradeStation & other sources (future-ready)

- **💡 Momentum Filters:**  
  Built-in filters for small-cap momentum trading (e.g., price between $2–$20, float ≤ 20M, RVOL ≥ 5x).

- **📰 News Sentiment & Catalyst Detection:**  
  Uses **StockTitan** to pull:
  - Latest stock news headlines
  - Rhea-AI Impact & Sentiment metrics (converted to High/Medium/Low impact)

- **🔔 Quality Grading & Alerts:**  
  Each stock is auto-graded (A/B/C/D) based on key momentum criteria:
  - Gap %
  - Float
  - RVOL
  - News presence
  - Real-time alerts for fresh momentum spikes

- **📈 Visualization: Bookmap-Style UI:**  
  A **Bookmap-like visualization tool** (planned with **Dash/React**):
  - DOM (Depth of Market) visualization
  - Order flow heatmaps & bubble charts
  - Real-time bid/ask ladder and Time & Sales highlights

- **📊 Fundamental Snapshot Panel:**  
  Pulls **bare minimum fundamental data** (e.g., Market Cap, Float, Cash/Debt, Revenue) for quick decision-making.

---

## ⚙️ Technical Information

**✅ Modular Architecture:**  
GainerStreamX is built with a **modular design**—each **data source** (TD Ameritrade, Webull, StockTitan, etc.) is implemented as a **separate module**. This means:

- ✅ **Easy to swap, upgrade, or add new data sources** in the future.
- ✅ Clear separation of concerns: scraping logic, data processing, visualization, and alerting are **decoupled**.
- ✅ Flexible integration for **APIs**, **screen scraping (OCR/OpenCV)**, and **desktop automation tools**.

**📡 Data Pipeline:**

1. **Scanner Module:**  
   Scrapes real-time stock metrics, applying filters (e.g., HOD within last 2 min, RVOL ≥ 5x).

2. **News & Catalyst Module:**  
   Pulls StockTitan data for headlines + Rhea-AI metrics.

3. **Fundamental Module:**  
   Collects fundamentals (Market Cap, Float, Cash, Debt, Revenue) via StockAnalysis.com scraping/API.

4. **Visualization Module:**  
   Uses **Dash (Python)** or **React (JS)** to render:
   - Price ladder
   - Heatmap trails
   - Bid/Ask bubbles
   - Time & Sales visual flow

5. **Alert & Quality Scoring Module:**  
   Assigns a **Quality Score (A/B/C/D)** and pushes alerts for top setups.

**🔧 Tech Stack:**

- **Backend:**
  - Python (requests, BeautifulSoup, Selenium, OpenCV, Tesseract)
  - TD Ameritrade API
  - TradeStation API (planned)
  - Custom screen scraping logic (Webull)
  
- **Frontend:**
  - Dash (Python framework) / React (JavaScript alternative)
  - Plotly for visual plots
  - WebSocket-based live updates (planned)

- **Extras:**
  - SQL/CSV for local caching of float data
  - Modular config for RVOL, filters, and quality grading

---

## 🚧 Roadmap & Future Plans

- ✅ **Phase 1:**  
  Core scraping + fundamental/news module (WIP)

- 🔄 **Phase 2:**  
  Dash/React visualization build-out + Bookmap-style UI

- 🔄 **Phase 3:**  
  Live alert system + webhook integration (e.g., Discord, Telegram)

- 🔄 **Phase 4:**  
  Modular plug-ins for **additional data sources** (e.g., ChartMill, Benzinga)

---

## 📝 Developer Notes

- **APIs & Auth:**  
  TD Ameritrade requires OAuth flow; ensure token refresh handling is in place.

- **Screen Scraping:**  
  For Webull, leverage **OCR (Tesseract)** or **visual automation (PyAutoGUI/OpenCV)** to extract DOM and Time & Sales data.

- **Data Refresh Rate:**  
  Designed for **sub-minute polling** where possible; may require rate-limit handling.

- **Visualization:**  
  Bookmap-style design prioritizes **real-time order flow analysis**—visualizing bid/ask bubbles and HOD lines.

---

## 🙌 Contributions

We welcome contributions, especially for:

- Additional **data sources**
- Enhancements to the **visualization**
- Performance optimizations (e.g., scraping speed, parallelism)
