import subprocess
from typing import List
from pydantic import BaseModel, Field


class Step(BaseModel):
    step: str = Field(description="a step of action to execute")


class Plan(BaseModel):
    """Your task is create a plan of action for an LLM
    agent to solve a given task. Avoid chaining actions.
    Break each step such that it only performs one action."""

    steps: List[Step]


class Status(BaseModel):
    response: str
    success: bool
    code: int


class Syntax(BaseModel):
    """Your task is to generate a bash command to interact with programs
    using the Python subprocess package."""

    command: str = Field(description="bash command to interact with programs")

    def execute(self) -> Status:
        print("Command", self.command)
        try:
            result = subprocess.run(
                self.command,
                text=True,
                check=True,
                shell=True,  # todo: REMOVE shell=True (dangerous)
            )
            output = result.stdout
            return Status(response=output, success=True, code=0)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")
            output = e.stderr
            return Status(response=output, success=False, code=e.returncode)


class Feedback(BaseModel):
    """Your task is to generate a final message to the action(s) performed.
    You will be provided with the user request, completed tasks and feedback."""

    message: str
