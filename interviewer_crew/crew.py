from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class InterviewerCrew():
    agent.config = 'config/agents.yaml'
    task.config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, model_name= "mixtral-8x7b-32768")
    
    @agent
    def company_hr(self) -> Agent:
        return Agent(
            config = self.agents_config['job_role_analyser'],
            llm = self.groq_llm
        )

    @agent
    def senior_engineer(self) -> Agent:
        return Agent(
            config = self.agents_config['question_generator'],
            llm = self.groq_llm
        )

    @task
    def job_responsibilities(self) -> Task:
        return Task(
            config = self.tasks_config['job_role_analysis'],
            agent = self.company_hr(),
        )

    @task
    def interview_questions(self) -> Task:
        return Task(
            config = self.tasks_config['generate_questions'],
            agent = self.senior_engineer(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )