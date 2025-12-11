from flask import Flask, render_template, request
from src.puzzle_generator import generate_puzzle
from src.tracker import PerformanceTracker
from src.yatacku import adjust_difficulty
 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    difficulty = request.form.get("difficulty", "medium")

    puzzle = generate_puzzle(difficulty)
    return f"<h2>Your Puzzle:</h2><p>{puzzle}</p>"

if __name__ == "__main__":
    app.run(debug=True)
