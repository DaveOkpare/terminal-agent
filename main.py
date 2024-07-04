import os
import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn

from workflow import Agent


cwd = os.getcwd()


def main(prompt: str):
    print(f"Action: [bold green]{prompt}[/bold green]\n")

    agent = Agent(prompt)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        output = agent.run()
        print(f"\n{output}")


if __name__ == "__main__":
    typer.run(main)
