from abc import ABC, abstractmethod


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value
    
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage
    
    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):

        average_protection = 0
        all_protection_for_all_equipment = sum([eq.protection for eq in self.equipment])
        number_of_equipments = len(self.equipment)

        if number_of_equipments > 0:
            average_protection = all_protection_for_all_equipment / number_of_equipments
        else:
            average_protection = 0

        info = f"Name: {self.name}\n"
        info += f'Country: {self.country}\n'
        info += f'Advantage: {self.advantage} points\n'
        info += f'Budget: {self.budget:.2f}EUR\n'
        info += f'Wins: {self.wins}\n'
        info += f'Total Equipment Price: {sum([eq.price for eq in self.equipment]):.2f}\n'
        info += f'Average Protection: {round(average_protection)}\n'
        return info[:-1]
