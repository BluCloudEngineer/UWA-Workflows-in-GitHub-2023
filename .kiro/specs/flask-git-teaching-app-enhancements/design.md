# Design Document

## Flask Git Teaching App Enhancements

---

## Overview

This document describes the technical design for enhancing the "All in One Computer Science Calculator" Flask web application. The application is used as a teaching tool for Git workflows: students are intentionally assigned overlapping sections of `application.py` so they encounter and must resolve merge conflicts.

The enhancement covers:

1. Implementing 18 additional mathematical operations (bringing the total to 19) directly in `application.py`.
2. Adding input validation and error handling for all operations.
3. Redesigning the UI (`index.html` + `styles.css`) with a soothing colour scheme, mobile responsiveness, and dynamic show/hide of the second number field.
4. Expanding the test suite in `tests/test_application.py` to cover all 19 operations.

The critical design constraint is intentional: all operation logic must live inside the single `calculate()` function in `application.py`. No helper modules or utility files are to be created. This maximises the likelihood of Git merge conflicts between students working on different branches.

---

## Architecture

The application follows a minimal Flask MVC-style pattern:

```
Browser
  │
  │  GET /           → renders index.html (blank result)
  │  GET /calculate  → renders index.html (blank result, redirect)
  │  POST /calculate → validates input, computes result, renders index.html with result
  │
Flask Application (application.py)
  │
  ├── route: /               → index()
  ├── route: /calculate GET  → calculate_redirect()
  └── route: /calculate POST → calculate()
        ├── Input validation (try/except, explicit checks)
        ├── Operation dispatch (sequence of independent if statements)
        └── Result formatting (string assembly)
  │
Jinja2 Template (templates/index.html)
  ├── Operation <select> dropdown (19 options)
  ├── number_1 <input>
  ├── number_2 <input> (shown/hidden via JS)
  ├── Submit button
  └── Result display area ({{ result }})
  │
Static Assets (static/styles.css)
  └── Responsive layout, soothing colour scheme, 44px touch targets
```

There is no database, no session state, and no client-side computation. Every calculation round-trips through the Flask server.

---

## Components and Interfaces

### 1. `application.py` — Flask Application

**Routes:**

| Method | Path | Handler | Description |
|--------|------|---------|-------------|
| GET | `/` | `index()` | Renders blank calculator page |
| GET | `/calculate` | `calculate_redirect()` | Renders blank calculator page |
| POST | `/calculate` | `calculate()` | Validates input, computes result, renders result page |

**`calculate()` function contract:**

- Reads `operation`, `number_1`, `number_2` from `request.form`
- Validates that `number_1` and `number_2` are parseable as floats (returns error string on failure)
- Validates operation-specific constraints (e.g., division by zero, negative factorial input)
- Dispatches to the correct `if` block
- Returns `render_template("index.html", result=result)` where `result` is a string

**Operation dispatch structure (sequence of independent `if` statements):**

```python
result = None

if operation == "addition":
    ...
if operation == "celsius_to_fahrenheit":
    ...
if operation == "celsius_to_kelvin":
    ...
if operation == "custom_exponential":
    ...
if operation == "custom_log_base":
    ...
if operation == "custom_sqrt":
    ...
if operation == "division":
    ...
if operation == "exponential":
    ...
if operation == "factorial":
    ...
if operation == "fahrenheit_to_celsius":
    ...
if operation == "log10":
    ...
if operation == "log2":
    ...
if operation == "modulus":
    ...
if operation == "multiplication":
    ...
if operation == "natural_log":
    ...
if operation == "sqrt":
    ...
if operation == "subtraction":
    ...
if operation == "to_binary":
    ...
if operation == "to_hexadecimal":
    ...
```

`result` is initialised to `None` before the block; each independent `if` overwrites it when its operation matches. This structure is intentional — each block is a completely self-contained addition, so students adding different operations on different branches will not conflict on control-flow keywords (`elif`). It also makes the intent of each block crystal clear.

