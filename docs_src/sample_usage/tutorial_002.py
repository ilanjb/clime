from clime import clime
from docs_src.sample_usage.tutorial_001 import Dude


def main():
    """
    CliMe it!
    :return:
    """
    dude: Dude = clime(Dude)
    dude.introduce()


if __name__ == "__main__":
    main()
