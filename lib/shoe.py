#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = "New"  # Default condition is set to "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Update the condition after cobbling


stan_smith = Shoe("Adidas", 9)
print(stan_smith.brand)  # Output: "Adidas"
print(stan_smith.size) # Output: 9
stan_smith.size = 10  # Setting new size
print(stan_smith.size) #Output: 10
stan_smith.size = "not an integer"  # This will print an error message
stan_smith.cobble()  # Output: "Your shoe is as good as new!"
print(stan_smith.condition)  # Output: "New"
stan_smith.cobble()  # Output: "Your shoe is as good as new!"
print(stan_smith.condition)  # Output: "New"
