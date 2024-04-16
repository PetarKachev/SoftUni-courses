from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):

        value_to_reduce = 0.3 * time_to_catch

        if not isinstance(value_to_reduce, int):
            value_to_reduce = round(value_to_reduce)

        if self.oxygen_level >= value_to_reduce:
            self.oxygen_level -= value_to_reduce

        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.OXYGEN_LEVEL
