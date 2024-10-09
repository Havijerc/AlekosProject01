from leapc_cffi import libleapc, ffi

def open_connection():
    # Crear el puntero a la conexión
    connection_ptr = ffi.new("LEAP_CONNECTION *")

    # Llamar a LeapCreateConnection
    result = libleapc.LeapCreateConnection(ffi.NULL, connection_ptr)
    if result != 0:
        print("Error al crear la conexión.")
        return None

    print("Conexión creada exitosamente.")

    # Abrimos la conexión
    result = libleapc.LeapOpenConnection(connection_ptr[0])
    if result != 0:
        print("Error al abrir la conexión.")
        return None

    print("Conexión abierta exitosamente.")
    return connection_ptr[0]

def poll_tracking_data(connection_ptr):
    if not connection_ptr:
        print("Puntero de conexión inválido.")
        return

    timeout = 1000  # Tiempo de espera de 1 segundo
    message = ffi.new("LEAP_CONNECTION_MESSAGE *")

    # Llamar a LeapPollConnection para recibir mensajes
    result = libleapc.LeapPollConnection(connection_ptr, timeout, message)

    if result == 0:  # 0 indica éxito
        print(f"Mensaje recibido de tipo: {message.type}")
        if message.type == libleapc.eLeapEventType_Tracking:
            print("Es un mensaje de tipo 'tracking'.")
            tracking_event = ffi.cast("LEAP_TRACKING_EVENT *", message.event)
            print(f"Frame ID: {tracking_event.frame_id}, Timestamp: {tracking_event.timestamp}")
        else:
            print(f"Mensaje recibido de tipo: {message.type} no es de tipo 'tracking'.")
    else:
        print("Error obteniendo los datos de tracking.")

def main():
    connection = open_connection()
    if connection:
        poll_tracking_data(connection)

if __name__ == "__main__":
    main()


def get_tracking_data():
    return None