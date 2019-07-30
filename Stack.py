# Class Representation of a Stack


class Stack:
    def __init__(self):
        self.collection = list()
        self.count = 0

    def push(self, element):
        """Adds a element to the top of the Stack"""
        self.collection.append(element)
        self.count += 1
        return self

    def pop(self):
        """Removes an element from the top of the Stack"""
        if len(self.collection) == 0:
            return None
        self.count -= 1
        element = self.collection[self.count]
        del self.collection[self.count]
        return element

    def peek(self):
        """Reveals the element on top of the Stack"""
        return self.collection[self.count-1]

    def size(self):
        """Returns the count of elements on the Stack"""
        return len(self.collection)

    def __repr__(self):
        items = ""

        for i in range(self.count-1, -1, -1):
            items += self.collection[i].__repr__() + "\n"

        return items
