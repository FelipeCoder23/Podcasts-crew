import os
from crewai import Crew, Process
from decouple import config
from agents import CustomAgents
from tasks import CustomTasks

# Configuración de claves de API desde el archivo .env utilizando decouple
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

class CustomCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
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

        # Creación de la Crew con varias tareas para cada agente
        crew = Crew(
            agents=[turing, lovelace, musk],
            tasks=[turing_task_1, lovelace_task_1, musk_task_1, 
                   turing_task_2, lovelace_task_2, musk_task_2],
            process=Process.sequential,  # Flujo secuencial para mantener el orden
            verbose=True,
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to the AI Podcast Crew")
    print("-------------------------------")
    topic = input("Enter the podcast topic: ")

    custom_crew = CustomCrew(topic)
    result = custom_crew.run()

    print("\n\n########################")
    print("## Podcast Transcript:")
    print("########################\n")
    print(result)
