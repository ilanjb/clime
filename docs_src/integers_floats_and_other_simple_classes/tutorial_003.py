"""
Any class with a 2 argument __init__ can be converted directly from argument parse.
"""
import attr

from clime import clime


class Thing:
    def __init__(self, thing):
        self.thing = thing


@attr.s(auto_attribs=True)
class Dude:
    thing: Thing

    def is_thing_a_thing(self):
        assert isinstance(self.thing, Thing)


def main():
    clime(Dude).is_thing_a_thing()


if __name__ == "__main__":
    main()
