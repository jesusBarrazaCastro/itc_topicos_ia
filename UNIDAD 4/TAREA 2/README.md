# 🌿 Proyecto de Clasificación de Plantas 🌿

## 📋 Descripción de la tarea

El objetivo de este proyecto fue entrenar un modelo de aprendizaje automático para clasificar imágenes de diferentes especies de plantas. La tarea incluyó:

1. 📂 Preparar y cargar los datos de entrenamiento desde un directorio con imágenes organizadas por clases.

2. 🧠 **Definir la arquitectura de la red neuronal a utilizar y explicar detalladamente su estructura y funcionamiento.**  
   Esta parte fue fundamental para asegurar que el modelo pudiera aprender a reconocer las características relevantes de las plantas. Se diseñó una red neuronal con capas convolucionales, capas de pooling, capas densas y funciones de activación adecuadas para el problema de clasificación.

3. ⚙️ Entrenar un modelo de red neuronal usando TensorFlow/Keras.

4. 📊 Evaluar el desempeño del modelo con varias métricas de precisión.

5. 💾 Guardar el modelo entrenado para su posterior uso.

6. 🎥 Crear un script en Python que permita usar la cámara web para capturar imágenes en tiempo real y hacer predicciones usando el modelo entrenado.

---

## 📁 Archivos del proyecto

### 1. 📓 Notebook completo (`clasificacion_plantas.ipynb`)

Contiene todo el desarrollo del proyecto, desde la carga y preprocesamiento de datos, definición y explicación detallada de la arquitectura de la red neuronal, entrenamiento del modelo, evaluación con métricas como accuracy, precision, recall y f1-score, hasta la exportación y guardado del modelo entrenado.

### 2. 🧩 Modelo guardado (`modelo_keras.keras`)

Archivo que contiene el modelo entrenado guardado en formato Keras. Este archivo permite cargar el modelo sin necesidad de entrenarlo nuevamente, facilitando su uso para predicciones en tiempo real o integración en aplicaciones.

### 3. 📷 Script para webcam (`pruebas_webcam.py`)

Script en Python que abre la cámara web del equipo, captura imágenes en tiempo real y permite, al presionar la tecla 'p', realizar una predicción de la clase de planta usando el modelo guardado. También permite cerrar la aplicación presionando 'q'. La predicción se muestra sobre la imagen en la ventana de la cámara para facilitar la interacción.

---

## 🚀 Uso

1. Ejecutar el notebook para entender el proceso completo y obtener el modelo entrenado.

2. Utilizar el modelo guardado para cargarlo rápidamente en cualquier aplicación.

3. Ejecutar el script `pruebas_webcam.py` para probar el modelo en tiempo real con la cámara web.

---

Si tienes dudas o quieres extender el proyecto, no dudes en contactarme. 😊
