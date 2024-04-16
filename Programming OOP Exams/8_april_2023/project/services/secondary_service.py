from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self):
        info = f"{self.name} Secondary Service:\n"
        info += f'Robots: {"none" if len(self.robots) == 0 else ", ".join(robot.name for robot in self.robots)}'
        return info