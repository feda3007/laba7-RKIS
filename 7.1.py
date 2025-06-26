def sum_string(suma):
    return sum(len(s) for s in suma)

strings=["арбуз", "дыня", "вишня", "кокос"]
result = sum_string(strings)
print(result)
