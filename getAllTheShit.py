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
    
    from datetime import date
    todate = str(date.today())
    list_length = len(data_numerica_general)
    start_index = list_length - 100
    last_100 = data_numerica_general[start_index:]
    elements_per_sublist = (len(last_100) // 5)
    sublists = []

    for i in range(0, len(last_100), elements_per_sublist):
        sublist = last_100[i:i+elements_per_sublist]
        sublists.append(sublist)
    output_dict = {
    "Nocturno": sublists[0],
    "De la tarde": sublists[1],
    "De la siesta": sublists[2],
    "Vespertino": sublists[3],
    "Matutino": sublists[4],
}
    
    with open(f"Winners_{todate}.json", "w") as outfile:
        json.dump(output_dict, outfile, indent=4)