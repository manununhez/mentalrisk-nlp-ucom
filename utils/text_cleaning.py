"""
text_cleaning.py

Módulo de funciones para la limpieza de texto en contextos de análisis de lenguaje natural (NLP).
"""

import re
import html
import unicodedata

# Expresiones regulares para identificar patrones comunes
URL      = re.compile(r"https?://\S+|www\.\S+")
MENTION  = re.compile(r"@\w+")
NUMBER   = re.compile(r"\b\d[\d,.]*\b")
WHITES   = re.compile(r"\s+")

def clean_text(text: str) -> str:
    """
    Limpia un texto conservando ciertos símbolos importantes y reduciendo el ruido.
    
    Procesos aplicados:
    - Decodifica entidades HTML
    - Reemplaza URLs, menciones y números por tokens especiales
    - Convierte a minúsculas
    - Normaliza tildes y caracteres Unicode
    - Elimina caracteres no alfabéticos excepto puntuaciones importantes y tokens
    - Reduce espacios múltiples a uno solo

    Parámetros:
    text (str): Texto original.

    Retorna:
    str: Texto limpio, listo para análisis o entrenamiento de modelos NLP.
    """
    text = html.unescape(text)
    text = URL.sub(" URL ", text)
    text = MENTION.sub(" MENTION ", text)
    text = NUMBER.sub(" NUM ", text)
    text = text.lower()
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[^a-záéíóúüñàèìòùü¿¡:_\s]", " ", text)
    text = WHITES.sub(" ", text).strip()
    return text
