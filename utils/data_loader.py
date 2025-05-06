"""
data_loader.py

Carga y procesamiento del corpus MentalRiskES en formato DataFrame para clasificación binaria a nivel de usuario.
"""

import os
import json
import pandas as pd
from text_cleaning import clean_text

def build_df_from_folder(json_dir: str, csv_path: str) -> pd.DataFrame:
    """
    Construye un DataFrame de usuarios a partir de una carpeta de archivos .json
    y un archivo CSV con etiquetas binarias.

    - Agrupa y concatena todos los mensajes por usuario
    - Limpia los textos con `clean_text`
    - Devuelve un DataFrame con columnas: ['user', 'label', 'message_clean']

    Parámetros:
    json_dir (str): Ruta a la carpeta con archivos .json (uno por usuario).
    csv_path (str): Ruta al archivo CSV con etiquetas (columnas: 'nick', 'bs').

    Retorna:
    pd.DataFrame: DataFrame con texto concatenado limpio y etiqueta binaria por usuario.

    Lanza:
    ValueError: si no se encuentran mensajes válidos.
    """
    labels_df = (pd.read_csv(csv_path, sep="\t")[["nick", "bs"]]
                 .rename(columns={"nick": "user", "bs": "label"})
                 .dropna())

    rows = []
    for file in os.listdir(json_dir):
        if file.endswith(".json") and file.startswith("subject"):
            user_id = file[:-5]
            label_row = labels_df[labels_df["user"] == user_id]
            if label_row.empty:
                continue
            label = int(label_row["label"].values[0])

            with open(os.path.join(json_dir, file), encoding="utf-8") as f:
                msgs = json.load(f)

            for m in msgs:
                if "message" in m and isinstance(m["message"], str):
                    rows.append({"user": user_id,
                                 "message": m["message"],
                                 "label": label})

    df_msgs = pd.DataFrame(rows)
    if df_msgs.empty:
        raise ValueError(f"¡Sin datos en {json_dir}!")
    
    df_msgs["message_clean"] = df_msgs["message"].apply(clean_text)

    df_user = (df_msgs
               .groupby(["user", "label"])["message_clean"]
               .agg(lambda col: " ".join(col))
               .reset_index())
    return df_user
