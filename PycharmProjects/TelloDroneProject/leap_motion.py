import ctypes
import os

# Path to the LeapC.dll
leap_dll_path = 'C:/Users/havij/PycharmProjects/TelloDroneProject/lib/x64/LeapC.dll'
leap_lib = ctypes.CDLL(leap_dll_path)

# Check if LeapC.dll is loaded
if leap_lib:
    print("LeapC.dll loaded successfully.")
else:
    print("Error loading LeapC.dll.")


# Define the necessary tracking structures
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
        ('hands', LEAP_HAND * 2),  # Assuming tracking up to 2 hands
        ('nHands', ctypes.c_uint32)
    ]


# Function to obtain tracking data
def get_tracking_data():
    tracking_event = LEAP_TRACKING_EVENT()
    result = leap_lib.LEAP_PollTracking(ctypes.byref(tracking_event))

    if result == 0:  # 0 indicates success
        print(f"Frame ID: {tracking_event.frame_id}, Timestamp: {tracking_event.timestamp}")
        # Process hand data
        for i in range(tracking_event.nHands):
            hand = tracking_event.hands[i]
            print(
                f"Hand ID: {hand.id}, Palm Position: x={hand.palm_position.x}, y={hand.palm_position.y}, z={hand.palm_position.z}")

            # Simple gesture recognition (palm up)
            if hand.palm_position.y > 200:
                print("Gesture Detected: Move Drone Up")
            elif hand.palm_position.y < 100:
                print("Gesture Detected: Move Drone Down")
    else:
        print("Error getting tracking data")


# Function to simulate a continuous Listener
def run_leap_motion_listener():
    while True:
        get_tracking_data()


if __name__ == "__main__":
    run_leap_motion_listener()
