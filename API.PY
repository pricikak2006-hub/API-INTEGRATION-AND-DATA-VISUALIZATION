import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# API CONFIGURATION
# -----------------------------
API_KEY = "3c3e0b530a7e674df530c686f1b6c553"
CITY = "Chennai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -----------------------------
# FETCH DATA
# -----------------------------
response = requests.get(URL)
data = response.json()

# -----------------------------
# EXTRACT DATA
# -----------------------------
records = []

for item in data["list"]:
    date = item["dt_txt"].split(" ")[0]   # Only date
    records.append({
        "Date": date,
        "Temperature": item["main"]["temp"],
        "Humidity": item["main"]["humidity"]
    })

df = pd.DataFrame(records)

# -----------------------------
# DAILY AVERAGE (ONE WEEK STYLE)
# -----------------------------
daily_df = df.groupby("Date").mean().reset_index()

# -----------------------------
# VISUALIZATION
# -----------------------------
sns.set(style="whitegrid")
plt.figure(figsize=(12, 7))

# Temperature
plt.subplot(2, 1, 1)
sns.lineplot(x="Date", y="Temperature", data=daily_df, marker="o")
plt.title("Daily Average Temperature – Chennai")
plt.ylabel("Temperature (°C)")

# Humidity
plt.subplot(2, 1, 2)
sns.lineplot(x="Date", y="Humidity", data=daily_df, marker="o")
plt.title("Daily Average Humidity – Chennai")
plt.ylabel("Humidity (%)")

plt.tight_layout()
plt.show()
