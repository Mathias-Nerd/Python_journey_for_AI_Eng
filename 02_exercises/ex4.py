"""
Task: You have a list of temperatures in Celsius: celsius_temps = [0, 12, 25, 38.5, 100].Goal: Use map() with a lambda function to convert all temperatures to Fahrenheit.Formula: $(C \times \frac{9}{5}) + 32$Expected Output: [32.0, 53.6, 77.0, 101.3, 212.0]
"""
celsius_temps = [0, 12, 25, 38.5, 100]
result = map(lambda x: (x * 9 / 5) + 32, celsius_temps)
print(list(result))
