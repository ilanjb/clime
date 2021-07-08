import attr

from clime import clime


def x_smaller_than_100(instance, attribute, value):
    if not value < 100:
        raise ValueError(f"{attribute.name} has to be smaller than 100!")


@attr.s
class Dude:
    favorite_number_less_than_100: int = attr.ib(
        validator=[attr.validators.instance_of(int), x_smaller_than_100]
    )

    def print_favorite_number_less_than_100(self):
        print(
            f"My favorite number less than 100 is {self.favorite_number_less_than_100}"
        )


def main():
    clime(Dude).print_favorite_number_less_than_100()


if __name__ == "__main__":
    main()