**Imports (unchanged from original):**

```python
from flask import Flask, render_template, request
import math
```

No new imports are required beyond `math` and the Flask components already in use.

### 2. `templates/index.html` — Frontend Template

**Key elements:**

- `<select id="operation" name="operation">` — 19 `<option>` elements, ordered by display label
- `<input type="number" id="number1" name="number_1" required>` — always visible
- `<div id="number2-group">` wrapping the `number_2` label and input — shown/hidden by JS
- `<input type="number" id="number2" name="number_2">` — `required` attribute toggled by JS
- `<button type="submit">` — minimum 44px height
- `<div id="result">Result: {{ result }}</div>` — displays result or empty when no result

**JavaScript — show/hide logic:**

A small inline `<script>` block handles the show/hide behaviour. No external JS libraries are required.

```javascript
const singleArgOps = [
  "sqrt", "exponential", "factorial", "natural_log",
  "log2", "log10", "celsius_to_fahrenheit",
  "celsius_to_kelvin", "fahrenheit_to_celsius",
  "to_binary", "to_hexadecimal"
];

function updateNumber2Visibility() {
  const op = document.getElementById("operation").value;
  const group = document.getElementById("number2-group");
  const input = document.getElementById("number2");
  if (singleArgOps.includes(op)) {
    group.style.display = "none";
    input.removeAttribute("required");
  } else {
    group.style.display = "block";
    input.setAttribute("required", "required");
  }
}

document.getElementById("operation").addEventListener("change", updateNumber2Visibility);
window.addEventListener("DOMContentLoaded", updateNumber2Visibility);
```

This runs on page load (to set the initial state) and on every `change` event of the `<select>`.

### 3. `static/styles.css` — Styles

**Design principles:**

- Soothing cool-tone palette (blues/teals) to reduce visual stress
- Minimal shadows and rounded corners
- Fluid layout using percentage widths with a `max-width` container
- Media query breakpoint at 768px for mobile adaptation
- All interactive elements (`input`, `select`, `button`) have `min-height: 44px` for touch accessibility

**Colour palette:**

| Role | Value |
|------|-------|
| Page background | `#eef3f7` (very light cool grey-blue) |
| Card background | `#ffffff` |
| Primary accent | `#3b82c4` (medium blue) |
| Primary accent hover | `#2d6aa3` |
| Text primary | `#2c3e50` (dark slate) |
| Text secondary | `#5a6a7a` |
| Border | `#c9d8e8` |
| Result background | `#f0f7ff` (pale blue tint) |
| Error text | `#c0392b` |

---

## Data Models

There is no persistent data model. All data is ephemeral per HTTP request.

**Request payload (form data):**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `operation` | `str` | Yes | One of the 19 operation identifiers |
| `number_1` | `str` (parsed to `float`) | Yes | Primary numeric input |
| `number_2` | `str` (parsed to `float`) | No* | Secondary numeric input; absent/empty for single-argument operations |

*`number_2` is optional in the HTTP sense when hidden. The server-side validator must handle its absence gracefully.

**Result value:**

The `result` variable passed to the Jinja2 template is always a `str` or `None`. The template renders it as-is in the result area. Possible formats:

| Category | Example |
|----------|---------|
| Plain numeric | `"21.0"` |
| ± prefix | `"± 12.0"` |
| Unit suffix | `"86.0 °F"`, `"298.15 K"`, `"32.222... °C"` |
| Binary | `"00000010"` |
| Hexadecimal | `"FF"` |
| Error | `"Error: Cannot divide by zero"` |

**Input validation flow:**

