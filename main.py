import os
from crewai import Crew
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
        mod = agents.moderator()

        # Definición de tareas
        turing_task = tasks.turing_task(turing)
        lovelace_task = tasks.lovelace_task(lovelace)
        musk_task = tasks.musk_task(musk)
        mod_task = tasks.moderation_task(mod)

        # Creación de la Crew
        crew = Crew(
            agents=[turing, lovelace, musk, mod],
            tasks=[turing_task, lovelace_task, musk_task, mod_task],
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
