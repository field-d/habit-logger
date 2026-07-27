from habit_logger.models import Entry
from habit_logger import storage

def add_entry_flow(log):
    mood = int(input("Please insert your mood score (0-10): "))

    calories = int(input("Please insert your caloric intake for the day: "))

    exercise = int(input("Please insert your exercise minutes for the day: "))

    sleep = int(input("Please insert your sleep score (0-100): "))

    entry = Entry(mood_score=mood, calories=calories, exercise_minutes=exercise, sleep_score=sleep)
    log.add_entry(entry)
    storage.save(log)
    print("Entry has been saved.\n")

def view_history_flow(log):
    print(log)
    print()

def view_stats_flow(log):
    print(f"Average mood: {log.average_mood():.1f}")
    print(f"Average total score: {log.average_total_score():.1f}\n")

def main():
    log = storage.load() # runs once at startup, loads all existing data once

    while True:
        print("1. Add entry\n2. View history\n3. View stats\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry_flow(log)
        elif choice == "2":
            view_history_flow(log)
        elif choice == "3":
            view_stats_flow(log)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please choose a valid option.\n")


if __name__ == "__main__":
    main()