from enum import Enum

import attr

from clime import clime


class Colors(Enum):
    red = "red"  # or 1 or auto()...
    blue = "blue"


@attr.s(auto_attribs=True)
class Dude:
    favorite_color: Colors

    def say_favorite_color(self):
        print(
            f"my favorite color is {self.favorite_color.name}"
        )  # we're dealing with Enums here!


def main():
    clime(Dude).say_favorite_color()


if __name__ == "__main__":
    main()
