from crewai import Task
from textwrap import dedent

class CustomTasks:
    def __tip_section(self):
        return "Keep your responses brief and build on the points of others."

    def turing_task_1(self, agent):
        return Task(
            description=dedent(
                f"""
                Alan Turing, start the discussion with a brief point about AI's potential. Make it short and engaging.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A brief point about AI's potential.",
            agent=agent,
        )

    def turing_task_2(self, agent):
        return Task(
            description=dedent(
                f"""
                Alan Turing, respond to the points raised by Ada Lovelace and Elon Musk. Keep the conversation flowing.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A continuation of the discussion with added insights.",
            agent=agent,
        )

    def lovelace_task_1(self, agent):
        return Task(
            description=dedent(
                f"""
                Ada Lovelace, quickly respond to Turing's point with a focus on ethics. Keep it concise.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A quick response focusing on the ethical aspects.",
            agent=agent,
        )

    def lovelace_task_2(self, agent):
        return Task(
            description=dedent(
                f"""
                Ada Lovelace, continue the discussion by addressing the points raised by Turing and Musk. Add your insights.
                
                {self.__tip_section()}
                """
            ),
            expected_output="Further ethical considerations and discussion.",
            agent=agent,
        )

    def musk_task_1(self, agent):
        return Task(
            description=dedent(
                f"""
                Elon Musk, respond to the ongoing conversation with a quick point on AI risks and opportunities. Be brief.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A concise point on AI risks and opportunities.",
            agent=agent,
        )

    def musk_task_2(self, agent):
        return Task(
            description=dedent(
                f"""
                Elon Musk, follow up with additional thoughts, responding to the points raised by Turing and Lovelace.
                
                {self.__tip_section()}
                """
            ),
            expected_output="A continuation of the discussion with focus on risks and advancements.",
            agent=agent,
        )
