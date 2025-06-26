class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration


sessions = [
    FitnessCenter("C001", "2023", "5", "60"),
    FitnessCenter("C002", "2023", "6", "45"),
    FitnessCenter("C003", "2023", "7", "90"),
    FitnessCenter("C004", "2023", "8", "30"),
    FitnessCenter("C005", "2023", "9", "120")
]

shortest = min(sessions, key=lambda x: x.duration)
longest = max(sessions, key=lambda x: x.duration)

print(f"Самое короткое занятие: {shortest.duration} мин (Клиент: {shortest.client_code})")
print(f"Самое продолжительное занятие: {longest.duration} мин (Клиент: {longest.client_code})")