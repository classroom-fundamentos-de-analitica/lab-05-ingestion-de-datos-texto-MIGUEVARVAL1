import pandas as pd
import os
import re
import zipfile

archivo = zipfile.ZipFile('data.zip','r')
archivo.extractall()

def procesar_carpeta(carpeta):
    datos = []
    for raiz, directorios, archivos in os.walk(carpeta):
        for archivo in archivos:
            if archivo.endswith('.txt'):
                ruta_archivo = os.path.join(raiz, archivo)
                etiqueta = os.path.basename(os.path.dirname(ruta_archivo))
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_txt:
                    texto = archivo_txt.read().strip()
                    datos.append((texto, etiqueta))
    return datos





datos_train = procesar_carpeta('train')
datos_test = procesar_carpeta('test')

df_train = pd.DataFrame(datos_train, columns=['phrase', 'sentiment'])
df_test = pd.DataFrame(datos_test, columns=['phrase', 'sentiment'])


df_train.to_csv('train_dataset.csv', index=False)
df_test.to_csv('test_dataset.csv', index=False)
