import os
import instructor
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

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
