from app.api.groq_client import run_llm
from app.prompts.brd_prompt import get_brd_prompt
from app.prompts.prd_prompt import get_prd_prompt

def generate_brd(user_input):
    prompt = get_brd_prompt(user_input)
    return run_llm(prompt)

def generate_prd(user_input):
    prompt = get_prd_prompt(user_input)
    return run_llm(prompt)
