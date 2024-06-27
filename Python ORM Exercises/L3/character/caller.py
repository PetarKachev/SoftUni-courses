import os
from decimal import Decimal

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name: str, dog: str):
    Pet1 = Pet(
        name=name,
        species=dog
    )
    Pet1.save()

    return f"{Pet1.name} is a very cute {Pet1.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact1 = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    Artifact1.save()

    return f"The artifact {Artifact1.name} is {Artifact1.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    all_info = []
    all_locations = Location.objects.all().order_by('-id')

    for location in all_locations:
        all_info.append(f"{location.name} has a population of {location.population}!")

    return '\n'.join(all_info)


def new_capital():
    first_object = Location.objects.first()
    first_object.is_capital = True
    first_object.save()


def get_capitals():
    names = Location.objects.filter(is_capital=True).values('name')
    return names


def delete_first_location():
    return Location.objects.first().delete()


def create_cars():
    Car1 = Car(
        model='Mercedes C63 AMG',
        year='2019',
        color='white',
        price=120000.00
    )
    Car1.save()

    Car2 = Car(
        model='Audi Q7 S line',
        year=2023,
        color='black',
        price=183900.00
    )
    Car2.save()

    Car3 = Car(
        model='Chevrolet Corvette',
        year=2021,
        color='dark grey',
        price=199999.00
    )
    Car3.save()

    return '3 cars created'


def apply_discount():
    all_car_objects = Car.objects.all()

    for car in all_car_objects:

        car_year = str(car.year)
        percentage_discount = 0
        for digit in car_year:
            percentage_discount += int(digit)

        car.price_with_discount = car.price - (car.price * Decimal(percentage_discount / 100))
        car.save()


def get_recent_cars():
    cars = Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')
    return cars


def delete_last_car():
    last_car = Car.objects.last()

    if last_car:
        last_car.delete()


def create_tasks():
    Task.objects.create(
        title='Sample Task',
        description='This is a sample task description',
        due_date='2023-10-31',
        is_finished=False
    )


def show_unfinished_tasks():
    all_info = []
    all_tasks_objects = Task.objects.all()

    for task in all_tasks_objects:
        if not task.is_finished:
            all_info.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return '\n'.join(all_info)


def complete_odd_tasks():
    all_tasks_objects = Task.objects.all()

    for task in all_tasks_objects:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    encoded_text = []

    for letter in text:
        encoded_text.append(chr(ord(letter) - 3))

    replacement_text = ''.join(encoded_text)

    all_objects = Task.objects.all()

    for task in all_objects:
        if task.title == task_title:
            task.description = replacement_text
            task.save()


def create_hotel_rooms():
    HotelRoom.objects.create(
        room_number='401',
        room_type='Standard',
        capacity=2,
        amenities='Tv',
        price_per_night=100.00
    )

    HotelRoom.objects.create(
        room_number='501',
        room_type='Deluxe',
        capacity=3,
        amenities='Wi-Fi',
        price_per_night=200.00
    )

    HotelRoom.objects.create(
        room_number='601',
        room_type='Deluxe',
        capacity=6,
        amenities='Jacuzzi',
        price_per_night=400.00
    )


def get_deluxe_rooms():
    rooms_info = []
    all_rooms = HotelRoom.objects.all()

    for room in all_rooms:
        if room.room_type == 'Deluxe' and room.id % 2 == 0:
            rooms_info.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return '\n'.join(rooms_info)


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all().order_by('id')

    if len(all_rooms) == 1 or all_rooms[0].is_reserved:
        all_rooms[0].capacity += all_rooms[0].id
        all_rooms[0].save()

    else:
        for index in range(1, len(all_rooms)):
            if all_rooms[index].is_reserved:
                all_rooms[index].capacity += all_rooms[index - 1].capacity
                all_rooms[index].save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()

    if not last_room.is_reserved:
        last_room.delete()
        last_room.save()


def create_characters():
    Character.objects.create(
        name='Voldemor',
        class_name='Mage',
        level=30,
        strength=200,
        dexterity=50,
        intelligence=20,
        hit_points=100,
        inventory='Food'
    )

    Character.objects.create(
        name='Gandalf',
        class_name='Warrior',
        level=30,
        strength=200,
        dexterity=50,
        intelligence=20,
        hit_points=100,
        inventory='Food'
    )

    Character.objects.create(
        name='Darin',
        class_name='Assassin',
        level=30,
        strength=200,
        dexterity=50,
        intelligence=20,
        hit_points=100,
        inventory='Food'
    )

    Character.objects.create(
        name='Petar',
        class_name='Scout',
        level=30,
        strength=200,
        dexterity=50,
        intelligence=20,
        hit_points=100,
        inventory='Food'
    )


def update_characters():
    all_character_objects = Character.objects.all()

    for char in all_character_objects:

        if char.class_name == 'Mage':
            char.level += 3
            char.intelligence -= 7

        elif char.class_name == 'Warrior':
            char.dexterity += 4
            char.hit_points /= 2

        elif char.class_name == 'Assassin' or char.class_name == 'Scout':
            char.inventory = 'The inventory is empty'

        char.save()


def fuse_characters(first_character: Character, second_character: Character):
    current_inventory = ''

    if first_character.class_name == 'Mage' or first_character.class_name == 'Scout':
        current_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif first_character.class_name == 'Warrior' or first_character.class_name == 'Assassin':
        current_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=f'{first_character.name} {second_character.name}',
        class_name='Fusion',
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=current_inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    all_characters = Character.objects.all()

    for char in all_characters:
        char.dexterity = 30
        char.save()


def grand_intelligence():
    all_characters = Character.objects.all()

    for char in all_characters:
        char.intelligence = 40
        char.save()


def grand_strength():
    all_characters = Character.objects.all()

    for char in all_characters:
        char.strength = 50
        char.save()


def delete_characters():
    all_characters = Character.objects.all()

    for char in all_characters:
        if char.inventory == "The inventory is empty":
            char.delete()
