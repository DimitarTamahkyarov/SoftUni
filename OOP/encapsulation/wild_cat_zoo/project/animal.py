class Animal:
    MONEY_FOR_CARE = 0

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = self.MONEY_FOR_CARE

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
