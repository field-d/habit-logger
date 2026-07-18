from models import Entry, HabitLog

__version__ = "0.1.0"

log = HabitLog()

log.add_entry(Entry(mood_score=8, calories=2000, exercise_minutes=30, sleep_score=80))
log.add_entry(Entry(mood_score=4, calories=1900, exercise_minutes=40, sleep_score=75))

print(log)
print("Average mood: ", log.average_mood())
print("Average total score: ", log.average_total_score())
