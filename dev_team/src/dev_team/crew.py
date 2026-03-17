from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class DevTeam():
    """DevTeam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def requirement_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['requirement_analyst'],
            verbose=True,
            human_in_the_loop=True
        )

    @task
    def interview_user_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_user_task'],
        )

    @task
    def generate_docs_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_docs_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DevTeam crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
