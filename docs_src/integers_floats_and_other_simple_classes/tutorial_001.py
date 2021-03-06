import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    age_in_years: int

    def confess_age(self):
        print(f"I am {self.age_in_years} years old.")


def main():
    clime(Dude).confess_age()


if __name__ == "__main__":
    main()
