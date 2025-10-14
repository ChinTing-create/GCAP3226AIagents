import requests
import pandas as pd

# Direct resource link (CSV or other format)
resource_url = "https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001/resource/469128e7-d65a-4040-ba1a-0a734361f512/download/tablechart-110-01001.csv"

response = requests.get(resource_url)
if response.status_code == 200:
    with open("tablechart-110-01001.csv", "wb") as f:
        f.write(response.content)
    print("Data downloaded and saved as tablechart-110-01001.csv")
    # Optionally, load and preview with pandas
    df = pd.read_csv("tablechart-110-01001.csv")
    print(df.head())
else:
    print("Failed to fetch data. Status code:", response.status_code)
