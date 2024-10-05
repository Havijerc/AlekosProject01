# Alekos Project - Leap Motion Control for DJI Tello Drone

## Project Overview

The Alekos Project focuses on integrating Leap Motion hand-tracking technology with the DJI Tello drone. The purpose of this project is to allow users to control the drone using simple hand gestures detected by the Leap Motion sensor, making it an intuitive and engaging experience.

## Repository Structure
Here’s an overview of the key files and directories in the repository:

leap_motion.py: This is the main Python script that captures hand-tracking data from the Leap Motion sensor and sends the corresponding commands to the Tello drone.
tello_control.py: This file manages communication with the Tello drone using its SDK.
lib/: Contains the Leap Motion SDK files, including the necessary LeapC.dll file.
x64/LeapC.dll: This is the dynamic link library that enables Python to communicate with the Leap Motion hardware.
README.md: Provides the instructions and details about the project.
requirements.txt: Lists the required Python packages to run the project.
LICENSE: The project is licensed under the MIT License.

## Features
Hand Gesture Recognition: The project detects hand movements like moving the palm up or down to control the altitude of the Tello drone.
Real-time Drone Control: It utilizes real-time data from the Leap Motion sensor to operate the drone.

## Setup Instructions
### 1. Clone the Repository
Clone this project to your local machine using the following command:


[git clone] (https://github.com/yourusername/AlekosProject.git)

### 2. Install Dependencies
After cloning, you need to install the required Python libraries using the requirements.txt file:
pip install -r requirements.txt

### 3. Leap Motion SDK Setup
Download and install the Ultraleap Gemini Hand Tracking Software (required for Leap Motion).
Copy the LeapC.dll and LeapC.lib files from the Ultraleap SDK and place them in the lib/x64/ directory.

### 4. Connecting the Drone and Leap Motion
Connect your Leap Motion sensor and run the Ultraleap Gemini tracking software.
Connect the DJI Tello Drone to your Wi-Fi network.

### 5. Running the Project
To start using Leap Motion to control the drone, run the following command:
python leap_motion.py

### 6. Testing and Gesture Recognition
Raise your hand to move the drone up.
Lower your hand to move the drone down.
The script will display the position of the palm in real-time for each frame.

## Troubleshooting

LeapC.dll not found: Ensure that the LeapC.dll is in the correct directory and that the path is correct in the Python script.
Drone not responding: Ensure the Tello drone is connected to the network and the Tello SDK is properly configured.
Gesture detection issues: Make sure the Leap Motion sensor is correctly positioned and can detect your hand movements clearly.
Future Work

### This project is still in development, and future updates may include:

Enhanced gesture control for more complex drone movements.
Improved hand-tracking accuracy and more gesture options.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.
