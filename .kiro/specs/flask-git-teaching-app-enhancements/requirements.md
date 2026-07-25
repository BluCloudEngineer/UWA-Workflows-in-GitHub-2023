# Requirements Document

## Introduction

This document defines the requirements for enhancing the "All in One Computer Science Calculator" — a Python Flask web application used to teach students how to use Git. The application currently supports addition only. These enhancements add 18 additional calculator operations (for a total of 19) and a UI/UX redesign.

All operations are exposed via an HTTP POST endpoint at `/calculate`. Each operation receives a JSON-like form payload containing an `operation` key, a `number_1` key, and a `number_2` key. Some operations use both numbers; others use only `number_1` (the `number_2` key must still be present in the payload). Results are rendered back to the user in the `index.html` template as `Result: <value>`.

## Glossary

- **Calculator**: The Python Flask web application (`application.py`) that receives POST requests and returns computed results.
- **Client**: A web browser or test client sending HTTP POST requests to the Calculator.
- **Operation**: A mathematical or conversion function identified by the `operation` field in the POST payload.
- **number_1**: The primary numeric input provided in the POST payload.
- **number_2**: The secondary numeric input provided in the POST payload; required to be present in every request even if its value is not used by the operation.
- **Result**: The formatted string rendered in the HTML template in the form `Result: <value>`.
- **±**: The plus-minus sign (Unicode U+00B1) prepended to results where both positive and negative roots are valid.
- **Binary_Representation**: An 8-digit zero-padded binary string produced from an integer input.
- **Hex_Representation**: An uppercase hexadecimal string produced from an integer input.
- **Test_Suite**: The collection of pytest unit tests located in `tests/test_application.py`.
- **UI**: The HTML/CSS/JavaScript front-end rendered in the user's browser via `index.html`.

## Requirements

### Requirement 1: Addition

**User Story:** As a student, I want to add two numbers together using the calculator, so that I can verify the sum and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"addition"`, a valid `number_1`, and a valid `number_2` is received, THE Calculator SHALL return a result equal to `number_1 + number_2`.
2. THE Calculator SHALL format the addition result as a float (e.g., `21.0` for inputs 12 and 9).

---

### Requirement 2: Subtraction

**User Story:** As a student, I want to subtract one number from another using the calculator, so that I can verify the difference and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"subtraction"`, a valid `number_1`, and a valid `number_2` is received, THE Calculator SHALL return a result equal to `number_1 - number_2`.
2. THE Calculator SHALL support negative results (e.g., `9 - 16 = -7`).

---

### Requirement 3: Multiplication

**User Story:** As a student, I want to multiply two numbers using the calculator, so that I can verify the product and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"multiplication"`, a valid `number_1`, and a valid `number_2` is received, THE Calculator SHALL return a result equal to `number_1 * number_2`.
2. THE Calculator SHALL format the multiplication result as a float (e.g., `240.0` for inputs 12 and 20).

---

### Requirement 4: Division

**User Story:** As a student, I want to divide one number by another using the calculator, so that I can verify the quotient and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"division"`, a valid `number_1`, and a non-zero `number_2` is received, THE Calculator SHALL return a result equal to `number_1 / number_2`.
2. THE Calculator SHALL format the division result as a float (e.g., `4.0` for inputs 100 and 25).
3. IF `number_2` is zero, THEN THE Calculator SHALL return an appropriate error message instead of raising an unhandled exception.

---

### Requirement 5: Modulus

**User Story:** As a student, I want to calculate the remainder of dividing one number by another, so that I can understand modular arithmetic and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"modulus"`, a valid `number_1`, and a valid `number_2` is received, THE Calculator SHALL return a result equal to `number_1 % number_2`.
2. THE Calculator SHALL format the modulus result as a float (e.g., `8.0` for inputs 100 and 23).

---

### Requirement 6: Exponential (e)

**User Story:** As a student, I want to calculate e raised to a given power, so that I can explore natural exponential growth and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"exponential"` and a valid `number_1` is received, THE Calculator SHALL return a result equal to `math.exp(number_1)` (i.e., e^number_1).
2. THE Calculator SHALL use `number_1` as the exponent and SHALL NOT use `number_2` in the calculation.
3. THE Calculator SHALL return a result with sufficient decimal precision (e.g., `20.0855369231877` for input 3).

---

### Requirement 7: Custom Exponential

**User Story:** As a student, I want to raise one number to the power of another, so that I can explore exponentiation with custom bases and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"custom_exponential"`, a valid `number_1` (base), and a valid `number_2` (exponent) is received, THE Calculator SHALL return a result equal to `number_1 ** number_2`.
2. THE Calculator SHALL format the custom exponential result as a float (e.g., `81.0` for inputs 3 and 4).

---

### Requirement 8: Square Root

**User Story:** As a student, I want to calculate the square root of a number, so that I can understand radical expressions and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"sqrt"` and a valid `number_1` is received, THE Calculator SHALL return a result equal to `math.sqrt(number_1)`.
2. THE Calculator SHALL prefix the square root result with the plus-minus sign and a space (e.g., `± 12.0` for input 144).
3. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 9: Custom Square Root

