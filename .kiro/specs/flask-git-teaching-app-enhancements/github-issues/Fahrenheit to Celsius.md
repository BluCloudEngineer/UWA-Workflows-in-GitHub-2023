# Fahrenheit to Celsius

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will convert the value (in degrees Fahrenheit) to degrees Celsius.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "fahrenheit_to_celsius",
    "number_1": 90,  # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 32.2222222222222 °C
```

**NOTE: The output must include °C at the end of the result**

## Additional Notes

Not applicable
