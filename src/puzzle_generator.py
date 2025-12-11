import random

def generate_puzzle(difficulty):
    if difficulty == "easy":
        num1, num2 = random.randint(1, 9), random.randint(1, 9)
        op = random.choice(["+", "-"])
    elif difficulty == "medium":
        num1, num2 = random.randint(10, 50), random.randint(1, 20)
        op = random.choice(["+", "-", "*"])
    else:  # hard
        num1, num2 = random.randint(10, 100), random.randint(1, 20)
        op = random.choice(["*", "/"])
        if op == "/" and num2 == 0: num2 = 1  # Avoid division by zero
    
    question = f"{num1} {op} {num2}"
    answer = eval(question)  # Simple eval for demo; in production, use safer parsing
    return question, int(answer)