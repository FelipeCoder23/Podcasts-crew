import os
import gradio as gr
from crewai import Crew, Process
from decouple import config
from agents import CustomAgents
from tasks import CustomTasks

# Configuración de claves de API desde el archivo .env utilizando decouple
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

class CustomCrew:
    def __init__(self, topic):
        self.topic = topic
        self.conversation = ""

    def run_step(self, agent_task_pair):
        agent, task = agent_task_pair
        # Usamos invoke y accedemos directamente al contenido del mensaje
        response = agent.llm.invoke(task.description)
        content = response.content  # Accedemos directamente al atributo content
        self.conversation += f"{agent.role}: {content}\n\n"
        return self.conversation

    def run(self, update_fn):
        agents = CustomAgents()
        tasks = CustomTasks()

        # Definición de agentes
        turing = agents.alan_turing()
        lovelace = agents.ada_lovelace()
        musk = agents.elon_musk()

        # Definición de tareas
        turing_task_1 = tasks.turing_task_1(turing)
        lovelace_task_1 = tasks.lovelace_task_1(lovelace)
        musk_task_1 = tasks.musk_task_1(musk)

        turing_task_2 = tasks.turing_task_2(turing)
        lovelace_task_2 = tasks.lovelace_task_2(lovelace)
        musk_task_2 = tasks.musk_task_2(musk)

        # Pares de agente-tarea para la secuencia de conversación
        agent_task_pairs = [
            (turing, turing_task_1),
            (lovelace, lovelace_task_1),
            (musk, musk_task_1),
            (turing, turing_task_2),
            (lovelace, lovelace_task_2),
            (musk, musk_task_2)
        ]

        for pair in agent_task_pairs:
            current_conversation = self.run_step(pair)
            update_fn(current_conversation)
        
        return self.conversation

# Función que se conecta con Gradio
def run_podcast(topic, update_fn):
    custom_crew = CustomCrew(topic)
    result = custom_crew.run(update_fn)
    return result

def launch_gradio():
    def gradio_interface(topic):
        def update_fn(new_text):
            return gr.update(value=new_text)

        result = run_podcast(topic, update_fn)
        return result

    iface = gr.Interface(
        fn=gradio_interface,
        inputs=gr.Textbox(lines=2, placeholder="Enter the podcast topic..."),
        outputs=gr.Textbox(label="Podcast Transcript"),
        title="AI Podcast Generator",
        description="Generate a podcast conversation on AI topics with Alan Turing, Ada Lovelace, and Elon Musk.",
        live=True  # Esto activa la actualización en tiempo real
    )
    iface.launch()

if __name__ == "__main__":
    launch_gradio()
