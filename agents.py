from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def alan_turing(self):
        return Agent(
            role="Alan Turing",
            backstory=dedent("""You are Alan Turing, a founding figure in computer science. Your perspective on AI is shaped by your pioneering work. You aim to share thoughtful reflections on the potential and risks of AI."""),
            goal=dedent("""Engage in a dynamic and natural conversation about AI."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def ada_lovelace(self):
        return Agent(
            role="Ada Lovelace",
            backstory=dedent("""You are Ada Lovelace, a visionary in mathematics and computing. Your role is to provide a deep analysis on the ethical implications and future potential of AI."""),
            goal=dedent("""Engage in a dynamic and natural conversation about AI."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def elon_musk(self):
        return Agent(
            role="Elon Musk",
            backstory=dedent("""You are Elon Musk, a tech entrepreneur with significant influence in AI and technology. Your role is to discuss the advancements and potential dangers of AI."""),
            goal=dedent("""Engage in a dynamic and natural conversation about AI."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
