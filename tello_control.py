# tello_control.py
from djitellopy import Tello
import time
from leap_motion import get_tracking_data  # Importamos la función para obtener los datos de Leap Motion

# Crear instancia del dron Tello y conectar
tello = Tello()
tello.connect()

# Función que controla el dron usando los datos de Leap Motion
def control_drone_with_leap():
    print("Iniciando control del dron con Leap Motion.")
    while True:
        # Obtener los datos de tracking de Leap Motion
        frame_data = get_tracking_data()
        if frame_data:
            palm_position = frame_data["palm_position"]
            print(f"Posición de la palma: x={palm_position['x']}, y={palm_position['y']}, z={palm_position['z']}")

            # Control básico del dron basado en la posición de la palma
            if palm_position["y"] > 15:
                tello.move_up(30)
                print("Subiendo...")
            elif palm_position["y"] < 5:
                tello.move_down(30)
                print("Bajando...")

            # Agregar más movimientos o controles según los datos de tracking aquí

            # Esperar un momento antes de la siguiente lectura para evitar sobrecargar el dron
            time.sleep(2)
        else:
            print("No se recibieron datos de tracking. Verifica la conexión con Leap Motion.")

# Ejecutar la función de control si el script se ejecuta directamente
if __name__ == "__main__":
    try:
        control_drone_with_leap()
    except KeyboardInterrupt:
        print("Interrupción manual detectada. Aterrizando el dron...")
        tello.land()
        print("Dron aterrizado y control detenido.")
