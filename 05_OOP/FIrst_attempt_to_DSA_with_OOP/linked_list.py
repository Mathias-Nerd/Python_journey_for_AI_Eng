class CupNode:
    def __init__(self, name):
        self.customer_name = name
        self.next = None


cup_1 = CupNode("Alice")
cup_2 = CupNode("Bob")
cup_3 = CupNode("Charlie")
cup_1.next = cup_2
cup_2.next = cup_3
print(cup_1.next.customer_name)
print(cup_1.next.next.customer_name)

class CupChain:
    def __init__(self):
        self.head = None  # The chain starts empty (no red flag on the counter)
    def append(self, name):
        new_cup = CupNode(name)
        # Scenario A: If the chain is empty, make this cup the head
        if self.head is None:
            self.head = new_cup
            return
        # Scenario B: Walk to the end of the chain and tie the new cup there
        current = self.head
        while current.next is not None:
            current = current.next  # Follow the string to the next cup
        current.next = new_cup  # Tie the new cup to the last cup's empty hook