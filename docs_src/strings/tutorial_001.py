import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    name: str  # attributes without default values in the class will be set as positional arguments in the cli

    def say_name(self):
        print(f"hi! my name is {self.name}")


def main():
    clime(Dude).say_name()


if __name__ == "__main__":
    main()
