import cv2
import mediapipe as mp
import numpy as np

print("✅ OpenCV version:", cv2.__version__)
print("✅ Mediapipe version:", mp.__version__)
print("✅ NumPy version:", np.__version__)

# Test camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not detected")
else:
    print("✅ Camera is working")
    cap.release()
