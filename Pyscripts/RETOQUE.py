#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:27:47 2024

@author: salferdez
"""

import pandas as pd

# Leer el archivo CSV de origen
file_path = '../../Malakathon Cero a la derecha/FUSION.csv'  # Cambia esto por el nombre de tu archivo

df = pd.read_csv(file_path)

"""

Una vez fusionadas las tablas, sustituimos los valores Nan de AMBITO_NOMBRE con los de DEMARC y eliminamos dicha
columna para evitar redundancias.

Hacemos lo mismo con EMBALSE_NOMBRE y NOMBRE

"""

"""df['AMBITO_NOMBRE'].fillna(df['DEMARC'], inplace=True)

df.drop(columns=['DEMARC'], inplace=True)

df['EMBALSE_NOMBRE'].fillna(df['NOMBRE, inplace=True)

df.drop(columns=['NOMBRE'], inplace=True)"""

df['ID'].fillna(df['CODIGO'], inplace=True)

# Sobrescribir el archivo CSV original con el DataFrame modificado
df.to_csv(file_path, index=False)

print(f"Archivo actualizado y guardado en {file_path}")