```
1. Try to parse number_1 as float
   └── ValueError → result = "Error: Please enter valid numbers"; return early

2. If operation requires number_2:
   a. Check number_2 is present and non-empty
      └── Missing/empty → result = "Error: Please enter valid numbers"; return early
   b. Try to parse number_2 as float
      └── ValueError → result = "Error: Please enter valid numbers"; return early

3. Operation-specific checks:
   - division: if number_2 == 0 → "Error: Cannot divide by zero"
   - factorial: if number_1 < 0 → "Error: Factorial is not defined for negative numbers"

4. Compute result
```

The list of operations requiring `number_2` (for step 2):

```python
REQUIRES_TWO_NUMBERS = {
    "addition", "subtraction", "multiplication", "division",
    "modulus", "custom_exponential", "custom_sqrt", "custom_log_base"
}
```

This constant informs the validation logic and mirrors the JavaScript `singleArgOps` array (as its complement).

---

## Correctness Properties

*A property is a characteristic or behaviour that should hold true across all valid executions of a system — essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Arithmetic operations are mathematically correct

*For any* two floats `a` and `b`, the Calculator's arithmetic operations (addition, subtraction, multiplication, division, modulus, custom exponential) SHALL return the same value as the corresponding Python operator applied to those inputs.

**Validates: Requirements 1.1, 2.1, 3.1, 4.1, 5.1, 7.1**

### Property 2: Division by zero always returns an error

*For any* value of `number_1`, when `number_2` is zero and the operation is `"division"`, the Calculator SHALL return a result string containing `"Error"`.

**Validates: Requirements 4.3, 23.3**

### Property 3: Single-argument math functions are correct

*For any* valid positive float `x`, the Calculator's single-argument operations (`exponential`, `sqrt`, `natural_log`, `log2`, `log10`) SHALL return results numerically equal to the corresponding `math` module function applied to `x`.

**Validates: Requirements 6.1, 8.1, 10.1, 11.1, 12.1**

### Property 4: Square root result carries ± prefix

*For any* non-negative float `x`, when the operation is `"sqrt"`, the result string SHALL begin with `"± "`.

**Validates: Requirements 8.2**

### Property 5: Custom square root ± prefix depends on even/odd root degree

*For any* positive float `x` and non-zero integer `n`, when the operation is `"custom_sqrt"`:
- if `n` is divisible by 2, the result SHALL begin with `"± "`;
- if `n` is NOT divisible by 2, the result SHALL NOT begin with `"± "`.

**Validates: Requirements 9.2, 9.3**

### Property 6: Factorial of non-negative integers is correct

*For any* non-negative integer `n`, the Calculator's `"factorial"` operation SHALL return a result numerically equal to `float(math.factorial(n))`.

**Validates: Requirements 14.1, 14.2**

### Property 7: Factorial of negative numbers always returns an error

*For any* negative float `x`, when the operation is `"factorial"`, the Calculator SHALL return a result string containing `"Error"`.

**Validates: Requirements 23.4**

### Property 8: Temperature conversions are correct

*For any* float `t`, the Calculator's temperature conversion operations SHALL return results numerically equal to their defining formulas:
- `celsius_to_fahrenheit`: `(t * 9/5) + 32`
- `celsius_to_kelvin`: `t + 273.15`
- `fahrenheit_to_celsius`: `(t - 32) * 5/9`

**Validates: Requirements 15.1, 16.1, 17.1**

### Property 9: Temperature results include correct unit suffix

*For any* float `t`, the Calculator's temperature conversion results SHALL end with the correct unit string:
- `celsius_to_fahrenheit` results end with `" °F"`
- `celsius_to_kelvin` results end with `" K"`
- `fahrenheit_to_celsius` results end with `" °C"`

**Validates: Requirements 15.2, 16.2, 17.2**

### Property 10: Binary conversion produces valid 8-digit zero-padded string

*For any* non-negative integer `n` (0–255), the Calculator's `"to_binary"` operation SHALL return a string of exactly 8 characters containing only `'0'` and `'1'` characters, equal to `bin(n)[2:].zfill(8)`.

**Validates: Requirements 18.1, 18.2, 18.3**

