# Alekos Project - Leap Motion Control for DJI Tello Drone

## Project Overview

The **Alekos Project** aims to integrate Leap Motion (Ultraleap) hand-tracking technology with a DJI Tello drone. The project enables users to control the drone using simple hand gestures detected by the Leap Motion sensor.

### Features
- **Hand Gesture Recognition**: Control the drone by raising or lowering your hand.
- **Real-time Drone Control**: Real-time hand tracking for drone movement.

## Requirements

Make sure you have the following:

- **Python 3.8 or higher**
- **Ultraleap Gemini Hand Tracking Software** (for Leap Motion)
- **DJI Tello Drone** and Tello SDK
- Required Python libraries (installed via requirements.txt):
  - `ctypes`
  - **Leap Motion SDK** (LeapC.dll and LeapC.lib)

## Setup Instructions

### 1. Clone the Repository
Clone the project to your local machine using Git:
```bash

2. Install Python Dependencies

pip install -r requirements.txt

3. Leap Motion SDK Setup

Download and install Ultraleap Gemini Hand Tracking Software.
Copy the LeapC.dll and LeapC.lib files from the SDK to the lib/x64/ directory.

4. Running the Project

Connect your Leap Motion sensor and start the Gemini tracking software.
Connect the DJI Tello drone.
Run the following command to start gesture-based control of the drone:


python leap_motion.py


5. Troubleshooting
LeapC.dll not loading: Ensure that the SDK files are in the correct directory.
Gesture detection issues: Make sure the Leap Motion sensor is positioned correctly and can see your hands.
