import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


# Create queries within functions


def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{pet.name} is a very cute {pet.species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))

def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by("-id")

    locations_info_output = []

    for location in locations:
        locations_info_output.append(
            f"{location.name} has a population of {location.population}!"
        )

    return "\n".join(locations_info_output)


def new_capital() -> None:
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()


# Location.objects.create(
#     name="Sofia",
#     region="Sofia Region",
#     population=1329000,
#     description="The capital of Bulgaria and the largest city in the country",
#     is_capital=False,
# )
#
# Location.objects.create(
#     name="Plovdiv",
#     region="Plovdiv Region",
#     population=346942,
#     description="The second-largest city in Bulgaria with a rich historical heritage",
#     is_capital=False,
# )
#
# Location.objects.create(
#     name="Varna",
#     region="Varna Region",
#     population=330486,
#     description="A city known for its sea breeze and beautiful beaches on the Black Sea",
#     is_capital=False,
# )

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


# Car.objects.create(
#     model="Mercedes C63 AMG",
#     year=2019,
#     color="white",
#     price=120000.00
# )
#
# Car.objects.create(
#     model="Audi Q7 S line",
#     year=2023,
#     color="black",
#     price=183900.00
# )
#
# Car.objects.create(
#     model="Chevrolet Corvette",
#     year=2021,
#     color="dark grey",
#     price=199999.00
# )
#
# apply_discount()
# print(get_recent_cars())


def show_unfinished_tasks():
    all_tasks = Task.objects.all()

    tasks_info_output = []

    for task in all_tasks:
        tasks_info_output.append(
            f"Task - {task.title} needs to be done until {task.due_date}!"
        )

    return "\n".join(tasks_info_output)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    tasks_with_matching_title = Task.objects.filter(title=task_title)
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)

    for task in tasks_with_matching_title:
        task.description = decoded_text
        task.save()


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title ='Simple Task') .description)


def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_id_deluxe_rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_id_deluxe_rooms.append(str(room))

    return '\n'.join(even_id_deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()
