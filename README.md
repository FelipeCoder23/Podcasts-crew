# Generador de Podcasts Con agentes de CrewAI

Este proyecto utiliza **CrewAI** y **Gradio** junto con modelos de lenguaje grande (LLMs) para generar conversaciones simuladas en formato de podcast entre agentes de IA que representan a figuras históricas como Alan Turing, Ada Lovelace y Elon Musk. Los usuarios pueden ingresar un tema relacionado con la Inteligencia Artificial (IA) y ver cómo los agentes discuten sobre él en tiempo real.

## Características

- **Agentes Personalizados**: Cada agente tiene un rol y un objetivo específicos en la conversación.
- **Conversación en Formato Podcast**: Los agentes colaboran para discutir el tema propuesto por el usuario.
- **Interfaz Gráfica con Gradio**: Permite a los usuarios interactuar con el sistema de forma sencilla y ver la transcripción del podcast.

  ## Estructura del Proyecto

- `main.py`: Archivo principal que inicia la interfaz de Gradio y coordina la ejecución del podcast.
- `agents.py`: Define los agentes de IA con sus roles y objetivos.
- `tasks.py`: Contiene las tareas que guían la conversación.
- `.env`: Archivo para almacenar la clave de API de OpenAI (no incluido en el repositorio).


## Instalación

- Clona el repositorio.
- Crea un entorno virtual e instala las dependencias (requerimientos).
- Crea el archivo .env y configura las claves de API de OpenAI.
- Ejecuta el proyecto con `python main.py`.
- Abre la URL proporcionada por Gradio en tu navegador.

## Ejemplo de Uso

1. Ingresa un tema relacionado con la IA en la interfaz de Gradio (por ejemplo, "Impacto de la IA en la sociedad").
2. Observa cómo los agentes simulan una conversación en formato de podcast sobre el tema ingresado.
