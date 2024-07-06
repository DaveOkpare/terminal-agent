# Terminal Agent

A CLI utility that controls your computer's terminal using an agentic workflow and OpenAI API.

### Setup

First, install the utility with the following steps:

```bash
# Clone the repo
git clone github.com/DaveOkpare/terminal-agent

# Change directory and install the utility
cd terminal-agent
poetry install
```

Set your OPENAI_API_KEY by running this:

```bash
# Paste your OPENAI API Key
agent set sk-OPENAI_API_KEY

# Leave empty to use the password prompt
agent set
```

Alternatively, create a .env and set the `OPENAI_API_KEY` inside of it

```.env
OPENAI_API_KEY=sk-OPENAI_API_KEY
```

### Quickstart

To interact with the agent, run this

```bash
# Example finds the staged files and commits
agent prompt "Read the staged file and commit it"

# Example writes a test for a function
agent prompt "Create a new python file and write a test for the main function in `main.py` inside of it"
```

### Inspiration

This project is inspired by Simon Willison's LLM CLI Utility.
