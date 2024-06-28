from models import Feedback, Plan, Syntax
from main import run


class Agent:
    def __init__(self, request: str) -> None:
        self.request = request
        self.state = []
        self.max_iterations = 3

    @property
    def plan(self):
        _ = run(query=self.request, model=Plan)
        return _.steps

    def run(self):
        for action in self.plan:
            iteration = 0
            successful = False
            prompt = f"Instruction: {action} \nCompleted Tasks: {self.state} "

            while not successful and iteration < self.max_iterations:
                print(prompt)
                status = run(query=prompt, model=Syntax).execute()
                feedback, successful, code = (
                    status.response,
                    status.success,
                    status.code,
                )
                print(feedback, successful)
                if successful:
                    self.state.append(action.step)
                else:
                    prompt += f"\nFeedback: {feedback}"
                    # if code == 1:
                    #     self.state.append(action.step)

                iteration += 1

            if not successful:
                break

        response = run(
            query=f"Request: {self.request} \nPlan: {self.plan} \nCompleted Tasks: {self.state} \nFeedback: {feedback}",
            model=Feedback,
        )
        return response.message


if __name__ == "__main__":
    a = Agent(
        request="what are all the files in my current directory, find david.txt and if it doesnt exist create it and write hello world in it"
    )
    print(a.run())
