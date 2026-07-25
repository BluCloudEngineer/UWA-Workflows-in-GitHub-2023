# Log2

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will calculate the log base 2 of the value.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "log2",
    "number_1": 128, # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 7.0
```

## Additional Notes

Not applicable
