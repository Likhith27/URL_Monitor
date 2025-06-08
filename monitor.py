# # monitor.py

# import requests
# import time

# def check_url_health(url):
#     try:
#         start = time.time()
#         response = requests.get(url, timeout=5)
#         end = time.time()
#         return {
#             "url": url,
#             "status": "UP" if response.status_code == 200 else "DOWN",
#             "time_ms": round((end - start) * 1000, 4)
#         }
#     except Exception:
#         return {
#             "url": url,
#             "status": "DOWN",
#             "time_ms": None
#         }

# def calculate_uptime(history, url):
#     total_checks = sum(1 for entry in history if entry["url"] == url)
#     up_checks = sum(1 for entry in history if entry["url"] == url and entry["status"] == "UP")
#     if total_checks == 0:
#         return "No data"
#     return f"{(up_checks / total_checks) * 100:.2f}%"

# monitor.py

import requests
import time

def check_url_health(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()
        return {
            "url": url,
            "status": "UP" if response.status_code == 200 else "DOWN",
            "time_ms": round((end - start) * 1000, 4)
        }
    except Exception:
        return {
            "url": url,
            "status": "DOWN",
            "time_ms": None
        }

def calculate_uptime(history, url):
    total_checks = sum(1 for entry in history if entry["url"] == url)
    up_checks = sum(1 for entry in history if entry["url"] == url and entry["status"] == "UP")
    if total_checks == 0:
        return "No data"
    return f"{(up_checks / total_checks) * 100:.2f}%"

def get_uptime_details(history, url):
    total = sum(1 for entry in history if entry["url"] == url)
    up = sum(1 for entry in history if entry["url"] == url and entry["status"] == "UP")
    if total == 0:
        return ("No data", 0, 0)
    percent = f"{(up / total) * 100:.2f}%"
    return (percent, up, total)