**User Story:** As a student, I want to calculate the nth root of a number with a custom root degree, so that I can explore higher-order radicals and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"custom_sqrt"`, a valid `number_1` (value), and a valid `number_2` (root degree) is received, THE Calculator SHALL return a result equal to `number_1 ** (1 / number_2)`.
2. IF `number_2` is divisible by 2, THEN THE Calculator SHALL prefix the result with the plus-minus sign and a space (e.g., `± 3.0` for inputs 81 and 4).
3. IF `number_2` is NOT divisible by 2, THEN THE Calculator SHALL return the result without the plus-minus prefix (e.g., `3.0` for inputs 27 and 3).

---

### Requirement 10: Natural Log

**User Story:** As a student, I want to calculate the natural logarithm of a number, so that I can explore logarithmic functions and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"natural_log"` and a valid `number_1` is received, THE Calculator SHALL return a result equal to `math.log(number_1)`.
2. THE Calculator SHALL return a result with sufficient decimal precision (e.g., `6.29710931993394` for input 543).
3. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 11: Log Base 2

**User Story:** As a student, I want to calculate the base-2 logarithm of a number, so that I can explore binary logarithms relevant to computer science and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"log2"` and a valid `number_1` is received, THE Calculator SHALL return a result equal to `math.log2(number_1)`.
2. THE Calculator SHALL format the log base 2 result as a float (e.g., `7.0` for input 128).
3. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 12: Log Base 10

**User Story:** As a student, I want to calculate the base-10 logarithm of a number, so that I can explore common logarithms and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"log10"` and a valid `number_1` is received, THE Calculator SHALL return a result equal to `math.log10(number_1)`.
2. THE Calculator SHALL format the log base 10 result as a float (e.g., `3.0` for input 1000).
3. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 13: Custom Log Base

**User Story:** As a student, I want to calculate the logarithm of a number using a custom base, so that I can explore arbitrary-base logarithms and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"custom_log_base"`, a valid `number_1` (value), and a valid `number_2` (base) is received, THE Calculator SHALL return a result equal to `math.log(number_1, number_2)`.
2. THE Calculator SHALL format the custom log base result as a float (e.g., `2.0` for inputs 16 and 4).

---

### Requirement 14: Factorial

**User Story:** As a student, I want to calculate the factorial of an integer, so that I can explore combinatorics and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"factorial"` and a valid non-negative integer `number_1` is received, THE Calculator SHALL return a result equal to `math.factorial(int(number_1))`.
2. THE Calculator SHALL format the factorial result as a float (e.g., `120.0` for input 5).
3. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 15: Celsius to Fahrenheit

**User Story:** As a student, I want to convert a temperature from Celsius to Fahrenheit using the calculator, so that I can practise unit conversions and submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"celsius_to_fahrenheit"` and a valid `number_1` (temperature in degrees Celsius) is received, THE Calculator SHALL return a result equal to `(number_1 * 9/5) + 32`.
2. THE Calculator SHALL append the string `" °F"` to the result (e.g., `86.0 °F` for input 30).
3. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 16: Celsius to Kelvin

**User Story:** As a student, I want to convert a temperature from Celsius to Kelvin using the calculator, so that I can practise scientific unit conversions and submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"celsius_to_kelvin"` and a valid `number_1` (temperature in degrees Celsius) is received, THE Calculator SHALL return a result equal to `number_1 + 273.15`.
2. THE Calculator SHALL append the string `" K"` to the result without a degrees sign (e.g., `298.15 K` for input 25).
3. THE Calculator SHALL NOT include the degrees sign (°) in the Kelvin result.
4. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 17: Fahrenheit to Celsius

**User Story:** As a student, I want to convert a temperature from Fahrenheit to Celsius using the calculator, so that I can practise unit conversions in reverse and submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"fahrenheit_to_celsius"` and a valid `number_1` (temperature in degrees Fahrenheit) is received, THE Calculator SHALL return a result equal to `(number_1 - 32) * 5/9`.
2. THE Calculator SHALL append the string `" °C"` to the result (e.g., `32.2222222222222 °C` for input 90).
3. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 18: Convert to Binary

**User Story:** As a student, I want to convert an integer to its binary representation, so that I can understand binary number systems and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"to_binary"` and a valid non-negative integer `number_1` is received, THE Calculator SHALL return a Binary_Representation of `number_1` using `bin(int(number_1))`.
2. THE Calculator SHALL zero-pad the binary output to exactly 8 digits (e.g., `00000010` for input 2).
3. THE Calculator SHALL NOT include the `0b` prefix in the output.
4. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 19: Convert to Hexadecimal

**User Story:** As a student, I want to convert an integer to its hexadecimal representation, so that I can understand hex number systems used in computing and practise submitting Git changes.

