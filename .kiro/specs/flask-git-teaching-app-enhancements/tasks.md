# Implementation Plan: Flask Git Teaching App Enhancements

## Overview

Implement 18 additional calculator operations in `application.py`, add input validation and error handling, redesign the UI in `index.html` and `styles.css`, and expand the test suite in `tests/test_application.py`. All operation logic stays inside the single `calculate()` function in `application.py` — no helper modules.

The implementation language is **Python** (Flask application).

---

## Tasks

- [ ] 1. Add input validation and error handling to `application.py`
  - [ ] 1.1 Replace the existing `calculate()` function body with the validated dispatch skeleton
    - Parse `number_1` with `try/except (ValueError, TypeError)` and return `"Error: Please enter valid numbers"` on failure
    - Define `REQUIRES_TWO = {"addition", "subtraction", "multiplication", "division", "modulus", "custom_exponential", "custom_sqrt", "custom_log_base"}` inside the function
    - Parse `number_2` only when `operation in REQUIRES_TWO`, returning the same error on failure
    - Add operation-specific guards: division-by-zero → `"Error: Cannot divide by zero"`, negative factorial → `"Error: Factorial is not defined for negative numbers"`
    - Keep the existing `if operation == "addition"` block intact
    - _Requirements: 4.3, 23.1, 23.2, 23.3, 23.4, 23.5, 23.6_

  - [ ]* 1.2 Write property test for non-numeric input error (Property 12)
    - **Property 12: Non-numeric inputs always return an error**
    - **Validates: Requirements 23.1, 23.2, 23.6**

  - [ ]* 1.3 Write property test for division-by-zero error (Property 2)
    - **Property 2: Division by zero always returns an error**
    - **Validates: Requirements 4.3, 23.3**

- [ ] 2. Implement arithmetic and power operations in `application.py`
  - [ ] 2.1 Add subtraction, multiplication, division, modulus, custom exponential, and custom square root `if` blocks
    - `subtraction`: `result = number_1 - number_2`
    - `multiplication`: `result = float(number_1 * number_2)`
    - `division`: `result = number_1 / number_2` (guard already in place)
    - `modulus`: `result = float(number_1 % number_2)`
    - `custom_exponential`: `result = float(number_1 ** number_2)`
    - `custom_sqrt`: `result = number_1 ** (1 / number_2)`; prefix `"± "` when `int(number_2) % 2 == 0`, otherwise no prefix
    - _Requirements: 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1, 5.2, 7.1, 7.2, 9.1, 9.2, 9.3_

  - [ ]* 2.2 Write property test for arithmetic correctness (Property 1)
    - **Property 1: Arithmetic operations are mathematically correct**
    - **Validates: Requirements 1.1, 2.1, 3.1, 4.1, 5.1, 7.1**

  - [ ]* 2.3 Write property test for custom square root ± prefix (Property 5)
    - **Property 5: Custom square root ± prefix depends on even/odd root degree**
    - **Validates: Requirements 9.2, 9.3**

- [ ] 3. Implement single-argument math operations in `application.py`
  - [ ] 3.1 Add `exponential`, `sqrt`, `natural_log`, `log2`, `log10`, `custom_log_base`, and `factorial` `if` blocks
    - `exponential`: `result = math.exp(number_1)`
    - `sqrt`: `result = "± " + str(math.sqrt(number_1))`
    - `natural_log`: `result = math.log(number_1)`
    - `log2`: `result = float(math.log2(number_1))`
    - `log10`: `result = float(math.log10(number_1))`
    - `custom_log_base`: `result = float(math.log(number_1, number_2))`
    - `factorial`: `result = float(math.factorial(int(number_1)))` (guard already in place)
    - _Requirements: 6.1, 6.2, 6.3, 8.1, 8.2, 8.3, 10.1, 10.2, 10.3, 11.1, 11.2, 11.3, 12.1, 12.2, 13.1, 13.2, 14.1, 14.2, 14.3_

  - [ ]* 3.2 Write property test for single-argument math correctness (Property 3)
    - **Property 3: Single-argument math functions are correct**
    - **Validates: Requirements 6.1, 8.1, 10.1, 11.1, 12.1**

  - [ ]* 3.3 Write property test for sqrt ± prefix (Property 4)
    - **Property 4: Square root result carries ± prefix**
    - **Validates: Requirements 8.2**

  - [ ]* 3.4 Write property test for factorial correctness and negative-input error (Properties 6 and 7)
    - **Property 6: Factorial of non-negative integers is correct**
    - **Property 7: Factorial of negative numbers always returns an error**
    - **Validates: Requirements 14.1, 14.2, 23.4**

