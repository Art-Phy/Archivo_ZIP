### Archivo_ZIP usando 'os' ###

# importamos los módulos necesarios
import os
import zipfile

# indicamos dónde queremos hacer la compresión
os.chdir("TU RUTA")

# indicamos el archivo que queremso comprimir. La 'w' significa que es sólo de escritura
with zipfile.ZipFile("prueba.zip", "w") as fzip:
    fzip.write("NOMBRE DEL ARCHIVO")

