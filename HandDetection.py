import cv2
import mediapipe as mp
import serial
import time

# Setup Serial to ESP32
esp32 = serial.Serial('COM3', 115200)  # IMPORTANT: Change 'COM3' if needed
time.sleep(2)  # Give ESP32 time to reset

# Setup MediaPipe for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Setup Webcam
cap = cv2.VideoCapture(0)

# Function to count fingers
def count_fingers(hand_landmarks):
    fingers = []

    # Thumb
    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
        fingers.append(1)
    else:

        
        fingers.append(0)

    # Other 4 fingers
    for tip_id in [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                   mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                   mp_hands.HandLandmark.RING_FINGER_TIP,
                   mp_hands.HandLandmark.PINKY_TIP]:

        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    finger_count = 0  # Default finger count

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_count = count_fingers(hand_landmarks)

            if finger_count == 1:
                esp32.write(b'1\n')
            elif finger_count == 2:
                esp32.write(b'2\n')
            else:
                esp32.write(b'0\n')
    else:
        esp32.write(b'0\n')

    # === NEW: Show Finger Count on Image ===
    cv2.putText(img, f'Fingers: {finger_count}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("ESP32 Hand Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
esp32.close()
cv2.destroyAllWindows()
