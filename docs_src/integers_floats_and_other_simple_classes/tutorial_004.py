"""
Any class with a 2 argument __init__ can be converted directly from argument parse.
Other claasses will fail on Clime
"""
import attr

from clime import clime


class ComplexThing:
    def __init__(self, thing1, thing2):
        self.thing1 = thing1
        self.thing2 = thing2


@attr.s(auto_attribs=True)
class Dude:
    complex_thing: ComplexThing

    def is_thing_a_thing(self):
        assert isinstance(self.complex_thing, ComplexThing)


def main():
    clime(Dude).is_thing_a_thing()


if __name__ == "__main__":
    main()
