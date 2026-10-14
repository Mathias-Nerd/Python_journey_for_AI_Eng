def celsius_to_fahrenheit(celsius):
    return round(celsius * ( 9 / 5 ) + 32, 2)


def fahrenheit_to_celsius(fahrenheit):
    return round( ( fahrenheit - 32 ) * ( 5 / 9 ) , 2)


def celsius_to_kelvin(celsius):
    return round( celsius + 273.15, 2)


def convert_temperature(value, from_unit, to_unit):
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise ValueError("Units must be strings")
    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()
    lower = {
        "celsius": -273.15,
        "fahrenheit" : -459.67,
        "kelvin" : 0
    }
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError("value should be a number")
    elif to_unit not in lower.keys() or from_unit not in lower.keys():
        raise ValueError("Unsuported unit")
    elif value < lower[from_unit]:
        raise ValueError("Below absolute")

    match (from_unit, to_unit):
        case ("celsius", "fahrenheit"):
            return celsius_to_fahrenheit(value)
        case ("celsius", "kelvin"):
            return celsius_to_kelvin(value)
        case ("fahrenheit", "celsius"):
            return fahrenheit_to_celsius(value)
        case ("fahrenheit", "kelvin"):
            return celsius_to_kelvin(fahrenheit_to_celsius(value))
        case ("kelvin", "celsius"):
            return round(value - 273.15, 2)
        case ("kelvin", "fahrenheit"):
            return   (celsius_to_fahrenheit(value - 273.15))

    return value


"""
Celsius to Kelvin: K = C + 273.15
Kelvin to Celcius: C = K - 273.15
Fahrenheit to Celcius: C = (F-32) (5/9)
Celsius to Fahrenheit: F = C(9/5) + 32
Fahrenheit to Kelvin: K = (F-32) (5/9) + 273.15
Kelvin to Fahrenheit: F = (K-273.15) (9/5) + 32
"""

