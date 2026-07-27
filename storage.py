import json
import os
from datetime import date
from habit_logger.models import Entry, HabitLog

DATA_FILE = "data/entries.json"


def save(habit_log: HabitLog, path: str = DATA_FILE):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    data = []
    for entry in habit_log.entries.values():
        data.append({
            "mood_score": entry.mood_score,
            "calories": entry.calories,
            "exercise_minutes": entry.exercise_minutes,
            "sleep_score": entry.sleep_score,
            "entry_date": entry.entry_date.isoformat(),
        })
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def load(path: str = DATA_FILE) -> HabitLog:
    log = HabitLog()
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        # if no file yet - return an empty log
        return log

    for item in data:
        entry = Entry(
            mood_score=item["mood_score"],
            calories=item["calories"],
            exercise_minutes=item["exercise_minutes"],
            sleep_score=item["sleep_score"],
            entry_date=date.fromisoformat(item["entry_date"]),
        )
        log.add_entry(entry)
    return log


