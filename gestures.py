import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Constants
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
DEBOUNCE_DELAY = 0.5  # Debounce delay in seconds
VOLUME_LOWER_THRESHOLD = 30  # Lower threshold for volume adjustment
VOLUME_UPPER_THRESHOLD = 70  # Upper threshold for volume adjustment

# Initialize variables
hand_present = False
thumb_id = 4  # Index of the thumb landmark
index_id = 8  # Index of the index finger landmark
last_toggle_time = time.time()
volume_adjusted = False

# Function to control volume based on hand gesture
def control_volume(thumb_tip, index_tip):
    global last_toggle_time, volume_adjusted

    # Calculate distance between thumb and index finger
    thumb_index_dist = np.linalg.norm(np.subtract(thumb_tip, index_tip))

    # Get hand size based on the maximum dimension of the frame
    hand_size = max(FRAME_WIDTH, FRAME_HEIGHT)

    # Adjust the volume control range based on hand size
    volume_distance_max = hand_size * 0.3
    volume_distance_min = hand_size * 0.05

    # Map the distance to volume control
    volume = np.interp(thumb_index_dist, [volume_distance_min, volume_distance_max], [0, 100])
    volume = int(max(0, min(100, volume)))  # Ensure volume is within the valid range

    # Check debounce delay
    current_time = time.time()
    if current_time - last_toggle_time >= DEBOUNCE_DELAY:
        if volume_adjusted and (volume <= VOLUME_LOWER_THRESHOLD or volume >= VOLUME_UPPER_THRESHOLD):
            volume_adjusted = False

        if not volume_adjusted:
            if volume <= VOLUME_LOWER_THRESHOLD:
                pyautogui.press('volumemute')  # Mute volume
            else:
                pyautogui.press('volumeup', presses=volume)  # Set volume

            volume_adjusted = True
            last_toggle_time = current_time

# Start capturing video
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

while True:
    # Read the current frame
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert frame to RGB for MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand landmarks using MediaPipe
    results = mp_hands.process(rgb)
    if results.multi_hand_landmarks:
        hand_present = True

        # Extract hand landmarks
        hand_landmarks = results.multi_hand_landmarks[0].landmark

        # Get thumb and index finger tip coordinates
        thumb_tip = (int(hand_landmarks[thumb_id].x * FRAME_WIDTH), int(hand_landmarks[thumb_id].y * FRAME_HEIGHT))
        index_tip = (int(hand_landmarks[index_id].x * FRAME_WIDTH), int(hand_landmarks[index_id].y * FRAME_HEIGHT))

        # Control volume based on hand gesture
        control_volume(thumb_tip, index_tip)

        # Draw line between thumb and index finger
        cv2.line(frame, thumb_tip, index_tip, (0, 0, 255), 3)
        # Draw circles at the thumb and index finger tips
        cv2.circle(frame, thumb_tip, 10, (0, 255, 0), -1)
        cv2.circle(frame, index_tip, 10, (0, 0, 255), -1)
    else:
        hand_present = False
        volume_adjusted = False

    # Display the frame
    cv2.imshow("Hand Gesture Volume Control", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
