from leapc_cffi import libleapc, ffi  # Importamos correctamente 'libleapc'

# Verifica que LeapC esté cargado
if libleapc:
    print("LeapC loaded successfully.")
else:
    print("Error loading LeapC.")


# Función para obtener los datos de tracking
def poll_tracking_data():
    # Crear el puntero a la conexión
    connection_ptr = ffi.new("LEAP_CONNECTION *")

    # Llamar a LeapCreateConnection con NULL y el puntero a la conexión
    result = libleapc.LeapCreateConnection(ffi.NULL, connection_ptr)

    if result == 0:
        print("Connection created successfully.")
    else:
        print("Error creating connection.")
        return

    # Proporcionar el tiempo de espera (en milisegundos)
    timeout = 1000  # 1 segundo

    # Crear un objeto para almacenar mensajes del servidor (conexión)
    message = ffi.new("LEAP_CONNECTION_MESSAGE *")

    # Llamar a LeapPollConnection para obtener datos de seguimiento
    result = libleapc.LeapPollConnection(connection_ptr[0], timeout, message)

    if result == 0:  # 0 indica éxito
        print(f"Received a message of type: {message.type}")
        if message.type == libleapc.eLeapEventType_Tracking:
            tracking_event = ffi.cast("LEAP_TRACKING_EVENT *", message.tracking_event)
            print(f"Frame ID: {tracking_event.frame_id}, Timestamp: {tracking_event.timestamp}")
            # Procesar los datos de las manos
            for i in range(tracking_event.nHands):
                hand = tracking_event.hands[i]
                print(
                    f"Hand ID: {hand.id}, Palm Position: x={hand.palm_position.x}, y={hand.palm_position.y}, z={hand.palm_position.z}")
    else:
        print("Error obteniendo los datos de tracking.")


# Función principal
def main():
    poll_tracking_data()


if __name__ == "__main__":
    main()
