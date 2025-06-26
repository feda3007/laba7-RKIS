def extract_sorted_two_digit_numbers(sequence):
    two_digit = [x for x in sequence if 10 <= x <= 99]
    return sorted(two_digit)

numbers = [5, 15, -10, 99, 7, 42, 123]
result = extract_sorted_two_digit_numbers(numbers)
print(result)