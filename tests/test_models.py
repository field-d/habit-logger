from datetime import date
from habit_logger.models import Entry

def test_valid_entry():
    # test function to ensure valid entries for the Entry class
    e = Entry(mood_score = 8, calories = 2000, exercise_minutes = 30, sleep_score = 80)
    assert e.mood_score == 8
    assert e.calories == 2000
    assert e.exercise_minutes == 30
    assert e.sleep_score == 80

def test_mood_score_rejects_over_max():
    # test function to ensure mood score cannot be over the defined maximum (10)
    e = Entry(mood_score = 15, calories = 2000, exercise_minutes = 30, sleep_score = 80)
    assert e.mood_score == 0

def test_mood_score_rejects_negative():
    e = Entry(mood_score = -15, calories = 2000, exercise_minutes = 30, sleep_score = 80)
    assert e.mood_score == 0

def test_sleep_score_rejects_over_max():
    e = Entry(mood_score = 8, calories = 2000, exercise_minutes = 30, sleep_score = 101)
    assert e.sleep_score == 0

def test_sleep_score_rejects_negative():
    e = Entry(mood_score = 8, calories = 2000, exercise_minutes = 30, sleep_score = -10)
    assert e.sleep_score == 0

def test_calories_rejects_negative():
    e = Entry(mood_score = 8, calories = -1000, exercise_minutes =30 , sleep_score = 80)
    assert e.calories == 0

def test_exercise_rejects_negative():
    e = Entry(mood_score = 8, calories = 2000, exercise_minutes = -20, sleep_score = 80)

def test_entry_date_defaults_to_today():
    e = Entry(mood_score = 8, calories = 2000, exercise_minutes = -20, sleep_score = 80)
    assert e.entry_date == date.today()

def test_entry_date_can_be_set_explicitly():
    d = date(2026, 7, 1)
    e = Entry(mood_score = 8, calories = 2000, exercise_minutes = -20, sleep_score = 80, entry_date = d)
    assert e.entry_date == d


