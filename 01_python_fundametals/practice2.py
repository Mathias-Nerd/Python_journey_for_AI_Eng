#: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
prev = 0
for i in range(0, 10):
    current = i
    print("Current NUmber", current, "Previous NUmber",
          prev, "Sum:", current + prev)
    prev = current
