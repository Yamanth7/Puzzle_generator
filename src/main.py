from puzzle_generator import generate_puzzle
from tracker import PerformanceTracker
from adaptive_engine import adjust_difficulty
import time

tracker = PerformanceTracker()
name = input("Enter your name: ")
difficulty = input("Choose initial difficulty (easy/medium/hard): ").lower()
for i in range(10):
    question, correct_answer = generate_puzzle(difficulty)
    start = time.time()
    user_answer = int(input(f"{question} = "))
    end = time.time()
    correct = 1 if user_answer == correct_answer else 0
    tracker.log(correct, end - start)
    difficulty = adjust_difficulty(difficulty, tracker.history)
    print(f"Correct! Next difficulty: {difficulty}" if correct else f"Wrong. Next difficulty: {difficulty}")

# Summary
accuracy = sum([h[0] for h in tracker.history]) / len(tracker.history)
avg_time = sum([h[1] for h in tracker.history]) / len(tracker.history)
print(f"Session Summary for {name}: Accuracy: {accuracy:.2f}, Avg Time: {avg_time:.2f}s, Recommended Next Level: {difficulty}")