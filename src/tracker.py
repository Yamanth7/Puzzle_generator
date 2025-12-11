class PerformanceTracker:
    def __init__(self):
        # Stores tuples: (correct_or_not, time_taken)
        self.history = []

    def log(self, correct, time_taken):
        """Store whether answer was correct and how long it took."""
        self.history.append((correct, time_taken))

    def accuracy(self):
        """Return accuracy over all attempts."""
        if len(self.history) == 0:
            return 0
        return sum([h[0] for h in self.history]) / len(self.history)

    def average_time(self):
        """Return average solving time."""
        if len(self.history) == 0:
            return 0
        return sum([h[1] for h in self.history]) / len(self.history)
