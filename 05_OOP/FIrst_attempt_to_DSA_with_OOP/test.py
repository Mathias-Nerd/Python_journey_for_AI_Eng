class CupNode:
    def __init__(self, name):
        self.data = name
        self.next = None


# 1. Create three separate cup nodes
cup_1 = CupNode("Alice")
cup_2 = CupNode("Bob")
cup_3 = CupNode("Charlie")
# 2. Tie the strings!
cup_1.next = cup_2  # Alice points to Bob
cup_2.next = cup_3  # Bob points to Charlie
# cup_3.next remains None (the end of the line)


# 3. Read the linked chain using nested dot notation
print(cup_1.next.customer_name)       # Output: Bob
print(cup_1.next.next.customer_name)  # Output: Charlie
