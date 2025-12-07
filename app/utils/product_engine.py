from app.api.groq_client import run_llm
from app.prompts.user_story_prompt import get_user_story_prompt
from app.prompts.prioritization_prompt import get_prioritization_prompt
from app.prompts.roadmap_prompt import get_roadmap_prompt

def generate_user_stories(user_input):
    prompt = get_user_story_prompt(user_input)
    return run_llm(prompt)

def generate_prioritization(user_input):
    prompt = get_prioritization_prompt(user_input)
    return run_llm(prompt)

def generate_product_roadmap(user_input):
    prompt = get_roadmap_prompt(user_input)
    return run_llm(prompt)