### Property 11: Hexadecimal conversion produces correct uppercase string without prefix

*For any* non-negative integer `n`, the Calculator's `"to_hexadecimal"` operation SHALL return a string equal to `hex(n)[2:].upper()`, containing no `'0x'` prefix and only uppercase hexadecimal characters.

**Validates: Requirements 19.1, 19.2, 19.3**

### Property 12: Non-numeric inputs always return an error

*For any* string that cannot be parsed as a float, when submitted as `number_1` or `number_2`, the Calculator SHALL return a result string containing `"Error"`.

**Validates: Requirements 23.1, 23.2, 23.6**

---

## Error Handling

All error handling occurs inside the `calculate()` route handler. The application follows a "fail fast with a friendly message" pattern.

### Validation sequence

```python
@application.route("/calculate", methods=["POST"])
def calculate():
    result = None
    operation = request.form.get("operation", "")

    # Step 1 — parse number_1
    try:
        number_1 = float(request.form.get("number_1", ""))
    except (ValueError, TypeError):
        return render_template("index.html",
                               result="Error: Please enter valid numbers")

    # Step 2 — parse number_2 only when required
    REQUIRES_TWO = {"addition", "subtraction", "multiplication", "division",
                    "modulus", "custom_exponential", "custom_sqrt", "custom_log_base"}
    number_2 = None
    if operation in REQUIRES_TWO:
        try:
            number_2 = float(request.form.get("number_2", ""))
        except (ValueError, TypeError):
            return render_template("index.html",
                                   result="Error: Please enter valid numbers")

    # Step 3 — operation-specific guards
    if operation == "division" and number_2 == 0:
        return render_template("index.html",
                               result="Error: Cannot divide by zero")
    if operation == "factorial" and number_1 < 0:
        return render_template("index.html",
                               result="Error: Factorial is not defined for negative numbers")

    # Step 4 — dispatch
    if operation == "addition":
        result = number_1 + number_2
    if operation == "celsius_to_fahrenheit":
        ...
```

### Error message catalogue

| Condition | Message |
|-----------|---------|
| Non-numeric `number_1` or `number_2` | `"Error: Please enter valid numbers"` |
| Empty required field | `"Error: Please enter valid numbers"` |
| Division by zero | `"Error: Cannot divide by zero"` |
| Negative factorial input | `"Error: Factorial is not defined for negative numbers"` |

No unhandled exceptions reach the user. The `try/except` around float parsing catches all `ValueError` and `TypeError` cases. No additional error types are expected given the constrained input model.

---

## Testing Strategy

### Overview

The test suite lives in `tests/test_application.py` and uses **pytest** as the test runner. Tests make HTTP POST requests via Flask's built-in test client — consistent with the existing test style in the repository.

Because the application logic is pure request-response (inputs → computed string output) with no external I/O, property-based testing is well-suited for validating all 19 operations. **Hypothesis** is the chosen property-based testing library for Python.

### Dual testing approach

- **Unit/example tests** — cover specific known values (the existing `test_addition_1` pattern). At least one example test per operation to demonstrate expected output for a concrete input.
- **Property tests** — cover the universal correctness properties defined above, generating hundreds of inputs automatically.

### Property-based testing setup

Install Hypothesis (add to `requirements.txt`):

```
hypothesis==6.131.20
```

Each property test is tagged with a comment referencing its design property:

```python
# Feature: flask-git-teaching-app-enhancements, Property 1: Arithmetic operations are mathematically correct
```

Hypothesis is configured with `@settings(max_examples=100)` per test (the default is 100; making it explicit documents the intent).

### Test file structure

