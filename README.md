# Detección de Riesgo Emocional en Telegram usando NLP

Este repositorio contiene el trabajo realizado como parte del proyecto académico de la Maestría en Ciencia de Datos, cuyo objetivo fue comparar diferentes enfoques de procesamiento de lenguaje natural (PLN) para identificar señales de ansiedad en textos en español.

## 📁 Estructura

- `notebooks/`: contiene los tres enfoques implementados:
  - `01_svm_tf-idf.ipynb`
  - `02_fasttext.ipynb`
  - `03_roberta_fine_tuning.ipynb`

- `paper/`: versión PDF del artículo técnico desarrollado.

- `requirements.txt`: dependencias necesarias para reproducir los notebooks.

- `data/`: instrucciones para acceder al dataset MentalRiskES 2023 (no incluido por restricciones de licencia).

## 📊 Modelos Evaluados

1. **SVM + TF-IDF**
2. **FastText + TF-IDF**
3. **RoBERTa-base-bne** (fine-tuning con PyTorch)

## 🧪 Dataset

Se utilizó el corpus **MentalRiskES 2023**, el cual contiene mensajes de usuarios de Telegram etiquetados según la presencia de trastornos mentales. Debido a su acceso restringido, debes solicitarlo desde la [página oficial del desafío](https://sites.google.com/view/mentalriskes/home).

Consulta el archivo [`data/README.md`](data/README.md) para instrucciones detalladas.

## ▶️ Cómo ejecutar

Podés abrir los notebooks directamente desde Google Colab haciendo clic en estos enlaces:

- [SVM](https://colab.research.google.com/github/tu_usuario/mental-risk-nlp/blob/main/notebooks/01_svm_tf-idf.ipynb)
- [FastText](https://colab.research.google.com/github/tu_usuario/mental-risk-nlp/blob/main/notebooks/02_fasttext.ipynb)
- [RoBERTa](https://colab.research.google.com/github/tu_usuario/mental-risk-nlp/blob/main/notebooks/03_roberta_fine_tuning.ipynb)

> **Nota:** Antes de ejecutar, asegúrate de haber montado el dataset en la ruta esperada (ver cada notebook).

## 📄 Artículo

El documento completo con la metodología, resultados y análisis está disponible en `paper/ucom_pln_mental_health_risk_2023.pdf`.

---

## 💡 Créditos

- Daniel Centurión  
- Manuel Núñez  
- Gustavo Báez  

Maestría en Ciencia de Datos, Universidad Comunera, 2025.