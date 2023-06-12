from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary

        if total_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_money_for_animals = 0

        for animal in self.animals:
            total_money_for_animals += animal.money_for_care

        if total_money_for_animals > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_money_for_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = []
        result.append(f"You have {len(self.animals)} animals")
        lions = []
        tigers = []
        cheetahes = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal.__repr__())
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal.__repr__())
            elif animal.__class__.__name__ == "Cheetah":
                cheetahes.append(animal.__repr__())

        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(lion)

        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(tiger)

        result.append(f"----- {len(cheetahes)} Cheetahs:")
        for cheetah in cheetahes:
            result.append(cheetah)

        return "\n".join(result)

    def workers_status(self) -> str:
        result = []
        result.append(f"You have {len(self.workers)} workers")

        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker.__repr__())
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker.__repr__())

        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(keeper)

        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(caretaker)

        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(vet)

        return "\n".join(result)






