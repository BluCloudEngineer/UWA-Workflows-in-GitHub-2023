# Convert to Binary

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will convert an integer value to binary.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "to_binary",
    "number_1": 2,   # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 00000010
```

**NOTE: The output must be padded to eight digits**

## Additional Notes

Not applicable
