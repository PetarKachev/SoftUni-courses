from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENTS = {"KneePad": KneePad,
                        "ElbowPad": ElbowPad
                        }

    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam,
                   "IndoorTeam": IndoorTeam
                   }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for letter in value:
            if str(letter).isalpha():
                pass
            elif str(letter).isdigit():
                pass
            else:
                raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):

        if equipment_type not in self.VALID_EQUIPMENTS:
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        equipment = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type][0]
        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        else:
            self.equipment.remove(equipment)
            team.equipment.append(equipment)
            team.budget -= equipment.price
            return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):

        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception("The team has {number_of_wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        changed_equipments = 0

        sold_equipments = []

        for team in self.teams:
            for eq in team.equipment:
                sold_equipments.append(eq)

        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                changed_equipments += 1

        return f"Successfully changed {changed_equipments}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):

        first_team = next(filter(lambda t: t.name == team_name1, self.teams))
        second_team = next(filter(lambda t: t.name == team_name2, self.teams))

        if not (first_team.__class__.__name__ == second_team.__class__.__name__):
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_sum = first_team.advantage + sum([eq.protection for eq in first_team.equipment])
        second_team_sum = second_team.advantage + sum([eq.protection for eq in second_team.equipment])

        if first_team_sum > second_team_sum:
            first_team.win()
            return f"The winner is {first_team.name}."

        elif first_team_sum < second_team_sum:
            second_team.win()
            return f"The winner is {second_team.name}."

        elif first_team_sum == second_team_sum:
            return "No winner in this game."

    def get_statistics(self):

        info = f'Tournament: {self.name}\n'
        info += f'Number of Teams: {len(self.teams)}\n'
        info += f'Teams:\n'

        for team in self.teams:
            info += f'{team.get_statistics()}\n'

        return info[:-1]