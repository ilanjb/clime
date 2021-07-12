from typing import Optional

import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    age_in_years: Optional[int] = None

    def volunteer_age(self):
        if self.age_in_years is not None:  # 0 counts!
            print(f"I am {self.age_in_years} years old.")
        else:
            print("A script never reveals its age")


def main():
    clime(Dude).volunteer_age()


if __name__ == "__main__":
    main()
