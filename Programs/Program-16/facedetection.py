import cv2
import matplotlib.pyplot as plt

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

# Check camera
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Prepare matplotlib plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

img_plot = None

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        # Draw rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Convert to RGB for matplotlib
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # First time: show the image
        if img_plot is None:
            img_plot = ax.imshow(rgb)
            plt.title("Live Face Detection")
            plt.axis("off")
        else:
            img_plot.set_data(rgb)  # Update image data

        plt.pause(0.001)

except KeyboardInterrupt:
    print("Stopped by user")

cap.release()
plt.ioff()
plt.close()
