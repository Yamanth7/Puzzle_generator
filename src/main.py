from src.puzzle_generator import generate_puzzle
from src.tracker import PerformanceTracker
from src.yatacku import adjust_difficulty



import time

def main():
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

        if correct:
            print(f"Correct! ✔  Next difficulty: {difficulty}")
        else:
            print(f"Wrong ❌  Correct answer: {correct_answer}. Next difficulty: {difficulty}")

    # Summary
    accuracy = sum([h[0] for h in tracker.history]) / len(tracker.history)
    avg_time = sum([h[1] for h in tracker.history]) / len(tracker.history)

    print("\n====== SESSION SUMMARY ======")
    print(f"User: {name}")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Average Time: {avg_time:.2f}s")
    print(f"Recommended Next Level: {difficulty}")

if __name__ == "__main__":
    main()
