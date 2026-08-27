name = "Alice"
drink = "latte"
price = 4.5087
#This will work because we are using formatted string
print(f"Order for {name}:{drink}-${price:.2f}")

#This will not work because you cant concatenate a string with a float
#print("Order for " + name + ":" + drink + "- ₦ " + price)
