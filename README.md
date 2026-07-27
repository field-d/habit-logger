Habit Logger

A simple command line application for tracking daily habits; mood, sleep, exercise, and calorie intake.

Brief Overview

Habit Logger lets you log a daily entry covering four metrics, then view your history and see a calculated "total score"
for each day based on how those metrics stack up. Data is saved locally so your log persists between sessions.

This project was built to practice core Python and object-oriented programming concepts: class design, input validation,
 data persistence, and basic testing.

Features

- Add daily entries: mood score, calories, exercise minutes, and sleep score
- Input validation: invalid or out-of-range values are caught and handled sensibly rather than silently corrupting data
- Automatic scoring: each entry gets a weighted total_score based on how mood, sleep, exercise, and calories compare against healthy ranges
- View history: see all logged entries in chronological order
- View stats: average mood and average total score across your logged history
- Persistent storage: entries are saved to a local JSON file, so your data survives closing the program
- One entry per day: logging a second entry for the same date updates that day's entry rather than creating a duplicate

Installation

Clone the repository:
```
bash
   git clone https://github.com/<your-username>/habit-logger.git
   cd habit-logger
(Optional but recommended) Create and activate a virtual environment:
bash
   python3 -m venv venv
   source venv/bin/activate
```
Install dependencies:
```
bash
   pip install -r requirements.txt
Usage
```

Run the CLI from the project root:
```
bash
python3 -m habit_logger.cli
```

You'll see a menu:
```
1. Add entry
2. View history
3. View stats
4. Exit
```
Follow the prompts to log your mood, calories, exercise, and sleep for the day. Entries are saved automatically after
each addition.

Project Structure

```
habit-logger/
├── README.md
├── requirements.txt
├── conftest.py
├── habit_logger/
│   ├── __init__.py
│   ├── models.py       # Entry and HabitLog classes
│   ├── storage.py       # Save/load entries to JSON
│   └── cli.py           # Command-line interface
├── data/
│   └── entries.json     # Saved entries
└── tests/
    └── test_models.py
```

How Scoring Works

Each entry's total_score is calculated by scoring mood, sleep, exercise and calories individually against target ranges
, then summing the results:
- Mood, sleep and exercise: higher values score better
- Calories: a healthy range scores highest, with values further outside that range scoring lower.

Running Tests

This project uses pytest for testing:
```
pip install pytest
pytest tests/
```

What I learned

This project was my first time building something from scratch and following it through to completion - practicing:
- Structuring a Python package across multiple files by responsibility
- Writing validation logic and handling edge cases (missing data, invalid input, out of range values)
- Separating data classes, persistence, and user interaction into distinct layers
- Debugging real import and packaging issues (relative vs. absolute imports, running models vs. scripts)
- Writing basic unit tests with pytest

Possible Future Improvements

- Web Based Interface
- Charts or graphs of trends over time
- Editing and deleting past entries
- More robust input handling in the CLI (currently assumes valid numeric input)
