# Alekos Project - Leap Motion Control for DJI Tello Drone

## Project Description

The **Alekos Project** is an innovative project that integrates Leap Motion (Ultraleap) hand-tracking technology with the DJI Tello drone. 
This project allows users to control the drone using hand gestures captured by the Leap Motion sensor.

The project is built using Python and uses the `ctypes` library to interact with the LeapC SDK, which handles the tracking data for hand positions. 
The hand gestures are then translated into commands for controlling the movement of the DJI Tello drone.

## Features

- Real-time hand gesture recognition
- Control of DJI Tello drone using Leap Motion gestures
- Drone commands: move up, down based on hand position

## Requirements

- **Python 3.8** (or higher)
- **Ultraleap Gemini SDK** (Leap Motion)
- **DJI Tello Drone**
- **ctypes** (Python library to interface with C functions)
