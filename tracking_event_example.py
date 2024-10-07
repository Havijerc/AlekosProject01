import Leap
import sys

class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print("Connected to Leap Motion")
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def on_tracking_event(self, controller):
        frame = controller.frame()
        hands = frame.hands
        for hand in hands:
            print(f"Hand ID: {hand.id}, Palm Position: {hand.palm_position}")

def main():
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    try:
        sys.stdin.read()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
