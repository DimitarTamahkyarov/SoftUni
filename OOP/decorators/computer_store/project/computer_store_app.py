from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Laptop":
            laptop = Laptop(manufacturer, model)
            result = laptop.configure_computer(processor, ram)
            self.warehouse.append(laptop)

            return result

        elif type_computer == "Desktop Computer":
            desktop = DesktopComputer(manufacturer, model)
            result = desktop.configure_computer(processor, ram)
            self.warehouse.append(desktop)

            return result

        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

        for pc in self.warehouse:
            if client_budget >= pc.price and wanted_processor == pc.processor and pc.ram >= wanted_ram:
                self.profits += client_budget - pc.price
                result = str(pc)
                self.warehouse.remove(pc)

                return f"{result} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")

