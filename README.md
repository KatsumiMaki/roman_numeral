# Roman to Decimal Converter

This is a simple Python script that takes a Roman numeral as input and outputs its decimal equivalent.

## Description

The script follows the traditional rules of Roman numerals to convert the input to a decimal number (1 to 3,999):

1. When certain numerals are repeated, the number represented by them is their sum. For example, II = 1 + 1 = 2.
2. No Roman numerals can come together more than 3 times.
3. The letters V, L, and D are not repeated.
4. Only I, X, and C can be used as subtractive numerals, and must not be repeated (IIX not allowed).
5. When a Roman numeral is placed after another Roman numeral of greater value, the result is the sum of the numerals.
6. When a Roman numeral is placed before another Roman numeral of greater value, the result is the difference between the numerals.
7. When a Roman numeral of a smaller value is placed between two numerals of greater value, it is subtracted from the numeral on its right.
8. Roman numerals strictly represent units (I), tens (X), hundreds (C), and thousands (M) as separate items, following the arrangement on an abacus.
9. Roman numerals do not follow any place value system.
10. There is no Roman numeral for zero (0).

## Getting Started

### Dependencies

This script requires Python 3.6 or later.

### Executing program

Run the script from the command line:

```bash
python3 roman_numeral.py
```

### Input

Enter a Roman numeral when prompted. The script accepts upper- and lowercase Roman numerals.

### Output

The script outputs the decimal equivalent of the input Roman numeral.

### Exiting the Program

You can exit the program by either submitting a valid Roman numeral or, if in a Unix-based environment, sending EOF (End of File, such as ^d) on a blank line. 

## Help

For any issues with input validation, refer to the rules above. The script will raise a ValueError with a detailed message for invalid inputs.

## License

This project is licensed under the GPL-3.0 license. The GPL-3.0 license allows for free distribution, modification, and use of the software, but requires the same licensing when the project is distributed further.
