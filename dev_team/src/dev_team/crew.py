from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class DevTeam():
    """DevTeam crew"""

    # These point to the relative yaml config paths
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def requirement_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['requirement_analyst'],
            verbose=True,
            # CRITICAL: This enables terminal interaction
            human_in_the_loop=True
        )

    @task
    def interview_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_task'],
        )

    @task
    def document_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_task'],
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
