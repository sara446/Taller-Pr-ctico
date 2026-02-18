import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# -----------------------------
# Configuración del entorno
# -----------------------------
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=API_KEY)

# -----------------------------
# Instrucciones del sistema
# -----------------------------
system_instruction = """
Eres un vendedor amable y experto de una tienda de tecnología.
Responde las preguntas de los clientes con claridad y cordialidad.
Proporciona especificaciones técnicas completas cuando sea necesario.
Mantén un tono cercano y útil.
"""

# -----------------------------
# Inicializar el chat vacío
# -----------------------------
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        max_output_tokens=4000,
        system_instruction=system_instruction
    )
)

# -----------------------------
# Few-Shot: enviar mensajes de ejemplo para establecer contexto
# -----------------------------
few_shot = [
    "Hola, ¿me puedes dar información sobre el portátil XPro 15?",
    "Gracias, ¿y qué colores tiene disponibles?"
]

# Respuestas predefinidas del modelo (para simular historial)
few_shot_responses = [
    "¡Hola! Claro 😊. El portátil XPro 15 tiene:\n- Procesador Intel i7 de 12ª generación\n- 16GB RAM\n- SSD 512GB\n- Pantalla 15.6\" Full HD\n- Batería hasta 10 horas",
    "El XPro 15 está disponible en Plata, Gris Espacial y Negro Mate."
]

# Enviar los mensajes few-shot y recibir respuestas
for i, msg in enumerate(few_shot):
    chat.send_message(msg)  # El SDK trata esto como usuario
    # Simular la respuesta para mantener contexto
    chat.send_message(few_shot_responses[i])  # El SDK agrega al historial automáticamente

# -----------------------------
# Bucle de chat interactivo
# -----------------------------
print("=== Chat de Soporte Técnico ===")
print("(Escribe 'finalizar' para salir)\n")

while True:
    user_input = input("Cliente: ").strip()
   
    if user_input.lower() == "finalizar":
        print("Asistente: ¡Gracias por visitarnos! Que tengas un excelente día 😊.")
        break

    try:
        response = chat.send_message(user_input)  # Solo se pasa el texto
        print(f"Asistente: {response.text}\n")
    except Exception as e:
        print("Error al procesar la solicitud:", e)