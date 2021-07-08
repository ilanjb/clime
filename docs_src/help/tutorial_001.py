import attr

from clime import clime


@attr.s  # dont need auto_attribs, but it wouldn't hurt...
class Dude:
    name: str = attr.ib(
        metadata={"help": "Your first name"}
    )  # help per attibute is taken from the metadata kwarg in attr.ib

    def introduce(self):
        print(f"hi! my name is {self.name}")


def main():
    clime(Dude).introduce()


if __name__ == "__main__":
    main()
