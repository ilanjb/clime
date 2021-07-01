import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    name: str  # attributes without default values in the class will be set as positional argumments in the cli

    def introduce(self):
        print(f"hi! my name is {self.name}")


def main():
    clime(Dude).introduce()


if __name__ == "__main__":
    main()
