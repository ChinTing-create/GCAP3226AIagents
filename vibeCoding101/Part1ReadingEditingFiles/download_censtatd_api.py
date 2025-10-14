import requests
import pandas as pd

# New API endpoint from input
api_url = "https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1"

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    # Save raw JSON
    with open("censtatd_110-01001.json", "w") as f:
        import json
        json.dump(data, f, indent=2)
    print("Raw JSON data saved as censtatd_110-01001.json")
    # Try to extract tabular data if available
    if 'data' in data:
        df = pd.DataFrame(data['data'])
        df.to_csv("censtatd_110-01001.csv", index=False)
        print("Tabular data saved as censtatd_110-01001.csv")
        print(df.head())
    else:
        print("No tabular 'data' field found in JSON.")
else:
    print("Failed to fetch data. Status code:", response.status_code)
