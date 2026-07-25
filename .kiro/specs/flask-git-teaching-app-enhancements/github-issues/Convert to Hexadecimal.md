# Convert to Hexadecimal

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will convert an integer value to hexadecimal.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "to_hexadecimal",
    "number_1": 255, # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: FF
```

**NOTE: The output must be in UPPERCASE**

## Additional Notes

Not applicable
