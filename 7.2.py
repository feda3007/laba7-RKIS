def extract_positive_numbers(sequence):
    return [x for x in sequence if x > 0]

# Пример:
numbers = [5, -3, 10, 0, -7, 2]
result = extract_positive_numbers(numbers)
print(result)  # [5, 10, 2]