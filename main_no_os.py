### Archivo ZIP usando rutas absolutas ###

# imporatamos el módulo necesario
import zipfile

# definimos el archivo a comprimir
archivo_comprimir = "RUTA DEL ARCHIVO A COMPRIMIR"

# definimos la ubicación y el nombre del archivo .zip
archivo_zip = "RUTA DE SALIDA/NOMBRE.zip"

# comprimimos el archivo
with zipfile.ZipFile(archivo_zip, 'w') as fzip:
    fzip.write(archivo_comprimir)