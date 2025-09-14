# ejercicio_2_dataset1_iris.py
# -*- coding: utf-8 -*-
"""
Ejercicio 2 (DESDE DATASET1 — Iris)
Cargar y analizar el dataset 'dataset1.csv' (formato Iris) desde tu máquina local.
Se generan histogramas y un scatter, además de etiquetar filas por tamaño usando PetalLengthCm.

Requisitos (instalar una vez):
    pip install pandas matplotlib

Antes de ejecutar:
    - Coloca el archivo 'dataset1.csv' en la MISMA carpeta de este script.
    - Asegúrate que las columnas se llamen al menos:
        ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
    - Si tu CSV tiene un índice en la primera columna, ajusta index_col según corresponda.

Ejecución:
    python ejercicio_2_dataset1_iris.py
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


def cargar_iris_csv(ruta_csv: str) -> pd.DataFrame:
    """Carga el CSV de Iris. Ajusta index_col si tu archivo no trae índice explícito."""
    if not os.path.exists(ruta_csv):
        print(f"ERROR: No se encontró el archivo: {ruta_csv}")
        sys.exit(1)
    try:
        # Si tu CSV NO tiene índice en la primera columna, cambia index_col=None
        df = pd.read_csv(ruta_csv, index_col=0)
    except Exception:
        # Fallback sin índice si falla lo anterior
        df = pd.read_csv(ruta_csv)
    return df


def analizar_iris(df: pd.DataFrame) -> None:
    print("\n=== Vista general del dataset ===")
    print(df.head())
    print("\n=== Columnas ===")
    print(list(df.columns))

    # Histograma de las dos primeras columnas numéricas (usando nombres estándar si existen)
    col0 = df.columns[0]
    col1 = df.columns[1]

    plt.figure()
    plt.hist(df[col0].dropna())
    plt.title(f'Distribución de {col0}')
    plt.xlabel(col0)
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.hist(df[col1].dropna())
    plt.title(f'Distribución de {col1}')
    plt.xlabel(col1)
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()

    # Scatter PetalLength vs PetalWidth si existen las columnas esperadas
    if {'PetalLengthCm', 'PetalWidthCm'}.issubset(df.columns):
        plt.figure()
        plt.scatter(df['PetalLengthCm'], df['PetalWidthCm'])
        plt.title('Dimensiones de los pétalos')
        plt.xlabel('PetalLengthCm')
        plt.ylabel('PetalWidthCm')
        plt.tight_layout()
        plt.show()

        # Etiquetado por tamaño según umbral de PetalLengthCm
        umbral = 2.5
        df = df.copy()
        df.loc[df['PetalLengthCm'] >= umbral, 'Tamaño'] = 'Grande'
        df.loc[df['PetalLengthCm'] >= umbral, 'Color'] = 'r'
        df.loc[df['PetalLengthCm'] < umbral, 'Tamaño'] = 'Pequeño'
        df.loc[df['PetalLengthCm'] < umbral, 'Color'] = 'b'

        print("\n=== Muestra con etiquetas de tamaño y color ===")
        cols_show = ['PetalLengthCm', 'PetalWidthCm', 'Tamaño', 'Color']
        print(df[cols_show].head())

        # Scatter coloreado por etiqueta calculada
        plt.figure()
        plt.scatter(df['PetalLengthCm'], df['PetalWidthCm'], c=df['Color'])
        plt.title('Dimensiones de pétalos (color por tamaño)')
        plt.xlabel('PetalLengthCm')
        plt.ylabel('PetalWidthCm')
        plt.tight_layout()
        plt.show()
    else:
        print("\nAviso: No se encontraron las columnas 'PetalLengthCm' y 'PetalWidthCm' en el CSV.")


if __name__ == "__main__":
    ruta = "dataset1.csv"  # Cambia si tu archivo tiene otro nombre o ruta
    iris = cargar_iris_csv(ruta)
    analizar_iris(iris)
