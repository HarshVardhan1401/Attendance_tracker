"""MODULE 1 - Taking and validating user input."""
from src.models import Subject


def read_int(prompt, minimum=0, maximum=None):
    """Keep asking until the user types a valid whole number."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            print(f"  Value must be at least {minimum}"
                  + (f" and at most {maximum}." if maximum is not None else "."))
            continue
        return value


def read_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("  Name cannot be empty.")


def enter_subjects(count=4):
    """Ask for name, total classes and attended classes of each subject."""
    subjects = []
    for i in range(1, count + 1):
        print(f"\n--- Subject {i} of {count} ---")
        name = read_name("Subject name: ")
        total = read_int("Total classes held: ")
        attended = read_int("Classes attended: ", 0, total)
        subjects.append(Subject(name, total, attended))
    return subjects
