from enum import Enum
from typing import Optional

import attr


class Colors(Enum):
    red = "red"  # or 1 or auto()...
    blue = "blue"


@attr.s(auto_attribs=True)
class Dude:
    """
    Everything about the Dude!
    """

    name: str
    favorite_color: Colors
    age_in_years: Optional[int] = None

    def say_name(self):
        print(f"hi! my name is {self.name}")

    def say_favorite_color(self):
        print(
            f"my favorite color is {self.favorite_color.name}"
        )  # we're dealing with Enums here!

    def say_age(self):
        if self.age_in_years is not None:  # 0 counts!
            print(f"I am {self.age_in_years} years old.")
        else:
            print("A script never reveals its age")

    def introduce(self):
        self.say_name()
        self.say_favorite_color()
        self.say_age()
