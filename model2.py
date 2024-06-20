import pandas as pd
import random
import numpy as np
import json

def generate_predictions(num_instances, num_predictions):
    all_predictions = []

    for _ in range(num_instances):
        instance_predictions = []
        while len(instance_predictions) < num_predictions:
            random_number = np.random.choice(numeros_validos)
            if random_number not in instance_predictions:
                instance_predictions.append(random_number)
        instance_predictions.sort()
        all_predictions.append(instance_predictions)

    return all_predictions

def process_predictions(predictions):
    flat_predictions = [item for sublist in predictions for item in sublist]
    padded_predictions = [str(p).zfill(4) for p in flat_predictions]
    random.shuffle(padded_predictions)
    split_size = int(len(padded_predictions) / 5)
    processed_lists = [padded_predictions[i:i+split_size] for i in range(0, len(padded_predictions), split_size)]

    return processed_lists

data = pd.read_csv("processed_data.csv")
numeros_validos = np.array(data["numero"])
X_train = numeros_validos.reshape(len(numeros_validos), 1)

num_instances = 5  # Number of instances to generate
num_predictions = 20  # Number of predictions per instance

predictions = generate_predictions(num_instances, num_predictions)
processed_lists = process_predictions(predictions)
print(processed_lists)  
output_dict = {
    "Matutino": processed_lists[0],
    "Vespertino": processed_lists[1],
    "De la siesta": processed_lists[2],
    "De la tarde": processed_lists[3],
    "Nocturno": processed_lists[4],
}

from datetime import date
todate = str(date.today())
with open(f"loterias_{todate}.json", "w") as outfile:
    json.dump(output_dict, outfile, indent=4)