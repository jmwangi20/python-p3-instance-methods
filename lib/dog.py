#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    def bark(self):
        print("Woolf!")
    
    # Add an instance of sitting on the dog class 
    def sit(self):
        print("The dog is sitting")

fido = Dog()

print(fido.bark())