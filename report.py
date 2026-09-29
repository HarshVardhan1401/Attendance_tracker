"""MODULE 3 - Reports and planner output."""
from src import calculator


def show_report(subjects):
    print("\n" + "=" * 62)
    print(f"{'Subject':<18}{'Attended':>9}{'Total':>7}{'  %':>8}  Status")
    print("-" * 62)
    for s in subjects:
        pct = calculator.percentage(s.attended, s.total)
        print(f"{s.name:<18}{s.attended:>9}{s.total:>7}{pct:>8}  {calculator.status(pct)}")
    print("-" * 62)
    overall = calculator.overall_percentage(subjects)
    print(f"{'OVERALL':<34}{overall:>8}  {calculator.status(overall)}")
    print("=" * 62)


def show_planner(subjects):
    print(f"\nPlanner (target = {calculator.REQUIRED}%)")
    for s in subjects:
        need = calculator.classes_needed(s.attended, s.total)
        skip = calculator.classes_can_skip(s.attended, s.total)
        if need > 0:
            print(f"  {s.name}: attend next {need} class(es) in a row to reach target.")
        else:
            print(f"  {s.name}: you can skip {skip} class(es) and stay safe.")
