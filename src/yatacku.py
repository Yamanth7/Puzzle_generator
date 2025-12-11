 def adjust_difficulty(current, history):
    """
    Adjusts difficulty based on last 3 attempts.
    - Promote: 100% accuracy + fast solving (<5 sec avg)
    - Demote: accuracy <60% OR slow solving (>12 sec avg)
    - Otherwise: keep same difficulty
    """

    # Need at least 3 attempts to adjust
    if len(history) < 3:
        return current

    # Last 3 records: [(correct, time), ...]
    recent = history[-3:]
    accuracy = sum([h[0] for h in recent]) / 3
    avg_time = sum([h[1] for h in recent]) / 3

    levels = ["easy", "medium", "hard"]
    idx = levels.index(current)

    # -------- Promotion rules --------
    if accuracy == 1.0 and avg_time < 5:
        if idx < 2:  # Not already at 'hard'
            return levels[idx + 1]

    # -------- Demotion rules --------
    if accuracy < 0.6 or avg_time > 12:
        if idx > 0:  # Not already at 'easy'
            return levels[idx - 1]

    # -------- No change --------
    return current
