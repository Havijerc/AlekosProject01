import os
import sys
import inspect

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
