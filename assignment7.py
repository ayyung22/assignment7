#CIS 103 XY Fundamentals of Programming
#Assignment 7: Inheritance and Abstract Classes
#Author: Annie Yung
#Date: 11/15/2024

from abc import ABC, abstractmethod

print("Conceptual Questions, Customizing a Class using Inheritance")
print()
#Creating a superclass
class Animal:
    def speak(self):
        return "All animals make sound"

#Creating a subclass that overrides the 'speak' method
class Cow(Animal):
    def speak(self): #Overriding the 'speak' method
        return "Moo!"

class Dog(Animal):
    def speak(self): #Overriding the 'speak' method
        return "Woof!"

#Creating instances of both the Cow and Dog
cow = Cow()
dog = Dog()

print(cow.speak())
print(dog.speak())
print()
print()

print("Part 2: Coding Exercises")
class ArrayBag:
    def __init__(self):
        #Initialize an empty bag
        self.items = []

    def add(self, item):
        #Add an item to the bag
        self.items.append(item)

    def contains(self, item):
        #Check if the item is in the bag
        return item in self.items

    def display(self):
        #Display the contents of the bag."""
        return self.items

    def __len__(self):
        #Return the number of items in the bag
        return len(self.items)


class ArraySortedBag(ArrayBag):
    def __init__(self):
        #Initialize an empty sorted bag
        super().__init__()

    def add(self, item):
        #Add an item to the bag
        from bisect import insort
        insort(self.items, item)

    def display(self):
        #Display the sorted contents of the bag
        return self.items


#Example:

# Create an unsorted bag
bag = ArrayBag()
bag.add(3)
bag.add(1)
bag.add(2)
print("Unsorted Bag Contents:", bag.display())

# Check if an item is in the bag
print("Contains 2?", bag.contains(2))

# Create a sorted bag
sorted_bag = ArraySortedBag()
sorted_bag.add(3)
sorted_bag.add(1)
sorted_bag.add(2)
print("Sorted Bag Contents:", sorted_bag.display())

# Check if an item is in the sorted bag
print("Contains 2?", sorted_bag.contains(2))

