# 📦 Instrucciones para acceder al dataset

Este proyecto utiliza el corpus **MentalRiskES 2023**, desarrollado como parte de la tarea compartida del IberLEF 2023. Este dataset contiene mensajes anónimos en español extraídos de grupos públicos de Telegram relacionados con temáticas de salud mental, etiquetados por usuarios en función de la presencia de trastornos como ansiedad, depresión o trastornos de la conducta alimentaria (TCA).

## ⚠️ Restricciones de acceso

El corpus **no puede ser subido ni distribuido** directamente por este repositorio debido a restricciones de licencia.

### ✅ Para acceder al dataset:

1. Visita la página oficial del shared task:  
   https://sites.google.com/view/mentalriskes/home

2. Completa el formulario de solicitud para acceso al dataset.

3. Acepta la licencia de uso académico.

4. Una vez aprobado, recibirás un enlace de descarga.

## 📁 Estructura esperada de carpetas

Una vez descargado el corpus, se recomienda organizarlo localmente de la siguiente manera (puede variar según tu entorno Colab):

Para utilizarlo:
- Solicitar acceso en: [https://temu.bsc.es/mentalriskes2023/](https://temu.bsc.es/mentalriskes2023/)
- Colocar los archivos en la carpeta `data/Anxiety/` con la siguiente estructura:

```
data/
└── Anxiety/
    ├── data/           # Archivos .json por usuario
    └── gold/
        └── gold_label.csv
```

## Ejemplo de uso en notebook

```python
# Clonar repositorio (una sola vez)
REPO_URL = "https://github.com/manununhez/mentalrisk-nlp-ucom.git"
REPO_NAME = "mentalrisk-nlp-ucom"

import os
if not os.path.exists(REPO_NAME):
    !git clone --depth 1 {REPO_URL}
%cd {REPO_NAME}

from utils.text_cleaning import clean_text
from utils.data_loader import build_df_from_folder

# Cargar los datos desde Drive
json_dir = "/content/drive/MyDrive/data/Anxiety/data"
csv_path = "/content/drive/MyDrive/data/Anxiety/gold/gold_label.csv"
df = build_df_from_folder(json_dir, csv_path)
```

💡 Tip: Asegúrate de mantener la misma estructura de carpetas que las notebooks esperan para evitar errores al ejecutar los experimentos.