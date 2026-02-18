import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=API_KEY)

def procesar_articulo(texto: str, tarea: str) -> str:
    """
    Procesa un artículo usando IA según la tarea indicada.

    :param texto: Texto largo a procesar
    :param tarea: "resumir" o "profesionalizar"
    :return: Texto procesado por la IA
    """
    if tarea not in ["resumir", "profesionalizar"]:
        raise ValueError("Tarea no válida. Debe ser 'resumir' o 'profesionalizar'.")

    # Instrucciones según la tarea
    if tarea == "resumir":
        instruction = """
Eres un Editor Editorial de prestigio.
Genera un resumen ejecutivo conciso y claro del texto proporcionado.
Devuelve **solo el resumen**, sin explicaciones adicionales.
"""
    else:  # profesionalizar
        instruction = """
Eres un Editor Editorial de prestigio.
Edita el texto proporcionado para que suene formal, técnico y profesional.
**Mantén todo el contenido original**, no resumas ni elimines información.
Devuelve **solo el texto profesionalizado**, sin explicaciones, comentarios o introducciones.
"""

    configuration = types.GenerateContentConfig(
        max_output_tokens=4000,
        system_instruction=instruction
    )

    prompt = f"Texto:\n{texto}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=configuration,
        contents=prompt
    )

    return response.text

# ----------------------------
# Programa interactivo
# ----------------------------
if __name__ == "__main__":
    print("=== Editor Editorial de Prestigio IA ===\n")
   
    texto_usuario = input("Ingresa el texto que deseas procesar:\n\n")

    print("\nSelecciona la tarea que deseas realizar:")
    print("1 - Resumir")
    print("2 - Profesionalizar")

    while True:
        opcion = input("\nIngresa 1 o 2: ").strip()
        if opcion == "1":
            tarea_usuario = "resumir"
            break
        elif opcion == "2":
            tarea_usuario = "profesionalizar"
            break
        else:
            print("Opción inválida. Debes ingresar 1 o 2.")

    try:
        resultado = procesar_articulo(texto_usuario, tarea_usuario)
        print("\n=== Resultado ===\n")
        print(resultado)
    except Exception as e:
        print("Ocurrió un error al procesar el texto:", e)