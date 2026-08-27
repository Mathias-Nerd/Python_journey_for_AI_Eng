"""
Implement smart_temperature(value). Convert value to a Celsius number. If conversion fails, return Invalid temperature. Convert Celsius to Fahrenheit using the standard formula. Return a three-line report with labels Celsius, Fahrenheit, and Status. Status is freezing when Celsius is less than or equal to 0, cold when below 20, warm when from 20 through 30, and hot when above 30.
"""
def smart_temperature(value):
    try:
        float(value)
    except:
        return "Invalid temperature"
    cel = float(value)
    temp = ""
    if cel <= 0:
        temp = "freezing"
    elif cel > 0 and cel <= 20:
        temp = "cold"
    elif cel > 20 and cel <= 30:
        temp = "warm"
    else:
        temp = "hot" 
    return f"Celsius: {cel}\nFahrenheit: { ( cel * 9 / 5 ) + 32}\nStatus: {temp}"

