# 🌿 Modelo de Clasificación de Plantas 🌿
Trabajo realizado por:
- Jesús Alberto Barraza Castro
- Jesús Guadalupe Wong Camacho
***

## 📋 Descripción de la tarea

El objetivo de este proyecto fue entrenar un modelo para clasificar imágenes de diferentes especies de plantas. La tarea incluyó:

📊 **Fuente de los dato**
Las imagenes utilizadas para entrenar y evaluar el modelo fueron obtenidas del dataset "House Plant Species" disponible en kaggle
[Clic aqui para ir al dataset](https://www.kaggle.com/datasets/kacpergregorowicz/house-plant-species/data)
![Image](https://github.com/user-attachments/assets/370d1cb6-98c6-487b-acdf-f99e8a29e911)

🧠 **Arquitectura de la red neuronal utilizada**  
Se utilizo una red neuronal con capas convolucionales, capas de pooling, capas densas y funciones de activación adecuadas para el problema de clasificación.
[Documentacion detallada](https://github.com/jesusBarrazaCastro/itc_topicos_ia/blob/main/UNIDAD%204/TAREA%202/documentacion_clasificacion_plantas.pdf)

---

## 📁 Archivos del proyecto

### 1. 📓 Notebook completo (`clasificacion_plantas.ipynb`)

Contiene todo el desarrollo del proyecto, desde la carga y preprocesamiento de datos, definición y explicación detallada de la arquitectura de la red neuronal, entrenamiento del modelo, evaluación con métricas, hasta la exportación y guardado del modelo entrenado.

### 2. 🧩 Modelo guardado (`modelo_keras.keras`)

Archivo que contiene el modelo entrenado guardado en formato Keras. Este archivo permite cargar el modelo sin necesidad de entrenarlo nuevamente, facilitando su uso para predicciones en tiempo real o integración en aplicaciones.

### 3. 📷 Script para webcam (`pruebas_webcam.py`)

Script en Python que abre la cámara web del equipo, captura imágenes en tiempo real y permite, al presionar la tecla 'p', realizar una predicción de la clase de planta usando el modelo guardado. También permite cerrar la aplicación presionando 'q'. La predicción se muestra sobre la imagen en la ventana de la cámara para facilitar la interacción.

---

## 📹 Video de pruebas con webcam
![Image](https://github.com/user-attachments/assets/a76faf95-0562-4516-8702-e273fbd5d285)
En este video se realizaron pruebas utilizando la camara web para clasificar plantas
[Clic aqui para ir al video](https://youtu.be/IKAmNQ2jGpc)
