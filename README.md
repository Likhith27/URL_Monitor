# 🌐 URL Health Monitor

A web-based tool that allows users to input multiple URLs and check whether the websites are **UP or DOWN**, along with their **response time**. The application also keeps track of past results and visualizes the **health metrics over time**.

---

## 🧠 Project Overview

The **URL Health Monitor** is designed to help users quickly assess the status and responsiveness of multiple websites. By inputting a list of URLs, users can instantly check if each website is UP or DOWN, view the response time, and track the availability history over time.

---

## 🚀 Core Features

- ✅ **Check Status**  
  Instantly determine if a URL is reachable (UP) or not (DOWN) based on HTTP response codes.

- ⚡ **Response Time**  
  Measure and display how long each request takes (in milliseconds).

- 🗂️ **Historical Data Storage**  
  Logs all checks with timestamps and stores them in a database.

- 📈 **Health Metrics Over Time**  
  Graphs showing average uptime percentage and response times for each URL.

- 🖥️ **Interactive GUI**  
  User-friendly interface to input multiple URLs, view current status, and analyze trends.

- 📬 **Notifications** *(optional)*  
  Send alerts if a URL remains down for multiple checks (via email or UI popup).

---

## 🧱 Tech Stack (Suggested)

| Layer      | Tools                                 |
|------------|----------------------------------------|
| Frontend   | React.js / Vue.js, Tailwind CSS        |
| Backend    | Flask / Django / Node.js               |
| Database   | SQLite (dev) / MongoDB (prod-ready)    |
| Visualization | Chart.js / D3.js                    |
| Task Scheduler | Cron / Celery / APScheduler        |

---

## 🛠️ Installation Guide

### 1. Clone the Repository
git clone https://github.com/yourusername/url-health-monitor.git
cd url-health-monitor

cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

cd frontend
npm install
npm start

url-health-monitor/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── check_urls.py
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── App.jsx
│   └── ...
├── database/
│   └── logs.db
├── README.md
└── requirements.txt


