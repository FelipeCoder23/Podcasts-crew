from crewai import Task
from textwrap import dedent

class CustomTasks:
    def __tip_section(self):
        return "Please focus on having a natural and engaging conversation."

    def turing_task(self, agent):
        return Task(
            description=dedent(
                f"""
                Alan Turing, please start the discussion by sharing your thoughts on AI and its future.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A natural and engaging discussion on AI's future.",
            agent=agent,
        )

    def lovelace_task(self, agent):
        return Task(
            description=dedent(
                f"""
                Ada Lovelace, continue by elaborating on Alan Turing's points, especially focusing on ethical considerations.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A thoughtful continuation of the discussion with a focus on ethics.",
            agent=agent,
        )

    def musk_task(self, agent):
        return Task(
            description=dedent(
                f"""
                Elon Musk, please add your insights on the potential risks and advancements of AI, referencing the previous discussions.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A discussion on AI risks and advancements, building on previous points.",
            agent=agent,
        )

    def moderation_task(self, agent):
        return Task(
            description=dedent(
                f"""
                As the moderator, guide the conversation. Ensure that participants build on each other's points and maintain a natural, conversational flow. Wrap up the discussion after everyone has had their responses.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A smoothly moderated, natural discussion on AI.",
            agent=agent,
        )
