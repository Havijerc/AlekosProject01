from djitellopy import Tello
import time
from leap_motion import get_tracking_data

# Crear instancia del dron Tello
tello = Tello()
tello.connect()

# Función que controla el dron basándose en los datos de Leap Motion
def control_drone_with_leap():
    frame_data = get_tracking_data()
    if frame_data:  # Si obtenemos un frame
        # Mover el dron según la información recibida
        tello.move_up(30)
        time.sleep(2)
        tello.move_down(30)

if __name__ == "__main__":
    control_drone_with_leap()
