# Exponential

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will calculate the value of e raised to that power. In other words, we are solving for y in the equation below:

```text
y = e^x
```

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "exponential",
    "number_1": 3,   # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 20.0855369231877
```

## Additional Notes

Not applicable
