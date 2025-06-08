# 🌐 URL Health Monitor

This is a lightweight web app that allows users to monitor the availability of multiple URLs. Users can enter a list of websites and check whether they are **UP** or **DOWN**, see **response times**, and track **uptime history** over time.

Built with **Python + Streamlit**, containerized with **Docker**, and developed using **Windsurf**, Codeium’s agentic AI IDE.

---

## 🚀 Features

- ✅ **Enter multiple URLs** via a simple web UI.
- 🔍 **Check real-time status** of each URL (UP/DOWN).
- ⚡ **See response time** in milliseconds.
- 🗂 **Persist historical results** using JSON.
- 📊 **Uptime statistics** shown in a sidebar.
- 🐳 **Dockerized** for portable deployment.

---

## 🖼️ UI Overview

- **Main Input Area**: Paste URLs (one per line).
- **Check URLs Button**: Starts health check.
- **Results Table**: Displays current statuses and timings.
- **Sidebar**: Select a URL to view uptime metrics like:
  - Uptime %
  - Total checks
  - Count of UP states
  - Recent results table

---

## 🧱 Tech Stack

| Layer     | Tech        |
|-----------|-------------|
| Language  | Python 3.10 |
| Frontend  | Streamlit   |
| Backend   | `requests` for HTTP checks |
| Storage   | JSON file-based logging (`history/results.json`) |
| Container | Docker      |
| AI Assist | Windsurf (Codeium) |

---

## 📂 Project Structure


---

## 🐳 Running with Docker

📁 url-health-monitor/
├── app.py # Streamlit app frontend
├── monitor.py # Core logic for URL health checks
├── Dockerfile # Containerization setup
├── requirements.txt # Python dependencies
└── history/
└── results.json # JSON store of all past URL checks


## 🐳 Running with Docker

```bash
docker build -t url-health-monitor .
docker run -p 8501:8501 url-health-monitor

pip install -r requirements.txt
streamlit run app.py
```
📊 Example URLs

https://www.google.com
https://openai.com
https://some-nonexistent-site.abc

📈 Future Enhancements

Scheduled auto-checks (cron/Celery)
Alert notifications
Graphical dashboards
User authentication

🙌 Acknowledgements

Built using Windsurf by Codeium
Streamlit for UI
Requests for backend checks

👨‍💻 Author
[Your Name]

Here is the video link of My project.

[https://www.loom.com/share/3033ffc336524bdb8744e5e709c7f7e8?sid=220b8151-e844-42a7-989a-6cf5394e078d](VideoLink)
