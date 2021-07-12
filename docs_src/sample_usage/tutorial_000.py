import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    """
    Everything about the Dude!
    """

    name: str


if __name__ == "__main__":
    print(clime(Dude))
