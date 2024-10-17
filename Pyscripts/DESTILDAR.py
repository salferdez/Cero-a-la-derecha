#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:07:02 2024

@author: salferdez
"""

import pandas as pd
import unicodedata

# Función para eliminar tildes
def eliminar_tildes(texto):
    if isinstance(texto, str):
        # Normalizar texto según Unicode
        texto_normalizado = unicodedata.normalize('NFKD', texto)
        texto_sin_tildes = ''.join([c for c in texto_normalizado if not unicodedata.combining(c)])
        return texto_sin_tildes
    else:
        return texto

#Aplicamos la función a los archivos .csv

df1 = pd.read_csv('./Malakathon Cero a la derecha/embalsesUTF8csv')

df1['EMBALSE_NOMBRE'] = df1['EMBALSE_NOMBRE'].apply(eliminar_tildes)

df1.to_csv('embalsesUTF8MODIFICADO.csv', index=False)

df2 = pd.read_csv('./Malakathon Cero a la derecha/listadoUTF8-3csv')

df2['NOMBRE'] = df2['NOMBRE'].apply(eliminar_tildes)

df2.to_csv('listadoUFT8-3MODIFICADO.csv', index=False)

