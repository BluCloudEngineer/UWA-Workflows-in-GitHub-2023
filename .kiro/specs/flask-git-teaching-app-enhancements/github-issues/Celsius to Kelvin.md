# Celsius to Kelvin

## Describe the New Feature

I want to add logic to the calculator application so that when one number is provided, it will convert the value (in degrees Celsius) to Kelvin.

For example, if the following POST data is sent to the application:

```python
data = {
    "operation": "celsius_to_kelvin",
    "number_1": 25,  # Key and value required
    "number_2": None # Key must be supplied but its value is not used
}
```

The result will be:

```text
Result: 298.15 K
```

**NOTE: The output must NOT include a degrees sign (°) at the end of the result**

## Additional Notes

Not applicable
