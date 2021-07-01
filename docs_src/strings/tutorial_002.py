import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    name: str = "joe"  # attributes with default values in the class will be set as optional arguments in the cli

    def introduce(self):
        print(f"hi! my name is {self.name}")


def main():
    clime(Dude).introduce()


if __name__ == "__main__":
    main()
