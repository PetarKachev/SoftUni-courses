from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):

    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str ):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage = ((mileage / self.max_mileage) * 100) - 5
        result = round(self.battery_level - percentage)
        self.battery_level = result