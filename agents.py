import subprocess
from typing import List
from pydantic import BaseModel, Field


class Step(BaseModel):
    step: str = Field(description="a step of action to execute")


class Plan(BaseModel):
    """Your task is create a plan of action for an LLM
    agent to solve a given task. Avoid dependence of other steps.
    Make each step clear and independent of other steps."""

    steps: List[Step]


class Syntax(BaseModel):
    """Your task is to generate a bash command to interact with programs
    using the Python subprocess package."""

    command: str = Field(description="bash command to interact with programs")

    def execute(self):
        commands = self.command.split(" ")
        try:
            result = subprocess.run(
                commands, capture_output=True, text=True, check=True
            )
            output = result.stdout
            return output
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")
            output = e.stderr
            return output
