def roman_to_int(roman):
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000,
    }

    # Subtraction pairs
    subtract_pairs = {('I', 'V'), ('I', 'X'), ('X', 'L'),
                      ('X', 'C'), ('C', 'D'), ('C', 'M')}

    total = 0
    i = 0
    while i < len(roman):
        # If this is a subtraction pair
        if i + 1 < len(roman) and (roman[i], roman[i+1]) in subtract_pairs:
            total += values[roman[i+1]] - values[roman[i]]
            i += 2
        # Else just add this number
        else:
            total += values[roman[i]]
            i += 1
    return total

def main():
    roman = input("Enter a Roman numeral: ")
    integer = roman_to_int(roman)
    print(f"The decimal equivalent of {roman} is {integer}")

if __name__ == "__main__":
    main()

