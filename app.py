# app.py

import streamlit as st
import os
import json
from monitor import check_url_health, calculate_uptime, get_uptime_details
import pandas as pd

st.set_page_config(page_title="URL Health Monitor", layout="wide")
st.title("🌐 URL Health Monitor")
st.caption("Enter URLs (one per line)")

os.makedirs("history", exist_ok=True)
HISTORY_FILE = "history/results.json"

# Load previous results
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

# Save updated results
def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# UI: Text input
urls_input = st.text_area("Enter URLs", height=150, placeholder="https://www.google.com/\nhttps://example.com")
urls = [url.strip() for url in urls_input.splitlines() if url.strip()]

# Button
if st.button("🔍 Check URLs"):
    history = load_history()

    new_results = []
    for url in urls:
        result = check_url_health(url)
        history.append(result)
        new_results.append(result)

    save_history(history)

    st.subheader("Results")
    df = pd.DataFrame(new_results)
    st.dataframe(df)

# Sidebar: Browse history + uptime stats
st.sidebar.title("📊 Uptime Stats")
history = load_history()
unique_urls = list({entry["url"] for entry in history})
selected = st.sidebar.selectbox("Select URL", unique_urls)

if selected:
    uptime_percentage, up_count, total_count = get_uptime_details(history, selected)
    st.sidebar.markdown(f"**Uptime:** `{uptime_percentage}`")
    st.sidebar.markdown(f"**Total Checks:** `{total_count}`")
    st.sidebar.markdown(f"**UP Count:** `{up_count}`")
    st.sidebar.markdown("---")
    st.sidebar.write("Recent Checks:")
    recent = [h for h in reversed(history) if h["url"] == selected][:10]
    st.sidebar.table(recent)
