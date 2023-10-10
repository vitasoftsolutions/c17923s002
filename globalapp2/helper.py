def number_to_alphabetic_order(number):
    if 1 <= number <= 26:
        return chr(ord('A') + number - 1)
    else:
        return None  # Return None for numbers outside the range 1-26