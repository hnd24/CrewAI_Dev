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
            human_in_the_loop=True # Cho phép Agent tương tác
        )

    @task
    def interview_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_task'],
            human_input=True # BẮT BUỘC: Dừng terminal để đợi bạn nhập liệu
        )

    @task
    def srs_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['srs_generation_task'],
            output_file='output/requirements.md', # Ghi file thực tế vào thư mục gốc
            context=[self.interview_task()] # Lấy dữ liệu từ cuộc phỏng vấn
        )

    @task
    def plan_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_generation_task'],
            output_file='output/plan.md', # Ghi file thực tế vào thư mục gốc
            context=[self.srs_generation_task()] # Lấy dữ liệu từ bản SRS
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