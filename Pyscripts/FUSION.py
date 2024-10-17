import pandas as pd

# Leer los archivos CSV en DataFrames
df1 = pd.read_csv('./Malakathon Cero a la derecha/embalsesUTF8MODIFICADO.csv')
df2 = pd.read_csv('./Malakathon Cero a la derecha/listadoUFT8-3MODIFICADO.csv')

#Fusionamos filas según si los valores de EMBALSE_NOMBRE y NOMBRE coinciden, una vez formateados ambos.
df_merged = pd.merge(df1, df2, how='outer', left_on='EMBALSE_NOMBRE', right_on='NOMBRE')

# Guardar el resultado en un nuevo archivo CSV
df_merged.to_csv('FUSION.csv', index=False)

print("Fusión completada. El archivo resultante se ha guardado como 'archivo_fusionado.csv'.")
