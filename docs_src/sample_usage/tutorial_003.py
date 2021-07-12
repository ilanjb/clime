from argparse import ArgumentParser

from docs_src.sample_usage.tutorial_001 import Dude, Colors


def main():
    """
    make a parser.
    parser the args.
    convert the args
    pass to Dude.
    :return:
    """
    # make the parser
    parser = ArgumentParser()
    # add the arguments. These must match the arguments from the class
    # If Dude's signature changes, dont forget to update here!!!
    parser.add_argument("name")
    parser.add_argument("favorite_color", choices=Colors.__members__)
    parser.add_argument("--age-in-years", type=int)

    # parse
    args = parser.parse_args()

    # convert args not handled by ArgumentParser
    favorite_color = Colors[args.favorite_color]  # i hope a spelled that right!

    # instantiate and go
    dude: Dude = Dude(args.name, favorite_color, age_in_years=args.age_in_years)
    dude.introduce()


if __name__ == "__main__":
    main()
