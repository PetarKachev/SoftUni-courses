from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist,
                       "Drummer": Drummer,
                       "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        try:
            musician = next(filter(lambda m: m.name == name, self.musicians))
            if musician:
                raise Exception(f"{name} is already a musician!")
        except StopIteration:
            pass

        musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):

        try:
            band = next(filter(lambda b: b.name == name, self.bands))
            if band:
                raise Exception(f"{name} band is already created!")
        except StopIteration:
            pass

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        try:
            concert = next(filter(lambda c: c.place == place, self.concerts))
            if concert:
                raise Exception(f"{place} is already registered for {genre} concert!")
        except StopIteration:
            pass

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        band = next(filter(lambda b: b.name == band_name, self.bands))

        musician_types = {"Singer": 0, "Drummer": 0, "Guitarist": 0}

        for member in band.members:
            if member.__class__.__name__ in musician_types:
                musician_types[member] += 1

        if not (musician_types["Guitarist"] >= 1 and musician_types["Drummer"] >= 1 and musician_types["Singer"] >= 1):
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        rock_concert_needed_skills = {'Drummer': 'play the drums with drumsticks',
                                      'Singer': 'sing high pitch notes',
                                      'Guitarist': 'play rock'}

        metal_concert_needed_skills = {'Drummer': 'play the drums with drumsticks',
                                       'Singer': 'sing low pitch notes',
                                       'Guitarist': 'play metal'}

        jazz_concert_needed_skills = {'Drummer': 'play the drums with drum brushes',
                                      'Singer': 'sing high pitch notes and sing low pitch notes',
                                      'Guitarist': 'play jazz'}

        if concert.genre == "Rock":
            drummer_skills = []
            singer_skills = []
            guitarist_skills = []

            for member in band.members:
                if member.__class__.__name__ == "Drummer":
                    drummer_skills = member.skills

                if member.__class__.__name__ == "Singer":
                    singer_skills = member.skills

                if member.__class__.__name__ == "Guitarist":
                    guitarist_skills = member.skills

            if rock_concert_needed_skills["Drummer"] in drummer_skills and rock_concert_needed_skills["Singer"] in singer_skills and rock_concert_needed_skills["Guitarist"] in guitarist_skills:
                profit = (concert.audience * concert.ticket_price) - concert.expenses
                return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
            else:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            drummer_skills = []
            singer_skills = []
            guitarist_skills = []

            for member in band.members:
                if member.__class__.__name__ == "Drummer":
                    drummer_skills = member.skills

                if member.__class__.__name__ == "Singer":
                    singer_skills = member.skills

                if member.__class__.__name__ == "Guitarist":
                    guitarist_skills = member.skills

            if metal_concert_needed_skills["Drummer"] in drummer_skills and metal_concert_needed_skills["Singer"] in singer_skills and metal_concert_needed_skills["Guitarist"] in guitarist_skills:
                profit = (concert.audience * concert.ticket_price) - concert.expenses
                return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
            else:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":

            drummer_skills = []
            singer_skills = []
            guitarist_skills = []

            for member in band.members:
                if member.__class__.__name__ == "Drummer":
                    drummer_skills = member.skills

                if member.__class__.__name__ == "Singer":
                    singer_skills = member.skills

                if member.__class__.__name__ == "Guitarist":
                    guitarist_skills = member.skills

            if jazz_concert_needed_skills["Drummer"] in drummer_skills and jazz_concert_needed_skills[
                "Singer"] in singer_skills and jazz_concert_needed_skills["Guitarist"] in guitarist_skills:
                profit = (concert.audience * concert.ticket_price) - concert.expenses
                return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
            else:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")