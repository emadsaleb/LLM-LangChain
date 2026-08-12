import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

gemini_model = genai.GenerativeModel("gemini-2.5-flash")


# load prompt
def load_prompt():
    with open("prompts/rag_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

PROMPT = load_prompt()


def ask_gemini(question, context):
    prompt = PROMPT.format(context=context, question=question)
    response = gemini_model.generate_content(prompt)
    return response.text



