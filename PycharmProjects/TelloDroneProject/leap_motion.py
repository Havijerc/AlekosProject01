import sys
import os
import ctypes
from Leap import Controller, Listener  # Importamos las clases necesarias

# Aseguramos que la ruta de los bindings esté incluida
sys.path.append('C:/Users/havij/PycharmProjects/TelloDroneProject/leapc-python-bindings-main/leapc-python-api')

# Ruta al archivo LeapC.dll
leap_dll_path = 'C:/Users/havij/PycharmProjects/TelloDroneProject/lib/x64/LeapC.dll'
leap_lib = ctypes.CDLL(leap_dll_path)

# Comprobamos si LeapC.dll está cargado
if leap_lib:
    print("LeapC.dll loaded successfully.")
else:
    print("Error loading LeapC.dll.")


# Definición de las estructuras necesarias para el tracking
class LEAP_VECTOR(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float), ("z", ctypes.c_float)]


class LEAP_HAND(ctypes.Structure):
    _fields_ = [
        ('id', ctypes.c_int32),
        ('palm_position', LEAP_VECTOR)
    ]


class LEAP_TRACKING_EVENT(ctypes.Structure):
    _fields_ = [
        ('frame_id', ctypes.c_longlong),
        ('timestamp', ctypes.c_longlong),
        ('hands', LEAP_HAND * 2),  # Asumiendo tracking para hasta 2 manos
        ('nHands', ctypes.c_uint32)
    ]


# Definir una clase Listener que hereda de Leap.Listener
class SampleListener(Listener):
    def on_connect(self, controller):
        print("Connected to Leap Motion")
        controller.enable_gesture(Controller.Gesture.TYPE_SWIPE)

    def on_frame(self, controller):
        frame = controller.frame()
        hands = frame.hands
        for hand in hands:
            print(
                f"Hand ID: {hand.id}, Palm Position: x={hand.palm_position.x}, y={hand.palm_position.y}, z={hand.palm_position.z}")


# Función principal para iniciar el listener
def main():
    listener = SampleListener()
    controller = Controller()
    controller.add_listener(listener)

    try:
        input("Press Enter to quit...\n")
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
