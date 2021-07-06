from enum import Enum

import attr

from clime import clime


class Colors(Enum):
    red = "red"
    blue = "blue"


@attr.s(auto_attribs=True)
class Dude:
    favorite_color: Colors

    def print_favorite_color(self):
        print(f"my favorite color is {self.favorite_color.value}")


def main():
    clime(Dude).print_favorite_color()


if __name__ == "__main__":
    main()
