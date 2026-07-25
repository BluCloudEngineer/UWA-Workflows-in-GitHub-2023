# Log10

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will calculate the log base 10 of the value.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "log10",
    "number_1": 1000, # Key and value required
    "number_2": None  # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 3.0
```

## Additional Notes

Not applicable
