def calculate_area(length, width):
    assert length > 0 and width > 0, "Dimensions must be positive."
    return length * width

print(calculate_area(5, 3))  # Works fine
print(calculate_area(-5, 3))  # Triggers an assertion error
    