### Archivo ZIP para comprimir varios archivos al mismo tiempo ###

# importamos el módulo necesario
import zipfile

# definimos los archivos a comprimir y la ubicación y el nombre para la salida de lo comprimido
archivos_comprimir = ["NOMBRE1", "NOMBRE2", "NOMBRE3"]
archivo_zip = "RUTA/NOMBRE.zip" # si no se indica ruta se creará en la carpeta donde estés trabajando

# comprimimos varios archivos
with zipfile.ZipFile(archivo_zip, 'w') as fzip:
    for archivo in archivos_comprimir:
        fzip.write(archivo)