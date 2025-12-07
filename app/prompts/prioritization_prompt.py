def get_prioritization_prompt(user_input):
    return f"""
You are Prodexa AI, acting as a Product Strategy Analyst.

Based on the input below, perform:

INPUT:
{user_input}

REQUIRED OUTPUT:

# 1. RICE Scoring Table
Columns:
- Feature
- Reach (1–10)
- Impact (1–10)
- Confidence (1–10)
- Effort (1–10)
- RICE Score (auto-calculated)

Provide 10+ features.

# 2. MoSCoW Classification
Categorize each feature as:
- Must Have
- Should Have
- Could Have
- Won't Have

# 3. Priority Ranking
Top 10 features ranked from highest to lowest strategic value.

Output in clean Markdown.
"""
