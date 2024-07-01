import os
import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn

from workflow import Agent


cwd = os.getcwd()


def main():
    print("\n[bold green]Welcome to the Terminal Agent![/bold green]")
    print("[bold green]--------------------------------[/bold green]\n")

    while True:
        action = typer.prompt("\nWhat action do want the agent to complete?")
        print(f"Action: [bold green]{action}[/bold green]\n")

        agent = Agent(action)

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
