# Easy Attendance Calculator

## Overview
Simple Python CLI that calculates attendance for four subjects.

## Features
- Module 1: Input with validation (`src/input_handler.py`)
- Module 2: Calculation & planner logic (`src/calculator.py`)
- Module 3: Report display (`src/report.py`)
- JSON storage + logging

## Technologies
Python 3.8+ (standard library only), unittest, Git

## Install & Run
```
git clone <your-repo-url>
cd attendance_tracker
python main.py
```

## Testing
```
python -m unittest discover tests
```

## Structure
```
main.py
src/  models.py  input_handler.py  calculator.py  report.py  storage.py
tests/test_calculator.py
```
