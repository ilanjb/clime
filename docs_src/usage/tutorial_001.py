import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    # docstrings will be take for the ArgumentParser "usage"
    """
    Amaze your friends by printing you name to the console
    """
    name: str

    def introduce(self):
        print(f"hi! my name is {self.name}")


def main():
    clime(Dude).introduce()


if __name__ == "__main__":
    main()
