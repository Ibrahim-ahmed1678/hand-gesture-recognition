import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Hand Detector
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Function to recognize simple gestures
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4][1]   # y coordinate
    index_tip = landmarks[8][1]
    middle_tip = landmarks[12][1]

    # Example Gestures:
    if index_tip < landmarks[6][1] and middle_tip < landmarks[10][1]:
        return "Fist"
    elif index_tip < thumb_tip:
        return "Pointing Up"
    elif landmarks[8][2] < landmarks[6][2] and landmarks[12][2] < landmarks[10][2]:
        return "Open Palm"
    elif landmarks[12][2] < landmarks[10][2] and landmarks[8][2] > landmarks[6][2] and landmarks[16][2] > landmarks[14][2] and landmarks[20][2] > landmarks[18][2]:
        return "Fuck You"
    else:
        return "Unknown"

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture = "No Hand"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            h, w, _ = frame.shape
            landmarks = []
            for id, lm in enumerate(hand_landmarks.landmark):
                landmarks.append((id, int(lm.x * w), int(lm.y * h)))

            # Gesture Recognition
            gesture = recognize_gesture(landmarks)

            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display Gesture
    cv2.putText(frame, f'Gesture: {gesture}', (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to quit
        break

cap.release()
cv2.destroyAllWindows()