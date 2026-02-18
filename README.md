# Proyecto Taller Practico - Gemini API

Este proyecto está diseñado para interactuar con la API de Gemini de Google. A través de tres ejercicios prácticos, se aprende cómo realizar consultas simples, procesar textos de forma inteligente y crear un chat de soporte con historial utilizando la API de Gemini.

## Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

TallerPractico/
│
├── env/ # Carpeta de entorno virtual
│ └── (archivos del entorno virtual)
│
├── img/ # Imágenes de las pruebas
│ ├── Ejercicio1.png
│ ├── Ejercicio2Resumir.png
│ ├── Ejercicio2Profesionalizar.png
│ ├── Ejercicio3PruebaPt1.png
│ ├── Ejercicio3PruebaPt2.png
│ ├── Ejercicio3PruebaPt3.png
│ ├── Ejercicio3PruebaPt4.png
│ └── ...
│
├── src/ # Código fuente
│ ├── ejercicio1.py # Ejercicio 1: Conexión y Petición Básica
│ ├── ejercicio2.py # Ejercicio 2: Procesador de Textos Inteligente
│ ├── ejercicio3.py # Ejercicio 3: Chat de Soporte con Historial
│ ├── prueba_entorno.py
│ └── ...
│
├── .env # Contiene la API Key para el acceso a Gemini API
├── pyvenv.cfg # Configuración del entorno virtual
└── README.md # Explicación del proyecto y cómo ejecutarlo

### **Archivos Principales**

- **ejercicio1.py**: Conexión a la API de Gemini y realización de una consulta simple sobre "Inferencia en IA".
  
- **ejercicio2.py**: Procesador de textos inteligente que puede resumir o profesionalizar un texto, dependiendo de la tarea proporcionada.
  
- **ejercicio3.py**: Simula un sistema de chat de soporte para una tienda de tecnología, con historial de interacciones (Few-Shot) y permite que el usuario realice preguntas hasta que escriba "finalizar".

---

## Instrucciones de Uso

Para ejecutar el proyecto y probar los ejercicios, sigue los siguientes pasos:

### **1. Clona o descarga el repositorio:**

Puedes clonar el repositorio desde GitHub usando Git:


git clone https://github.com/tu_usuario/TallerPractico.git
O descargarlo como archivo ZIP y descomprimirlo.

### **2. Instala las dependencias necesarias:**
Asegúrate de tener instalado Python 3.8+ y pip. Luego, instala las dependencias usando el siguiente comando:
pip install -r requirements.txt
Este comando instalará todas las librerías necesarias, como google-genai, dotenv, entre otras.
### **3. Configura tu clave de API de Gemini:**
Para interactuar con la API de Gemini de Google, necesitarás configurar tu API Key.
Crea un archivo .env en la raíz del proyecto (si no lo tienes).
Dentro del archivo .env, agrega la siguiente línea:
GENAI_API_KEY=tu_api_key_aqui
Reemplaza "tu_api_key_aqui" con tu clave de API de Gemini. Puedes obtener la clave siguiendo los pasos en Google Cloud Console.
### **4. Ejecuta los ejercicios:**
Puedes ejecutar los scripts directamente en tu terminal o IDE:
Ejercicio 1: Conexión y Petición Básica
Este script consulta a la API sobre la "Inferencia en IA" y devuelve una explicación concisa en menos de 50 palabras.
python src/ejercicio1.py
Ejercicio 2: Procesador de Textos Inteligente
Este script permite elegir entre resumir o profesionalizar un texto largo, basado en la tarea proporcionada.
python src/ejercicio2.py
Ejercicio 3: Chat de Soporte con Historial
Este script simula un chat de soporte para una tienda de tecnología. El chat mantiene un historial de interacciones previas y responde a preguntas del usuario hasta que escriba "finalizar".
python src/ejercicio3.py
### **5. Revisa las imágenes de las pruebas**
Cada ejercicio tiene una imagen correspondiente que muestra el resultado de la ejecución del código. Estas imágenes se encuentran en la carpeta img/. Las imágenes están nombradas de la siguiente forma:
- **Ejercicio1.png**: Muestra la salida de la consulta sobre la "Inferencia en IA".
- **Ejercicio2Resumir.png**: Muestra el resultado del procesamiento de un texto para resumirlo.
- **Ejercicio2Profesionalizar.png**: Muestra el resultado del procesamiento de un texto para hacerlo más formal y técnico.
- **Ejercicio3PruebaPt1.png hasta Ejercicio3PruebaPt4.png**: Muestran las interacciones del chat de soporte con historial, incluyendo las preguntas y respuestas de ejemplo.
  
Puedes revisar estas imágenes para comparar los resultados obtenidos con las salidas esperadas.
Detalles de la Implementación
- **Ejercicio 1**: Conexión y Petición Básica
Este ejercicio demuestra cómo conectar el cliente de Gemini API y realizar una consulta sencilla, pidiendo una explicación sobre la "Inferencia en IA". La respuesta es concisa y se ajusta al límite de 50 palabras.
- **Ejercicio 2**: Procesador de Textos Inteligente
Este ejercicio utiliza la API para procesar un texto largo. Dependiendo de la tarea (resumir o profesionalizar), el modelo genera un resumen ejecutivo o transforma el texto para que suene más formal y técnico. Se usa un rol de "Editor Editorial de prestigio" para guiar el estilo de la respuesta.
- **Ejercicio 3**: Chat de Soporte con Historial (Few-Shot)
El chat simula el soporte de una tienda de tecnología. Se pre-cargan ejemplos de interacción utilizando un historial de mensajes (Few-shot). El modelo responde preguntas sobre productos (como el portátil XPro 15) y mantiene un hilo de conversación hasta que el usuario decide finalizar. El rol de la IA está definido como un vendedor amable.
Conclusión
Este proyecto demuestra cómo interactuar con la API de Gemini para realizar tareas de procesamiento de texto, como consultas simples, resúmenes y profesionalización de textos. También incluye la implementación de un chat de soporte con historial, lo que permite mantener un flujo continuo de la conversación.
### **Autor**
Catalina Gordillo Peña

Sara Murcia Rojas
