from typing import Optional

import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    name: Optional[
        str
    ] = None  # defaults can be set to None. Make sure to annotate as Optional

    def introduce(self):
        if self.name:
            print(f"hi! my name is {self.name}")
        else:
            print(f"hi! my name is a secret")


def main():
    clime(Dude).introduce()


if __name__ == "__main__":
    main()
