"""
You are given a list of dictionaries representing products in a catalogue:
Python
Write a program or function that:
Uses filter() with a lambda to keep only items where "category" is "tech".
Uses map() with a lambda and a ternary operator (A if condition else B) to apply:
A 10% discount if price > 1000 (e.g., price becomes price * 0.9).
A 5% discount otherwise (e.g., price becomes price * 0.95).
Returns formatted strings for each discounted item: "Laptop: $1080.0".
Combines all discounted tech products into a single string separated by ", ".
Expected Output:
"Laptop: $1080.0, Phone: $760.0"
"""
# given catalogue
catalogue = [
    {"name": "Laptop", "price": 1200, "category": "tech"},
    {"name": "Shirt", "price": 35, "category": "apparel"},
    {"name": "Phone", "price": 800, "category": "tech"},
    {"name": "Book", "price": 15, "category": "media"},
]


# Filtering out the tech gadgets
tech_list = list(filter(lambda x: x["category"] == "tech", catalogue))

# applying discount based on price
discounted_list = list(map(
    lambda m: f"{m['name']}: ${m['price'] * 0.9 if m['price'] > 1000 else m['price'] * 0.95}", tech_list))

# result string
result_string = ", ".join(discounted_list)
print(result_string)