#### Acceptance Criteria

1. WHEN a POST request with `operation` equal to `"to_hexadecimal"` and a valid non-negative integer `number_1` is received, THE Calculator SHALL return a Hex_Representation of `number_1` using `hex(int(number_1))`.
2. THE Calculator SHALL return the hexadecimal output in UPPERCASE (e.g., `FF` for input 255).
3. THE Calculator SHALL NOT include the `0x` prefix in the output.
4. THE Calculator SHALL NOT use `number_2` in the calculation.

---

### Requirement 20: UI/UX Redesign

**User Story:** As a student, I want to use a visually appealing and stress-reducing interface, so that I can focus on learning Git without visual distractions.

#### Acceptance Criteria

1. WHILE all 19 mathematical operations are implemented, THE Calculator SHALL render a redesigned `index.html` with a minimalistic visual style.
2. THE Calculator SHALL apply a soothing colour scheme (e.g., cool tones such as blues or greens) intended to reduce visual stress.
3. THE Calculator SHALL preserve all existing form fields (`operation` selector, `number_1` input, `number_2` input, and submit button) in the redesigned layout.
4. THE Calculator SHALL display all 19 operations as selectable options in the operation dropdown.
5. THE Calculator SHALL remain functional after the UI/UX changes — all 19 operations SHALL continue to return correct results.
6. WHEN a user selects an operation that requires only one number (i.e., `sqrt`, `exponential`, `factorial`, `natural_log`, `log2`, `log10`, `celsius_to_fahrenheit`, `celsius_to_kelvin`, `fahrenheit_to_celsius`, `to_binary`, `to_hexadecimal`), THE UI SHALL hide the `number_2` input field.
7. WHEN a user selects an operation that requires two numbers (i.e., `addition`, `subtraction`, `multiplication`, `division`, `modulus`, `custom_exponential`, `custom_sqrt`, `custom_log_base`), THE UI SHALL show the `number_2` input field.
8. The show/hide behaviour SHALL occur dynamically without a page reload using JavaScript.
9. WHEN the `number_2` field is hidden, its value SHALL NOT be required for form submission.
10. THE UI SHALL be responsive and adapt its layout for mobile screen sizes (viewports below 768px wide).
11. Touch interactions (tap, scroll) SHALL work correctly on mobile devices.
12. Input fields and buttons SHALL have a minimum touch target height of 44px.
13. THE UI SHALL NOT require horizontal scrolling on standard mobile screen widths.

---

### Requirement 21: Code Structure — All Operations in application.py

**User Story:** As an instructor, I want all mathematical operation logic to reside in `application.py`, so that students encounter intentional merge conflicts during the Git teaching exercise and practise resolving them.

#### Acceptance Criteria

1. THE Calculator SHALL implement all 19 mathematical operation logic blocks directly inside `application.py`.
2. THE Calculator SHALL NOT delegate any operation logic to helper modules, utility files, or separate Python files.
3. THE Calculator SHALL NOT import operation logic from any module other than the Python standard library (e.g., `math`) and Flask.

---

### Requirement 22: Unit Tests for All Operations

**User Story:** As an instructor, I want every mathematical operation to have at least one unit test, so that students can verify their implementations are correct.

#### Acceptance Criteria

1. THE Test_Suite SHALL include at least one unit test for each of the 19 mathematical operations.
2. WHEN a unit test for an operation is executed with a known input, THE Test_Suite SHALL assert that the result equals the expected output (e.g., `addition(12, 9) == 21.0`).
3. THE Test_Suite SHALL place all new unit tests in the existing `tests/test_application.py` file.
4. THE Test_Suite SHALL use pytest as the test framework, consistent with the existing test suite.
5. THE Test_Suite SHALL NOT include integration tests or end-to-end tests of the Flask web application for the purpose of this requirement.

---

### Requirement 23: Input Validation and Error Handling

**User Story:** As a student, I want the calculator to show clear error messages for invalid inputs, so that I understand what went wrong without seeing a confusing Python stack trace.

#### Acceptance Criteria

1. IF a non-numeric value is submitted for `number_1` or `number_2`, THEN THE Calculator SHALL display a user-friendly error message in the result area (e.g., "Error: Please enter valid numbers").
2. IF a required field (`number_1` or `number_2`) is submitted as empty, THEN THE Calculator SHALL display a user-friendly error message in the result area.
3. IF `number_2` is zero and the selected operation is `"division"`, THEN THE Calculator SHALL display the error message `"Error: Cannot divide by zero"` in the result area.
4. IF a negative number is submitted as `number_1` and the selected operation is `"factorial"`, THEN THE Calculator SHALL display the error message `"Error: Factorial is not defined for negative numbers"` in the result area.
5. THE Calculator SHALL display all error messages in the same result area used for normal results.
6. THE Calculator SHALL NOT raise unhandled exceptions or expose Python stack traces to the user.
