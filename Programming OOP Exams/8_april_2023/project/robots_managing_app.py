from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICES = {"MainService": MainService,
                      "SecondaryService": SecondaryService
                      }

    VALID_ROBOTS = {"MaleRobot": MaleRobot,
                    "FemaleRobot": FemaleRobot
                    }

    VALID_ROBOT_SERVICE_TYPES = {"FemaleRobot": "SecondaryService",
                                 "MaleRobot": "MainService"}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):

        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):

        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        if service.capacity > len(service.robots):

            if self.VALID_ROBOT_SERVICE_TYPES[robot.__class__.__name__] == service.__class__.__name__:
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
            else:
                return "Unsuitable service."

        else:
            raise Exception("Not enough capacity for this robot!")

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = next(filter(lambda s: s.name == service_name, self.services))

        try:
            robot = next(filter(lambda r: r.name == robot_name, self.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):

        service = next(filter(lambda s: s.name == service_name, self.services))
        fed_robots_count = 0

        for robot in service.robots:
            robot.eating()
            fed_robots_count += 1

        return f"Robots fed: {fed_robots_count}."

    def service_price(self, service_name: str):

        service = next(filter(lambda s: s.name == service_name, self.services))

        total_price = sum([robot.price for robot in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):

        info = ''

        for service in self.services:
            info += f'{service.details()}\n'

        return info