```
tests/test_application.py
│
├── Existing tests (unchanged)
│   ├── test_addition_1()
│   ├── test_addition_2()
│   ├── test_default_route()
│   └── test_get_calculate_redirect()
│
├── Example tests (one per operation)
│   ├── test_subtraction_example()            → 16 - 9 = 7.0
│   ├── test_multiplication_example()         → 12 × 20 = 240.0
│   ├── test_division_example()               → 100 / 25 = 4.0
│   ├── test_modulus_example()                → 100 % 23 = 8.0
│   ├── test_exponential_example()            → e^3 ≈ 20.0855...
│   ├── test_custom_exponential_example()     → 3^4 = 81.0
│   ├── test_sqrt_example()                   → √144 → "± 12.0"
│   ├── test_custom_sqrt_even_example()       → 81^(1/4) → "± 3.0"
│   ├── test_custom_sqrt_odd_example()        → 27^(1/3) → "3.0"
│   ├── test_natural_log_example()            → ln(543) ≈ 6.2971...
│   ├── test_log2_example()                   → log2(128) = 7.0
│   ├── test_log10_example()                  → log10(1000) = 3.0
│   ├── test_custom_log_base_example()        → log4(16) = 2.0
│   ├── test_factorial_example()              → 5! = 120.0
│   ├── test_celsius_to_fahrenheit_example()  → 30°C = 86.0 °F
│   ├── test_celsius_to_kelvin_example()      → 25°C = 298.15 K
│   ├── test_fahrenheit_to_celsius_example()  → 90°F ≈ 32.222 °C
│   ├── test_to_binary_example()              → 2 → "00000010"
│   └── test_to_hexadecimal_example()         → 255 → "FF"
│
├── Error/edge case tests
│   ├── test_division_by_zero()
│   ├── test_factorial_negative()
│   └── test_invalid_input_non_numeric()
│
└── Property tests (Hypothesis)
    ├── test_property_arithmetic_correct()        → Property 1
    ├── test_property_division_by_zero_error()    → Property 2
    ├── test_property_single_arg_math()           → Property 3
    ├── test_property_sqrt_prefix()               → Property 4
    ├── test_property_custom_sqrt_prefix()        → Property 5
    ├── test_property_factorial_correct()         → Property 6
    ├── test_property_factorial_negative_error()  → Property 7
    ├── test_property_temperature_values()        → Property 8
    ├── test_property_temperature_suffixes()      → Property 9
    ├── test_property_binary_format()             → Property 10
    ├── test_property_hex_format()                → Property 11
    └── test_property_invalid_input_error()       → Property 12
```

### Property test examples

```python
from hypothesis import given, settings
from hypothesis import strategies as st

# Feature: flask-git-teaching-app-enhancements, Property 1: Arithmetic operations are mathematically correct
@given(a=st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False),
       b=st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False))
@settings(max_examples=100)
def test_property_arithmetic_correct(a, b):
    for op, expected_fn in [
        ("addition",       lambda x, y: x + y),
        ("subtraction",    lambda x, y: x - y),
        ("multiplication", lambda x, y: x * y),
    ]:
        response = application.test_client().post("/calculate", data={
            "operation": op, "number_1": a, "number_2": b
        })
        assert response.status_code == 200
        expected = str(expected_fn(a, b))
        assert expected.encode() in response.data


# Feature: flask-git-teaching-app-enhancements, Property 10: Binary conversion produces valid 8-digit zero-padded string
@given(n=st.integers(min_value=0, max_value=255))
@settings(max_examples=100)
def test_property_binary_format(n):
    response = application.test_client().post("/calculate", data={
        "operation": "to_binary", "number_1": n, "number_2": 0
    })
    assert response.status_code == 200
    expected = bin(n)[2:].zfill(8)
    assert expected.encode() in response.data
    assert len(expected) == 8
    assert all(c in "01" for c in expected)
```

### Running tests

```bash
# From the project root
pytest tests/test_application.py -v

# Or for a quick single-pass (no watch mode)
pytest tests/test_application.py --tb=short
```

No test fixtures or `conftest.py` are required — the Flask test client is instantiated directly in each test, consistent with the existing test style.