- [ ] 4. Implement temperature conversion and number base operations in `application.py`
  - [ ] 4.1 Add `celsius_to_fahrenheit`, `celsius_to_kelvin`, `fahrenheit_to_celsius`, `to_binary`, and `to_hexadecimal` `if` blocks
    - `celsius_to_fahrenheit`: `result = str((number_1 * 9/5) + 32) + " °F"`
    - `celsius_to_kelvin`: `result = str(number_1 + 273.15) + " K"`
    - `fahrenheit_to_celsius`: `result = str((number_1 - 32) * 5/9) + " °C"`
    - `to_binary`: `result = bin(int(number_1))[2:].zfill(8)`
    - `to_hexadecimal`: `result = hex(int(number_1))[2:].upper()`
    - _Requirements: 15.1, 15.2, 15.3, 16.1, 16.2, 16.3, 16.4, 17.1, 17.2, 17.3, 18.1, 18.2, 18.3, 18.4, 19.1, 19.2, 19.3, 19.4, 21.1, 21.2, 21.3_

  - [ ]* 4.2 Write property test for temperature conversion values (Property 8)
    - **Property 8: Temperature conversions are correct**
    - **Validates: Requirements 15.1, 16.1, 17.1**

  - [ ]* 4.3 Write property test for temperature unit suffixes (Property 9)
    - **Property 9: Temperature results include correct unit suffix**
    - **Validates: Requirements 15.2, 16.2, 17.2**

  - [ ]* 4.4 Write property test for binary format (Property 10)
    - **Property 10: Binary conversion produces valid 8-digit zero-padded string**
    - **Validates: Requirements 18.1, 18.2, 18.3**

  - [ ]* 4.5 Write property test for hexadecimal format (Property 11)
    - **Property 11: Hexadecimal conversion produces correct uppercase string without prefix**
    - **Validates: Requirements 19.1, 19.2, 19.3**

- [ ] 5. Checkpoint — Ensure all tests pass
  - Ensure all tests pass with `pytest tests/test_application.py -v`. Ask the user if any questions arise.

