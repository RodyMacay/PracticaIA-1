
"""
Ejercicio 1 (PRE-DATASET)
Contiene tres secciones:
  1) Pandas básico: Sistema Solar
  2) DataFrame de personas y gráficos
  3) Población por país e iteración con iterrows

Requisitos (instalar una vez):
    pip install pandas matplotlib
Ejecución:
    python ejercicio_1_pre_dataset.py
"""

import pandas as pd
import matplotlib.pyplot as plt


def sistema_solar():
    print("\n=== 1) Pandas básico: Sistema Solar ===")
    planeta = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno', 'Plutón']
    lugar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    masa = [0.06, 0.82, 1.00, 0.11, 318, 95.1, 14.6, 17.2, 0.002]

    datos = {'Planeta': planeta, 'Posición': lugar, 'Masa': masa}
    planetas_ss = pd.DataFrame(datos)
    print(planetas_ss)

    print("\n--- Iterando filas ---")
    for etiqueta, fila in planetas_ss.iterrows():
        print(etiqueta)
        print(fila)


def personas_y_graficos():
    print("\n=== 2) DataFrame de personas y gráficos ===")
    nombre = ['Paco', 'Juan', 'Andrés', 'Natalia', 'Vanesa', 'Miriam', 'Juan']
    color = ['rojo', 'verde', 'amarillo', 'verde', 'verde', 'rojo', 'amarillo']
    edad = [24, 30, 41, 22, 31, 35, 22]
    altura = [182, 170, 169, 183, 178, 172, 164]
    peso = [74.8, 70.1, 60.0, 75.0, 83.9, 76.2, 68.0]
    puntuacion = [83, 500, 20, 865, 221, 413, 902]

    datos = {
        'Nombres': nombre,
        'Color': color,
        'Edad': edad,
        'Altura': altura,
        'Peso': peso,
        'Puntuación': puntuacion
    }
    registro = pd.DataFrame(datos)
    print(registro)

    # Gráfico 1: serie de edades
    plt.figure()
    plt.plot(registro['Edad'])
    plt.title('Edad')
    plt.xlabel('Índice')
    plt.ylabel('Edad')
    plt.tight_layout()
    plt.show()

    # Gráfico 2: dispersión Edad vs Peso
    plt.figure()
    plt.scatter(registro['Edad'], registro['Peso'])
    plt.title('Edad vs Peso')
    plt.xlabel('Edad')
    plt.ylabel('Peso')
    plt.tight_layout()
    plt.show()


def poblacion_por_pais():
    print("\n=== 3) Población por país e iteración con iterrows ===")
    paises = ['China', 'India', 'Estados Unidos', 'Indonesia', 'Brasil']
    poblaciones = [1.36, 1.29, 0.33, 0.26, 0.20]

    datos = {'Países': paises, 'Población': poblaciones}
    poblacion = pd.DataFrame(datos)
    poblacion.index = ['CH', 'IN', 'USA', 'ID', 'BR']
    print(poblacion)

    print("\n--- Iterando filas (objeto fila completo) ---")
    for etiqueta, fila in poblacion.iterrows():
        print(etiqueta)
        print(fila)

    print("\n--- Iterando filas (mostrando etiqueta + país) ---")
    for etiqueta, fila in poblacion.iterrows():
        print(etiqueta + ':' + fila['Países'])


if __name__ == "__main__":
    sistema_solar()
    personas_y_graficos()
    poblacion_por_pais()
