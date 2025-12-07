from app.api.groq_client import run_llm
from app.prompts.discovery_prompt import get_discovery_prompt
from app.prompts.rca_prompt import get_rca_prompt

def run_discovery_analysis(user_input):
    prompt = get_discovery_prompt(user_input)
    return run_llm(prompt)

def run_rca_analysis(user_input):
    prompt = get_rca_prompt(user_input)
    return run_llm(prompt)
