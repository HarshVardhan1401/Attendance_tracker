"""MODULE 2 - Calculation logic (no input/print here, so it is easy to test)."""
import math

REQUIRED = 75.0  # minimum attendance % (change if your college differs)


def percentage(attended, total):
    """Attendance % rounded to 2 decimals. 0 if no classes yet."""
    if total == 0:
        return 0.0
    return round(attended / total * 100, 2)


def overall_percentage(subjects):
    """Combined % across all subjects."""
    attended = sum(s.attended for s in subjects)
    total = sum(s.total for s in subjects)
    return percentage(attended, total)


def classes_needed(attended, total, required=REQUIRED):
    """How many classes in a row you must attend to reach `required` %."""
    r = required / 100
    if total == 0 or attended / total >= r:
        return 0
    return math.ceil((r * total - attended) / (1 - r))


def classes_can_skip(attended, total, required=REQUIRED):
    """How many classes you can miss and still stay at/above `required` %."""
    r = required / 100
    if total == 0:
        return 0
    return max(0, math.floor(attended / r - total))


def status(pct, required=REQUIRED):
    return "SAFE" if pct >= required else "LOW"
