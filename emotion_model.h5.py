import tensorflow as tf
from tensorflow.keras import layers, models

# Define your deep learning model (e.g., a CNN)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(7, activation='softmax')  # 7 emotions (happy, sad, angry, etc.)
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model on your preprocessed dataset
model.fit(train_images, train_labels, epochs=10, batch_size=32)

import cv2

# Load the pre-trained model
model = tf.keras.models.load_model('emotion_model.h5')

# Initialize the webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Preprocess the frame (resize, convert to grayscale, normalize)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, (48, 48))
    normalized_frame = resized_frame / 255.0
    input_frame = normalized_frame.reshape(1, 48, 48, 1)

    # Make predictions using the model
    prediction = model.predict(input_frame)
    emotion_label = emotion_labels[prediction.argmax()]  # Map predictions to emotion labels

    # Display the emotion label on the frame
    cv2.putText(frame, emotion_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with emotion label
    cv2.imshow('Emotion Detection', frame)

    # Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
