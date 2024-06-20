import json
import requests
from datetime import date
import csv

data_numerica_general = []
module = 5
url_start_point = 14710
with open('lastdate.txt','r') as df:
    date_str=df.read()
target_date = date.fromisoformat(date_str)
today = date.today()
days_diff = (today - target_date).days
result = 5 * days_diff
url_current = url_start_point + result

while url_current > url_start_point:
    print(f'Getting shit for id {url_current}')
    url = f'https://resultadosquiniela.cajapopular.gov.ar/api/extracto-registro/?id={url_current}'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        if isinstance(json_data, list) and json_data:
            for item in json_data:
                data_numerica_general.append((item["numero"]))
        else:
            pass
    else:
        print(f"Failed to retrieve data for {url_start_point} due to {response.status_code}")
    url_current = url_current - 1

if len(data_numerica_general) > 0:
    with open("processed_data.csv", "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
    
    for item in data_numerica_general:
        csv_writer.writerow([item])
    with open("lastdate.txt",'w') as df:
        df.write(str(today))