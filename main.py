import os
import sys
import inspect
import ctypes

# Ruta a LeapC.dll - Ajusta según la ubicación de tu archivo LeapC.dll
leap_dll_path = "C:/Users/havij/PycharmProjects/TelloDroneProject/lib/x64/LeapC.dll"
leap_lib = ctypes.CDLL(leap_dll_path)

# Verificar que la biblioteca LeapC.dll se haya cargado correctamente
if leap_lib:
    print("LeapC.dll cargado correctamente.")
else:
    print("Error cargando LeapC.dll.")
    sys.exit(1)

# Configuración para importar la biblioteca Leap Motion
# Obtiene la ruta actual del script
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))  # Ruta del script actual
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'  # Verifica si es 64 o 32 bits y configura la ruta

# Añadir la ruta del SDK de Leap Motion al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

# Intentar importar Leap Motion
try:
    import Leap
except ImportError as e:
    print("Error importando Leap: ", e)
    Leap = None  # Define Leap como None en caso de error

# Aquí se pueden añadir más configuraciones o inicializaciones si es necesario

def main():
    # Aquí iría la lógica principal de tu programa, por ejemplo, abrir conexiones, etc.
    # Esto se deja vacío para que lo personalices con la lógica que necesitas
    pass

if __name__ == "__main__":
    main()
