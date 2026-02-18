import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno desde el archivo .env
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

# Configuración: Explicación corta sobre Inferencia en IA
configuration = types.GenerateContentConfig(
    max_output_tokens=300,
    system_instruction="""Eres un experto en Inteligencia Artificial.
Explica claramente qué es la "Inferencia en IA" en menos de 50 palabras.
Tu respuesta debe ser completa y coherente, no solo una palabra.
Responde con un párrafo completo.
"""
)

# Consulta simple al modelo
response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=configuration,
    contents="¿Qué es la Inferencia en IA?"
)

print(response.text)
