"""Easy Attendance Calculator - CLI entry point."""
import logging
from src import input_handler, report, storage

logging.basicConfig(filename="attendance.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

MENU = """
===== ATTENDANCE CALCULATOR =====
1. Enter attendance (4 subjects)
2. View report
3. Planner (classes needed / can skip)
4. Exit
"""


def main():
    subjects = storage.load()
    while True:
        print(MENU)
        choice = input("Choose 1-4: ").strip()
        if choice == "1":
            subjects = input_handler.enter_subjects(4)
            storage.save(subjects)
            print("Saved!")
        elif choice in ("2", "3"):
            if not subjects:
                print("No data yet - choose option 1 first.")
            elif choice == "2":
                report.show_report(subjects)
            else:
                report.show_planner(subjects)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
