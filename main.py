import os
from typing_extensions import Annotated
import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn

from workflow import Agent


cwd = os.getcwd()
app = typer.Typer()


@app.command()
def prompt(message: str):
    print(f"Action: [bold green]{message}[/bold green]\n")

    agent = Agent(message)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        output = agent.run()
        print(f"\n{output}")


def key_prompt():
    key = typer.prompt("Paste OPENAI_API_KEY e.g sk-...", hide_input=True)
    return key


@app.command("set")
def set_api_key(
    key: Annotated[
        str,
        typer.Option(
            help="Paste OPENAI_API_KEY e.g sk-...",
            show_default=False,
            hide_input=True,
            default_factory=key_prompt,
        ),
    ]
):
    path = os.path.join(cwd, ".env")
    with open(path, "+a") as f:
        f.write(f"OPENAI_API_KEY={key}")
    print(f"Key stored at {path}")


if __name__ == "__main__":
    app()
