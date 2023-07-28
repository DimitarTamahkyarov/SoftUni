from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []
        self.valid_musician_types = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in self.valid_musician_types:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        self.musicians.append(self.valid_musician_types[musician_type](name, age))

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name][0]

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = [b for b in self.bands if b.name == band_name][0]

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        for band in self.bands:
            if band.name == band_name:

                for musician in band.members:
                    if musician.name == musician_name:
                        band.members.remove(musician)
                        return f"{musician_name} was removed from {band_name}."

                raise Exception(f"{musician_name} isn't a member of {band_name}!")

        else:
            raise Exception(f"{band_name} isn't a band!")

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        singers = [m for m in band.members if isinstance(m, Singer)]
        drummers = [m for m in band.members if isinstance(m, Drummer)]
        guitarists = [m for m in band.members if isinstance(m, Guitarist)]

        if not (singers and drummers and guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for drummer in drummers:
                if "play the drums with drumsticks" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            for singer in singers:
                if "sing high pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            for guitarist in guitarists:
                if "play rock" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for drummer in drummers:
                if "play the drums with drumsticks" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            for singer in singers:
                if "sing low pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            for guitarist in guitarists:
                if "play metal" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for drummer in drummers:
                if "play the drums with drumsticks" not in drummer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            for singer in singers:
                if "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

            for guitarist in guitarists:
                if "play jazz" not in guitarist.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."







