def save_markdown(content, filename):
    with open(f"exports/{filename}", "w", encoding="utf-8") as f:
        f.write(content)