- [ ] 6. Add example unit tests for all 18 new operations to `tests/test_application.py`
  - [ ] 6.1 Write example tests for arithmetic and power operations
    - `test_subtraction_example`: 16 − 9 → `"7.0"`
    - `test_multiplication_example`: 12 × 20 → `"240.0"`
    - `test_division_example`: 100 / 25 → `"4.0"`
    - `test_modulus_example`: 100 % 23 → `"8.0"`
    - `test_custom_exponential_example`: 3^4 → `"81.0"`
    - `test_custom_sqrt_even_example`: 81^(1/4) → `"± 3.0"`
    - `test_custom_sqrt_odd_example`: 27^(1/3) → `"3.0"`
    - _Requirements: 2.1, 3.1, 4.1, 5.1, 7.1, 9.1, 9.2, 9.3, 22.1, 22.2, 22.3, 22.4_

  - [ ] 6.2 Write example tests for single-argument math operations
    - `test_exponential_example`: e^3 → `"20.0855369231877"` (substring match)
    - `test_sqrt_example`: √144 → `"± 12.0"`
    - `test_natural_log_example`: ln(543) → `"6.29710931993394"` (substring match)
    - `test_log2_example`: log2(128) → `"7.0"`
    - `test_log10_example`: log10(1000) → `"3.0"`
    - `test_custom_log_base_example`: log4(16) → `"2.0"`
    - `test_factorial_example`: 5! → `"120.0"`
    - _Requirements: 6.1, 6.3, 8.1, 8.2, 10.1, 10.2, 11.1, 11.2, 12.1, 12.2, 13.1, 13.2, 14.1, 14.2, 22.1, 22.2, 22.3, 22.4_

  - [ ] 6.3 Write example tests for temperature conversions and base operations
    - `test_celsius_to_fahrenheit_example`: 30 → `"86.0 °F"`
    - `test_celsius_to_kelvin_example`: 25 → `"298.15 K"`
    - `test_fahrenheit_to_celsius_example`: 90 → `"32.222"` (substring match)
    - `test_to_binary_example`: 2 → `"00000010"`
    - `test_to_hexadecimal_example`: 255 → `"FF"`
    - _Requirements: 15.1, 15.2, 16.1, 16.2, 17.1, 17.2, 18.1, 18.2, 19.1, 19.2, 22.1, 22.2, 22.3, 22.4_

  - [ ] 6.4 Write error-condition tests
    - `test_division_by_zero`: POST division with `number_2=0` → response contains `"Error: Cannot divide by zero"`
    - `test_factorial_negative`: POST factorial with `number_1=-1` → response contains `"Error: Factorial is not defined for negative numbers"`
    - `test_invalid_input_non_numeric`: POST addition with `number_1="abc"` → response contains `"Error: Please enter valid numbers"`
    - _Requirements: 4.3, 14.1, 23.1, 23.3, 23.4, 23.6_

- [ ] 7. Add Hypothesis property tests to `tests/test_application.py`
  - [ ] 7.1 Add `hypothesis` to `requirements.txt` and write `test_property_arithmetic_correct` (Property 1)
    - Add `hypothesis==6.131.20` to `requirements.txt`
    - Use `@given(st.floats(...), st.floats(...))` for addition, subtraction, multiplication
    - _Requirements: 1.1, 2.1, 3.1_

  - [ ]* 7.2 Write `test_property_division_by_zero_error` (Property 2)
    - **Property 2: Division by zero always returns an error**
    - Use `@given(st.floats(...))` for `number_1`; fix `number_2=0`
    - **Validates: Requirements 4.3, 23.3**

  - [ ]* 7.3 Write `test_property_single_arg_math` (Property 3)
    - **Property 3: Single-argument math functions are correct**
    - Use `@given(st.floats(min_value=0.001, ...))` for `x`
    - Check `exponential`, `sqrt`, `natural_log`, `log2`, `log10`
    - **Validates: Requirements 6.1, 8.1, 10.1, 11.1, 12.1**

  - [ ]* 7.4 Write `test_property_sqrt_prefix` (Property 4)
    - **Property 4: Square root result carries ± prefix**
    - Use `@given(st.floats(min_value=0, ...))` for `x`
    - **Validates: Requirements 8.2**

  - [ ]* 7.5 Write `test_property_custom_sqrt_prefix` (Property 5)
    - **Property 5: Custom square root ± prefix depends on even/odd root degree**
    - Use `@given(st.floats(min_value=0.001,...), st.integers(min_value=1, max_value=10))`
    - **Validates: Requirements 9.2, 9.3**

  - [ ]* 7.6 Write `test_property_factorial_correct` (Property 6) and `test_property_factorial_negative_error` (Property 7)
    - **Property 6: Factorial of non-negative integers is correct**
    - **Property 7: Factorial of negative numbers always returns an error**
    - Use `@given(st.integers(min_value=0, max_value=12))` for Property 6
    - Use `@given(st.floats(max_value=-0.001, ...))` for Property 7
    - **Validates: Requirements 14.1, 14.2, 23.4**

  - [ ]* 7.7 Write `test_property_temperature_values` (Property 8) and `test_property_temperature_suffixes` (Property 9)
    - **Property 8: Temperature conversions are correct**
    - **Property 9: Temperature results include correct unit suffix**
    - Use `@given(st.floats(min_value=-1e4, max_value=1e4, ...))`
    - **Validates: Requirements 15.1, 15.2, 16.1, 16.2, 17.1, 17.2**

  - [ ]* 7.8 Write `test_property_binary_format` (Property 10)
    - **Property 10: Binary conversion produces valid 8-digit zero-padded string**
    - Use `@given(st.integers(min_value=0, max_value=255))`
    - **Validates: Requirements 18.1, 18.2, 18.3**

  - [ ]* 7.9 Write `test_property_hex_format` (Property 11)
    - **Property 11: Hexadecimal conversion produces correct uppercase string without prefix**
    - Use `@given(st.integers(min_value=0, max_value=65535))`
    - **Validates: Requirements 19.1, 19.2, 19.3**

  - [ ]* 7.10 Write `test_property_invalid_input_error` (Property 12)
    - **Property 12: Non-numeric inputs always return an error**
    - Use `@given(st.text())` filtered to exclude float-parseable strings
    - **Validates: Requirements 23.1, 23.2, 23.6**

