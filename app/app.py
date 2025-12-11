from flask import Flask, render_template, request
from src.puzzle_generator import generate_puzzle
from src.tracker import PerformanceTracker
from src.yatacku import adjust_difficulty

app = Flask(__name__)
tracker = PerformanceTracker()
current_difficulty = "easy"

@app.route("/", methods=["GET", "POST"])
def home():
    global current_difficulty
    puzzle = None
    feedback = None

    if request.method == "POST":
        user_answer = request.form.get("answer")
        question = request.form.get("question")
        correct_answer = eval(question)
        try:
            is_correct = float(user_answer) == correct_answer
        except Exception:
            is_correct = False
        tracker.record(is_correct, 0, current_difficulty)
        current_difficulty = adjust_difficulty(current_difficulty, tracker.history)
        feedback = "Correct!" if is_correct else f"Wrong! Answer was {correct_answer}"

    question, _ = generate_puzzle(current_difficulty)
    puzzle = question

    return render_template(
        "index.html",
        puzzle=puzzle,
        feedback=feedback,
        difficulty=current_difficulty,
        accuracy=tracker.get_accuracy()
    )

if __name__ == "__main__":
    app.run(debug=True)
