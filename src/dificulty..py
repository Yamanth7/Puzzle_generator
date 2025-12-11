def adjust_difficulty(current, history):
    if len(history) < 3:
        return current
    recent = history[-3:]
    accuracy = sum([h[0] for h in recent]) / 3
    avg_time = sum([h[1] for h in recent]) / 3
    if accuracy == 1 and avg_time < 10:
        return "hard" if current == "medium" else "medium" if current == "easy" else "hard"
    elif accuracy < 1 or avg_time > 20:
        return "easy" if current == "medium" else "medium" if current == "hard" else "easy"
    return current