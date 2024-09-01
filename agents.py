from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def alan_turing(self):
        return Agent(
            role="Alan Turing",  # Usando el nombre del personaje como el rol
            backstory=dedent("""You are Alan Turing, a founding figure in computer science. Your perspective on AI is shaped by your pioneering work. You aim to share thoughtful reflections on the potential and risks of AI."""),
            goal=dedent("""Develop insights on AI and its future by building on the points made by the other participants."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def ada_lovelace(self):
        return Agent(
            role="Ada Lovelace",  # Usando el nombre del personaje como el rol
            backstory=dedent("""You are Ada Lovelace, a visionary in mathematics and computing. Your role is to provide a deep analysis on the ethical implications and future potential of AI."""),
            goal=dedent("""Build on the discussion points to address the ethical considerations and future implications of AI."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def elon_musk(self):
        return Agent(
            role="Elon Musk",  # Usando el nombre del personaje como el rol
            backstory=dedent("""You are Elon Musk, a tech entrepreneur with significant influence in AI and technology. Your role is to discuss the advancements and potential dangers of AI."""),
            goal=dedent("""Elaborate on the potential risks and advancements of AI, incorporating previous points made during the discussion."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def moderator(self):
        return Agent(
            role="Moderator",  # El moderador sigue siendo un rol funcional
            backstory=dedent("""You are the moderator tasked with guiding a fluid conversation on AI advancements. Ensure each participant contributes progressively."""),
            goal=dedent("""Guide the podcast discussion, prompting each participant to build on previous contributions. Ensure a cohesive and flowing discussion."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
