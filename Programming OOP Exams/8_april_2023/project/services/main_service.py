from project.services.base_service import BaseService


class MainService(BaseService):

    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        info = f"{self.name} Main Service:\n"
        info += f'Robots: {"none" if len(self.robots) == 0 else ", ".join(robot.name for robot in self.robots)}'
        return info