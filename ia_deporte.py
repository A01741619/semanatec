# Importar librerías necesarias
import openai
from dotenv import load_dotenv
import os

# Cargar el archivo .env que contiene la API key
load_dotenv()

# Configurar la clave API desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para pedir información al usuario y procesarla con OpenAI
def obtener_estado_animo_usuario():
    respuesta = input("Describe cómo te sientes hoy (energía, estrés, sueño, motivación): ")

    # Solicitar una predicción del modelo de OpenAI utilizando el nuevo formato de la API
    respuesta_modelo = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Puedes usar "gpt-4" si tienes acceso
        messages=[
            {"role": "system", "content": "Eres un asistente que evalúa el estado de ánimo de deportistas basado en su descripción."},
            {"role": "user", "content": f"Basado en la siguiente descripción: '{respuesta}', ¿cómo describirías el estado de ánimo del deportista?"}
        ]
    )

    return respuesta_modelo['choices'][0]['message']['content'].strip()

# Obtener la predicción y mostrarla
estado_animo = obtener_estado_animo_usuario()
print(f"Según tu descripción, tu estado de ánimo es: {estado_animo}")
