"""
=============================
     ARCHIVO ZIP (v2)
=============================

Autor: Art-Phy
Descripción:
  Programa que permite comprimir uno o varios archivos arrastrándolos 
  directamente a la terminal. Crea un archivo ZIP en la ruta que el usuario 
  indique y, al finalizar, ofrece la opción de volver a comprimir o salir.

Mejoras respecto a la versión anterior:
- Permite arrastrar varios archivos directamente a la terminal.
- Bucle interactivo para repetir o salir sin cerrar el programa.
- Limpieza automática de pantalla entre ejecuciones.
- Validación de rutas y manejo de errores.
- Código modularizado con funciones descriptivas.
- Preparado para futuras ampliaciones (colores, GUI, logs...).
"""


import os
import zipfile
import shlex


def limpiar_rutas_entrada(entrada_usuario):
    rutas = shlex.split(entrada_usuario)
    rutas_limpias = [os.path.abspath(ruta) for ruta in rutas]
    return rutas_limpias


def comprimir_archivos(rutas_archivos, ruta_salida):
    # Comprime uno o varios archivos en un archivo ZIP.
    if not rutas_archivos:
        print("⚠️ No se han proporcionado archivos para comprimir.\n")
        return False

    try:
        with zipfile.ZipFile(ruta_salida, "w", compression=zipfile.ZIP_DEFLATED) as fzip:
            alguno_comprimido = False
            for archivo in rutas_archivos:
                if os.path.isfile(archivo):
                    fzip.write(archivo, os.path.basename(archivo))
                    print(f"✅ Añadido: {archivo}")
                    alguno_comprimido = True
                else:
                    print(f"❌ No se encontró el archivo: {archivo}")

        if alguno_comprimido:
            print(f"\n🎉 Compresión completada correctamente.")
            print(f"📦 Archivo ZIP creado en: {ruta_salida}\n")
            return True
        else:
            print("\n⚠️ Ningún archivo válido fue comprimido.\n")
            return False

    except Exception as e:
        print(f"❌ Error durante la compresión: {e}\n")
        return False


def solicitar_datos_usuario():
    print("=== COMPRESOR DE ARCHIVOS ZIP ===\n")
    print("👉 Arrastra uno o varios archivos a esta ventana y presiona Enter:\n")

    entrada = input("Archivos: ").strip()
    rutas_archivos = limpiar_rutas_entrada(entrada)

    print("\n📦 Introduce la ruta y nombre del ZIP de salida")
    print("(por ejemplo: /Users/tuusuario/Desktop/resultado.zip)\n")
    ruta_zip = input("Archivo ZIP: ").strip()

    if not os.path.isabs(ruta_zip):
        ruta_zip = os.path.join(os.getcwd(), ruta_zip)

    return rutas_archivos, ruta_zip


def main():
    while True:
        rutas_archivos, ruta_zip = solicitar_datos_usuario()
        exito = comprimir_archivos(rutas_archivos, ruta_zip)

        # Preguntamos al usuario si desea continuar o salir
        while True:
            opcion = input("¿Quieres comprimir más archivos? (s/n): ").strip().lower()
            if opcion == "s":
                os.system("clear")  # limpia pantalla (Mac/Linux)
                break
            elif opcion == "n":
                print("\n👋 Saliendo del programa. ¡Nos vemos!\n")
                return
            else:
                print("❌ Venga que no es tan difícil. Escribe 's' para sí o 'n' para no.")


if __name__ == "__main__":
    main()


