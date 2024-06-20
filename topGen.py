import pandas as pd
import json

def leer_csv(ruta_archivo):
  try:
    df = pd.read_csv(ruta_archivo)
    return df
  except FileNotFoundError:
    print(f"Error: Archivo no encontrado. Ruta: {ruta_archivo}")
    return None

def convertir_a_4_digitos(df, columna):
  df[columna] = df[columna].astype(str)
  df[columna] = df[columna].str.zfill(4)
  return df

def obtener_top_5(df, columna):
  top_5 = df[columna].value_counts().nlargest(6).to_dict()
  del top_5["0000"]
  return top_5

def guardar_en_json(datos, ruta_archivo):
  with open(ruta_archivo, "w") as f:
    json.dump(datos, f, indent=4)

def main():
  ruta_archivo_csv = "processed_data.csv"
  df = leer_csv(ruta_archivo_csv)
  if df is None:
    return
  columna = "numero"

  df = convertir_a_4_digitos(df, columna)

  top_5 = obtener_top_5(df, columna)

  ruta_archivo_json = "top_5_numeros.json"
  guardar_en_json(top_5, ruta_archivo_json)

  print(f"Top 5 números guardados en: {ruta_archivo_json}")

if __name__ == "__main__":
  main()
