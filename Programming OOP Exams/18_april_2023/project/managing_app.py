from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPES = {"PassengerCar": PassengerCar,
                           "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        try:
            user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            if user:
                return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
            if vehicle:
                return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            pass

        vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        try:
            route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point and r.length == length, self.routes))
            if route:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        except StopIteration:
            pass

        try:
            route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point and r.length < length, self.routes))
            if route:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
        except StopIteration:
            pass

        try:
            route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point and r.length > length, self.routes))
            if route:
                route.is_locked = True
        except StopIteration:
            pass

        route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            is_accident_happened = True
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            is_accident_happened = True
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            is_accident_happened = True
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()

        else:
            user.increase_rating()

        return f"{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number} Battery: {vehicle.battery_level}% Status: {'OK' if not vehicle.is_damaged else 'Damaged'}"

    def repair_vehicles(self, count: int):

        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))
        left_part = sorted_damaged_vehicles[:count]
        right_part = sorted_damaged_vehicles[count:]
        repaired_vehicles = 0

        if len(left_part) > len(right_part):
            for vehicle in left_part:
                vehicle.is_damaged = False
                vehicle.battery_level = 100
                repaired_vehicles += 1
        else:
            for vehicle in sorted_damaged_vehicles:
                vehicle.is_damaged = False
                vehicle.battery_level = 100
                repaired_vehicles += 1

        return f"{repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):

        sorted_users = sorted(self.users, key=lambda user_: -user_.rating)

        info = '*** E-Drive-Rent ***\n'
        for user in sorted_users:
            info += f'{user.__str__()}\n'

        return info[:-1]

app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())