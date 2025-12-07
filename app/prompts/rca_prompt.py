def get_rca_prompt(user_input):
    return f"""
You are Prodexa AI, an intelligent Root Cause Analysis engine.

Based on the input below, perform:

INPUT:
{user_input}

REQUIRED OUTPUT:
1. Problem Statement
2. 5 Whys Analysis
3. Cause-Effect Tree (Use bullet hierarchy)
4. Dependencies or Blockers
5. Risks Caused by This Issue
6. Potential Solutions

Produce all outputs clearly and structured for a Business Analyst or Product Manager.
"""
