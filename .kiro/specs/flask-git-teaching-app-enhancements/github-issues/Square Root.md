# Square Root

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will calculate the square root of the value.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "sqrt",
    "number_1": 144, # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: ± 12.0
```

**NOTE: You MUST include the plus-minus sign (±) in the output**

## Additional Notes

Not applicable
