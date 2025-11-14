#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Simba", breed="Korokoro"):
        self.name = name

    if name == type(str) and (char(range(1,26)) in name):
        print("Valid dog name")
    else:
        print("Name must be string between 1 and 25 characters")

    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self.breed = breed
            print(f"{self.name} is a {self.breed}")
        else:
            print(f"Breed '{breed}' is not approved.")
        
    pass

    
