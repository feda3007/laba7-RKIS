class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

sessions = [
    FitnessCenter("C101", 2022, 1, 50),
    FitnessCenter("C102", 2022, 2, 70),
    FitnessCenter("C103", 2023, 3, 90),
    FitnessCenter("C104", 2023, 1, 80),
    FitnessCenter("C105", 2023, 2, 60),
    FitnessCenter("C106", 2023, 3, 110),
    FitnessCenter("C107", 2023, 4, 100),
    FitnessCenter("C108", 2024, 1, 120),
    FitnessCenter("C109", 2024, 2, 130),
    FitnessCenter("C110", 2024, 3, 90)
]

yearly_total = {}
for session in sessions:
    if session.year not in yearly_total:
        yearly_total[session.year] = 0
    yearly_total[session.year] += session.duration


max_duration = max(yearly_total.values())
best_years = [year for year, total in yearly_total.items() if total == max_duration]
best_year = min(best_years)

print(f"Год с наибольшей суммарной продолжительностью: {best_year}")
print(f"Суммарная продолжительность: {max_duration} мин")
