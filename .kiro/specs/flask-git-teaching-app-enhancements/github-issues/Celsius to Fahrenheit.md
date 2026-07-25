# Celsius to Fahrenheit

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will convert the value (in degrees Celsius) to degrees Fahrenheit.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "celsius_to_fahrenheit",
    "number_1": 30,  # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 86.0 °F
```

**NOTE: The output must include °F at the end of the result**

## Additional Notes

Not applicable
