import ctypes



# Cargar la biblioteca LeapC.dll
leap_dll_path = 'C:/Users/havij/PycharmProjects/TelloDroneProject/lib/x64/LeapC.dll'
leap_lib = ctypes.CDLL(leap_dll_path)

# Listar todas las funciones en LeapC.dll
for func_name in dir(leap_lib):
    if not func_name.startswith('_'):
        print(func_name)

# Define la ruta al archivo LeapC.dll
leap_dll_path = 'ruta/a/tu/LeapC.dll'

# Cargar la librería LeapC.dll
leap_lib = ctypes.CDLL(leap_dll_path)

# Define funciones según la API de LeapC
leap_lib.LEAP_Initialize.restype = ctypes.c_int

def initialize_leap():
    result = leap_lib.LEAP_Initialize()
    if result == 0:
        print("Leap Motion inicializado correctamente.")
    else:
        print(f"Error al inicializar Leap Motion: {result}")



