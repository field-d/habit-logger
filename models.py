class Entry:

    def __init__(self, mood_score: int, calories: int, exercise_minutes: int, sleep_score: int):

        self.mood_score = self._mood_validation(mood_score)
        self.calories = self._calories_validation(calories)
        self.exercise_minutes = self._exercise_validation(exercise_minutes)
        self.sleep_score = self._sleep_validation(sleep_score)

    def _mood_validation(self, mood_score: int) -> int:

        if not mood_score:
            return 0

        if mood_score > 10:
            return 0
        else:
            return mood_score

    def mood_rating(self):

        if self.mood_score == 0:
            return "No Data"

        if self.mood_score < 5:
            return "Bad Day"
        else:
            return "Good Day"

    def _calories_validation(self, calories: int) -> int:

        if not calories:
            return 0
        elif calories > 1800 and calories < 2200:
            return calories

    def calorie_rating(self):

        if self.calories == 0:
            return "No Data"
        else:
            return self.calories

    def _exercise_validation(self, exercise_minutes: int) -> int:

        if not exercise_minutes:
            return 0
        else:
            return exercise_minutes

    def _sleep_validation(self, sleep_score: int) -> int:

        if not sleep_score:
            return 0

        if sleep_score > 100:
            return 0
        else:
            return sleep_score

    def total_score(self):

        score = 0

        # mood score
        if self.mood_score >= 7:
            score += 3
        elif self.mood_score >= 4:
            score += 2
        else:
            score += 1

        # sleep score
        if self.sleep_score >= 90:
            score += 4
        elif self.sleep_score >= 75:
            score += 3
        elif self.sleep_score >= 50:
            score += 2
        else:
            score += 1

        # exercise mins
        if self.exercise_minutes >= 45:
            score += 4
        elif self.exercise_minutes >= 30:
            score += 3
        elif self.exercise_minutes >= 15:
            score += 2
        else:
            score += 1

        # calories
        if 1800 <= self.calories <= 2200:
            score += 5
        elif self.calories <= 1800:
            score += 3
        else:
            score += 1

        return score

    def __str__(self):
        return f"Mood Score: {self.mood_score}, Calories: {self.calories}, Sleep Score {self.sleep_score}, Exercise Minutes: {self.exercise_minutes}\nTotal Score: {self.total_score()}"


class HabitLog:

    def __init__(self):

        self.entries = {}

    def add_entry(self, entry: Entry):

        self.entries[entry.entry_date] = entry

    def get_last_n_days(self, n: int) -> list[Entry]:

        sorted_dates = sorted(self.entries.keys())
        last_n_dates = sorted_dates[-n:]
        return [self.entries[d] for d in last_n_dates]

    def average_mood(self) -> float:

        if not self.entries:
            return 0
        return sum(e.mood_score() for e in self.entries.values()) / len(self.entries)

    def average_total_score(self) -> float:

        if not self.entries:
            return 0
        return sum(e.total_score() for e in self.entries.values()) / len(self.entries)

    def __str__(self):
        sorted_dates = sorted(self.entries.keys())
        return "\n".join(str(self.entries[d]) for d in sorted_dates)
