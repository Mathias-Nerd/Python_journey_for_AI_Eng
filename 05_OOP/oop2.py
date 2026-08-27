# class Cup:
#     def __init__(self, size):
#         self.size = size

#     def __eq__(self, other):
#         return self.size == other.size


# print(Cup("large") == Cup("large"))


# class Car:
# pass

# def __str__(self):
#     return f" This is an object called of the Car class"


# print((Car()))

class Cup:
    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        if not isinstance(other, Cup):
            return NotImplemented
        return self.size == other.size

    def __add__(self, other):
        if not isinstance(other, Cup):
            return NotImplemented
        return Cup(self.size + other.size)

    def __str__(self):
        return f"{self.size}"


cup1 = Cup(5)
cup2 = Cup(10)
print(cup1 + cup2)
