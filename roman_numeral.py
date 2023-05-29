import re

def roman_to_int(roman):
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000,
    }

    subtract_pairs = {('I', 'V'), ('I', 'X'), ('X', 'L'),
                      ('X', 'C'), ('C', 'D'), ('C', 'M')}

    total = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and (roman[i], roman[i+1]) in subtract_pairs:
            total += values[roman[i+1]] - values[roman[i]]
            i += 2
        else:
            total += values[roman[i]]
            i += 1
    return total

def input_validation(roman):
    if not roman:
        raise ValueError("Input string is empty. There is no way to write 0 in Roman numerals.")

    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for char in roman:
        if char not in roman_numerals:
            raise ValueError(f"Invalid character: {char}. Roman numerals can only include the characters 'I', 'V', 'X', 'L', 'C', 'D', 'M'.")

    if 'VV' in roman or 'LL' in roman or 'DD' in roman:
        raise ValueError("Invalid repetition. The Roman numerals 'V', 'L', and 'D' can't be repeated.")

    if 'IIII' in roman or 'XXXX' in roman or 'CCCC' in roman or 'MMMM' in roman:
        raise ValueError("Invalid repetition. The Roman numerals 'I', 'X', 'C', and 'M' can't be repeated more than 3 times consecutively.")

    # Check for invalid subtraction sequences
    for i in range(len(roman) - 1):
        if values[roman[i]] < values[roman[i+1]]:
            if i > 0 and values[roman[i-1]] <= values[roman[i]]:
                raise ValueError(f"Invalid sequence: {roman[i-1:i+2]}. A group of numerals written in subtractive notation (of lower value) cannot precede a numeral of larger value. For example, write 'VIII' for 8, not 'IIX'; write 'XIX' for 19, not 'IXX'.")
            if i + 2 < len(roman) and values[roman[i+2]] >= values[roman[i+1]]:
                raise ValueError(f"Invalid sequence: {roman[i:i+3]}. A group of numerals written in subtractive notation (of lower value) cannot precede a numeral of larger value. For example, write 'VIII' for 8, not 'IIX'; write 'XIX' for 19, not 'IXX'.")

    # Check with regex for any other invalid cases
    pattern = r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$'
    if not re.match(pattern, roman):
        raise ValueError("Not valid Roman numeral. Rules dictate separate representation of units, tens, hundreds, and thousands. Examples: 99 is XCIX, not IC. 999 is not IM, and 1999 is not MIM. Constraints: I precedes V or X, X precedes L or C, C precedes D or M.")

def main():
    while True:
        try:
            roman = input("Enter a Roman numeral: ").upper()
            input_validation(roman)
            integer = roman_to_int(roman)
            print(f"The decimal equivalent of {roman} is {integer}")
            break
        except (EOFError, KeyboardInterrupt):
            print("Exiting...")
            break
        except ValueError as e:
            print(e)
            print("Please try again.")

if __name__ == "__main__":
    main()

