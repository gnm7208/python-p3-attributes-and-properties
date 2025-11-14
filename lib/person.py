#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Alex", job="Admin"):
        self.name = name

        if name == type(str) and (char(range(1,26)) in name):
            return name.totitle()
        else:
            print("Name must be string between 1 and 25 characters")

        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")
        
    

    pass
