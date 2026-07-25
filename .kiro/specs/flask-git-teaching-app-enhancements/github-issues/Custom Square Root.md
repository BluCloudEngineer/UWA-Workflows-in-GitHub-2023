# Custom Square Root

## Describe the New Feature

I want to add logic to the calculator application so that when two numbers are provided, it will calculate the root of a custom base.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "custom_sqrt",
    "number_1": 27, # Key and value required
    "number_2": 3   # Key and value required
}
```

The result will be:

```text
Result: 3.0
```

**NOTE: If the second number is divisible by 2, you MUST include the plus-minus sign (±) in the output**

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "custom_sqrt",
    "number_1": 81, # Key and value required
    "number_2": 4   # Key and value required
}
```

The result will be:

```text
Result: ± 3.0
```

## Additional Notes

Not applicable
