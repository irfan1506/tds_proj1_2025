import requests
import json

with open("cookies.txt", "r") as file:
    cookie = file.read().strip()

headers = {    
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0"  # Add this to reduce chance of block
}

url = "https://discourse.onlinedegree.iitm.ac.in/directory_items?period=yearly&order=likes_received&user_field_ids=1&plugin_column_ids=8%7C10"

response = requests.get(url, headers=headers)

# Print status and text to debug
print("Status code:", response.status_code)
print("Response text (first 500 chars):")
print(response.text[:500])  # Avoid printing huge response

# Check if it's valid JSON
try:
    data = response.json()
    with open("discourse.json", "w") as file:
        json.dump(data, file, indent=4)
except json.JSONDecodeError:
    print("❌ Error: Response is not valid JSON.")
