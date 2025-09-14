# Hand Gesture Recognition

This project implements a hand gesture recognition system using OpenCV and Mediapipe. It captures video from the webcam, detects hand landmarks, recognizes simple gestures, and displays the recognized gesture in real-time.

## Features

- Real-time hand gesture recognition
- Simple gesture detection (Fist, Pointing Up, Open Palm)
- Visual feedback with drawn landmarks and recognized gestures

## Installation

To run this project, you need to have Python installed on your machine. You can install the required dependencies using pip. 

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/hand-gesture-recognition.git
   cd hand-gesture-recognition
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the hand gesture recognition script:
   ```
   python src/hand_gesture_recognition.py
   ```

2. Allow access to your webcam when prompted.

3. Perform gestures in front of the camera to see the recognized gestures displayed on the screen.

## Dependencies

- opencv-python
- mediapipe

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.