import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ChessPlayer, Meal, Dungeon, Workout, ArtworkGallery, Laptop


def show_highest_rated_art():
    arts = ArtworkGallery.objects.order_by('-rating', 'id')
    first_art = arts.first()
    return f"{first_art.art_name} is the highest-rated art with a {first_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    list_of_arts = [
        first_art,
        second_art
    ]
    ArtworkGallery.objects.bulk_create(list_of_arts)


def delete_negative_rated_arts():
    negative_ratings = ArtworkGallery.objects.filter(rating__lt=0)
    negative_ratings.delete()


def show_the_most_expensive_laptop():
    laptop = Laptop.objects.order_by('-price', '-id').first()

    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"


def bulk_create_laptops(args):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand='Asus').update(operation_system='Windows')
    Laptop.objects.filter(brand='Apple').update(operation_system='MacOS')
    Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='Linux')
    Laptop.objects.filter(brand='Lenovo').update(operation_system='Chrome OS')


def delete_inexpensive_laptops():
    Laptop.objects.filter(price_lt=1200).delete()


def bulk_create_chess_players(args):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__gte=2300, rating__lte=2399).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating_gte=2200, rating__lte=2299).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating_gte=0, rating_lte=2199).update(title='regular player')


def set_new_chefs():
    Meal.objects.filter(meal_type='Breakfast').update(chef="Gordon Ramsay")
    Meal.objects.filter(meal_type='Lunch').update(chef="Julia Child")
    Meal.objects.filter(meal_type="Dinner").update(chef="Jamie Oliver")
    Meal.objects.filter(meal_type="Snack").update(chef="Thomas Keller")


def set_new_preparation_times():
    Meal.objects.filter(meal_type='Breakfast').update(preparation_time='10 minutes')
    Meal.objects.filter(meal_type='Lunch').update(preparation_time='12 minutes')
    Meal.objects.filter(meal_type="Dinner").update(preparation_time='15 minutes')
    Meal.objects.filter(meal_type="Snack").update(preparation_time='5 minutes')


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


def show_hard_dungeons():
    hard_dungeons = []
    dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')

    for dungeon in dungeons:
        hard_dungeons.append(
            f"{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!")

    return '\n'.join(hard_dungeons)


def bulk_create_dungeons(args):
    Dungeon.objects.bulk_create(args)


def update_dungeon_names():
    Dungeon.objects.filter(difficulty='Easy').update(name="The Erased Thombs")
    Dungeon.objects.filter(difficulty='Medium').update(name="The Coral Labyrinth")
    Dungeon.objects.filter(difficulty='Hard').update(name="The Lost Haunt")


def update_dungeon_bosses_health():
    dungeons = Dungeon.objects.all()

    for dungeon in dungeons:
        if dungeon.difficulty != 'Easy':
            dungeon.boss_health = 500
            dungeon.save()


def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty='Easy').update(recommended_level=25)
    Dungeon.objects.filter(difficulty='Medium').update(recommended_level=50)
    Dungeon.objects.filter(difficulty='Hard').update(recommended_level=75)


def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")

    dungeons = Dungeon.objects.all()

    for dungeon in dungeons:

        if dungeon.location[0] == 'E':
            dungeon.reward = "New dungeon unlocked"
            dungeon.save()

        elif dungeon.location[-1] == 's':
            dungeon.reward = "Dragonheart Amulet"
            dungeon.save()


def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


def show_workouts():
    all_workouts = []
    workouts = Workout.objects.filter(workout_type__in=["Calisthenics", "CrossFit"])

    for workout in workouts:
        all_workouts.append(f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!")

    return '\n'.join(all_workouts)


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors():
    Workout.objects.filter(workout_type="Cardio").update(instructor="John Smith")
    Workout.objects.filter(workout_type="Strength").update(instructor="Michael Williams")
    Workout.objects.filter(workout_type="Yoga").update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type="CrossFit").update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type="Calisthenics").update(instructor="Chris Heria")


def set_new_duration_times():
    Workout.objects.filter(instructor="John Smith").update(duration='15 minutes')
    Workout.objects.filter(instructor="Sarah Davis").update(duration='30 minutes')
    Workout.objects.filter(instructor="Chris Heria").update(duration='45 minutes')
    Workout.objects.filter(instructor="Michael Williams").update(duration='1 hour')
    Workout.objects.filter(instructor="Emily Johnson").update(duration='1 hour and 30 minutes')


def delete_workouts():
    workouts = Workout.objects.all()

    for workout in workouts:
        if workout.workout_type != 'Strength' and workout.workout_type != "Calisthenics":
            workout.delete()


workout1 = Workout.objects.create(
    name="Push-Ups",
    workout_type="Calisthenics",
    duration="10 minutes",
    difficulty="Intermediate",
    calories_burned=200,
    instructor="Chris Heria"
)
workout2 = Workout.objects.create(
    name="Running",
    workout_type="Cardio",
    duration="30 minutes",
    difficulty="High",
    calories_burned=400,
    instructor="John Smith"
)
print(show_workouts())
high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
for workout in high_difficulty_cardio_workouts:
    print(f"{workout.name} by {workout.instructor}")
    set_new_instructors()
    workouts_with_new_instructors = Workout.objects.all()

for workout in workouts_with_new_instructors:
    print(f"Instructor: {workout.instructor}")
    set_new_duration_times()
    workouts_with_new_durations = Workout.objects.all()

for workout in workouts_with_new_durations:
    print(f"Duration: {workout.duration}")