- [ ] 8. Checkpoint — Ensure all tests pass
  - Ensure all tests pass with `pytest tests/test_application.py -v`. Ask the user if any questions arise.

- [ ] 9. Redesign `templates/index.html`
  - [ ] 9.1 Rewrite `index.html` with updated structure and JavaScript show/hide logic
    - Replace `<input type="text">` inputs with `<input type="number">`
    - Wrap the `number_2` label and input in `<div id="number2-group">`
    - Add the JavaScript `singleArgOps` array and `updateNumber2Visibility()` function (inline `<script>`)
    - Bind the function to `DOMContentLoaded` and to the `change` event of `#operation`
    - Toggle the `required` attribute alongside `display` style
    - Ensure the result area is `<div id="result">Result: {{ result }}</div>`
    - _Requirements: 20.1, 20.3, 20.4, 20.5, 20.6, 20.7, 20.8, 20.9_

- [ ] 10. Redesign `static/styles.css`
  - [ ] 10.1 Rewrite `styles.css` with soothing colour palette, responsive layout, and touch targets
    - Apply the colour palette from the design: background `#eef3f7`, card `#ffffff`, accent `#3b82c4`, text `#2c3e50`, border `#c9d8e8`, result background `#f0f7ff`, error `#c0392b`
    - Use a fluid `max-width` container centred on the page
    - Set `min-height: 44px` on all `input`, `select`, and `button` elements
    - Add `@media (max-width: 768px)` breakpoint to ensure single-column layout with no horizontal scrolling
    - _Requirements: 20.2, 20.10, 20.11, 20.12, 20.13_

- [ ] 11. Final checkpoint — Ensure all tests pass
  - Ensure all tests pass with `pytest tests/test_application.py -v`. Ask the user if any questions arise.

---

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP
- Each task references specific requirements for traceability
- All operation `if` blocks in `application.py` must remain independent (no `elif`) to maximise Git merge conflicts between students
- Hypothesis must be added to `requirements.txt` before property tests can run
- Property tests validate universal correctness properties; example tests validate specific known values

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["1.2", "1.3", "2.1"] },
    { "id": 2, "tasks": ["2.2", "2.3", "3.1"] },
    { "id": 3, "tasks": ["3.2", "3.3", "3.4", "4.1"] },
    { "id": 4, "tasks": ["4.2", "4.3", "4.4", "4.5", "6.1", "6.2", "6.3", "6.4"] },
    { "id": 5, "tasks": ["7.1", "9.1", "10.1"] },
    { "id": 6, "tasks": ["7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9", "7.10"] }
  ]
}
```
