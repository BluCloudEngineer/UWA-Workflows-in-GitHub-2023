# Natural Log

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will calculate the natural log (ln) of the value.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "natural_log",
    "number_1": 543, # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 6.29710931993394
```

## Additional Notes

Not applicable
