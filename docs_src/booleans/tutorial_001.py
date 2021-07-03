import attr

from clime import clime


@attr.s(auto_attribs=True)
class Dude:
    likes_ice_cream: bool = False

    def ice_cream_status(self):
        negate = " do not" if not self.likes_ice_cream else ""
        print(f"hi! i{negate} like ice cream")


def main():
    clime(Dude).ice_cream_status()


if __name__ == "__main__":
    main()
