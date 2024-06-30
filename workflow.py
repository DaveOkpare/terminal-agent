import os
import instructor
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

from models import Feedback, Plan, Syntax

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = instructor.from_openai(OpenAI())


def run(query: str, model: BaseModel = None):
    request = client.chat.completions.create(
        model=os.getenv("MODEL", "gpt-4o"),
        messages=[{"role": "user", "content": query}],
        response_model=model,
    )
    return request


class Agent:
    def __init__(self, request: str) -> None:
        self.request = request
        self.state = ""
        self.max_iterations = 3

    @property
    def plan(self):
        _ = run(query=self.request, model=Plan)
        return _.steps

    def run(self):
        for action in self.plan:
            iteration = 0
            successful = False
            prompt = f"Instruction: {action} \nPrevious Task: {self.state} "

            while not successful and iteration < self.max_iterations:
                print(prompt)
                status = run(query=prompt, model=Syntax).execute()
                feedback, successful = (status.response, status.success)
                print(feedback, successful)
                if successful:
                    self.state = action.step
                else:
                    prompt += f"\nFeedback: {feedback}"

                iteration += 1

            if not successful:
                break

        response = run(
            query=f"Request: {self.request} \nPlan: {self.plan} \nCurrent State: {self.state} \nFeedback: {feedback}",
            model=Feedback,
        )
        return response.message


if __name__ == "__main__":
    a = Agent()
    print(a.run())
