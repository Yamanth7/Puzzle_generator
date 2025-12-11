import random

def generate_puzzle(difficulty):
    if difficulty == "easy":
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        op = random.choice(["+", "-"])

    elif difficulty == "medium":
        num1 = random.randint(10, 50)
        num2 = random.randint(1, 20)
        op = random.choice(["+", "-", "*"])

    else:  # hard
        op = random.choice(["*", "/"])
        
        if op == "*":
            num1 = random.randint(10, 100)
            num2 = random.randint(5, 20)
        
        else:  # clean division (always integer)
            num2 = random.randint(2, 12)
            answer = random.randint(2, 12)
            num1 = num2 * answer   # ensures num1 / num2 = answer exactly

    # Calculate correct answer safely
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "*":
        answer = num1 * num2
    else:  # op == "/"
        answer = num1 // num2    # guaranteed integer
    
    question = f"{num1} {op} {num2}"
    return question, answer
