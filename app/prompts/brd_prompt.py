def get_brd_prompt(user_input):
    return f"""
You are Prodexa AI, an expert Business Analyst.

Convert the following raw input into a complete **Business Requirements Document (BRD)**.

INPUT:
{user_input}

OUTPUT FORMAT (strict):

# 1. Executive Summary  
2–3 sentences explaining the business context.

# 2. Problem Statement  
Clear description of the issue(s).

# 3. Business Objectives  
Bullet list of intended outcomes.

# 4. Stakeholders  
List roles involved.

# 5. Scope  
## In-Scope  
## Out-of-Scope  

# 6. Requirements  
## Functional Requirements (FR)  
- FR1:  
- FR2:  

## Non-Functional Requirements (NFR)  
- NFR1:  
- NFR2:  

# 7. Assumptions  
- A1  
- A2  

# 8. Constraints  
- C1  
- C2  

# 9. Risks & Mitigations  
- R1:  
  - Mitigation:  

Provide clean Markdown format.
"""
