import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf
import os

model = tf.keras.models.load_model('modelo_keras.keras')

class_names = sorted(entry.name for entry in os.scandir('/Users/jesusbarraza/Projects/clasificacion_plantas/split/train') if entry.is_dir())

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se puede abrir la cámara")
    exit()

pred_text = ""  # Variable para almacenar texto de predicción

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el frame")
        break

    # Si tienes predicción previa, la pintas en el frame
    if pred_text:
        cv2.putText(frame, pred_text, (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('p'):
        img = cv2.resize(frame, (128, 128))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        pred = model.predict(img_array)
        pred_class = np.argmax(pred)
        pred_text = f'Prediccion: {class_names[pred_class]}'
        print(pred_text)

    elif key == ord('q'):
        print("Saliendo...")
        break

cap.release()
cv2.destroyAllWindows()
