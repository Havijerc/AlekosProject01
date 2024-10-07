import ctypes
import os

# Ruta a LeapC.dll (ajusta esta ruta según donde esté LeapC.dll)
leap_dll_path = 'C:/Users/havij/PycharmProjects/TelloDroneProject/lib/x64/LeapC.dll'
leap_lib = ctypes.CDLL(leap_dll_path)

# Verificar si la librería se cargó correctamente
if leap_lib:
    print("LeapC.dll cargado correctamente.")
else:
    print("Error cargando LeapC.dll.")

# Definir algunas funciones de LeapC usando ctypes
class LEAP_TRACKING_EVENT(ctypes.Structure):
    _fields_ = [
        ('frame_id', ctypes.c_longlong),
        ('timestamp', ctypes.c_longlong),
        # Puedes agregar más campos según lo que necesites
    ]

# Llamar una función de LeapC para obtener el estado de las manos
leap_lib.LEAP_GetNow.restype = ctypes.c_longlong

time_now = leap_lib.LEAP_GetNow()
print(f"Tiempo actual según Leap: {time_now} nanosegundos")

# Función para obtener datos de tracking
def get_tracking_data():
    tracking_event = LEAP_TRACKING_EVENT()
    result = leap_lib.LEAP_PollTracking(ctypes.byref(tracking_event))
    if result == 0:
        print(f"ID del frame: {tracking_event.frame_id}, Timestamp: {tracking_event.timestamp}")
    else:
        print("Error obteniendo datos de tracking")

# Llamada para obtener los datos de tracking
get_tracking_data()
