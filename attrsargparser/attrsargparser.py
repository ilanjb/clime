from argparse import ArgumentParser

import attr


@attr.s(auto_attribs=True)
class AttrsArgparser:
    @staticmethod
    def _add_argument_to_parser(
        parser: ArgumentParser, attibute_arument: attr.Attribute
    ) -> None:
        """
        Parses information from that Attribute to add an argument to the parser
        """
        arg_name = attibute_arument.name
        arg_type = attibute_arument.type
        default = attibute_arument.default
        if default == attr.NOTHING:  # required, positional
            parser.add_argument(
                f"{arg_name}",
                type=arg_type,
            )
        else:
            parser.add_argument(
                f"--{arg_name}",
                type=arg_type,
                default=default,
            )

    @classmethod
    def _build_argument_parser(cls) -> ArgumentParser:
        """
        Creates the parser. then adds the arguments.
        :return:
        """
        parser = ArgumentParser()
        for attibute_arument in cls.__attrs_attrs__:
            cls._add_argument_to_parser(parser, attibute_arument)
        return parser

    @classmethod
    def getargs(cls, args=None, namespace=None):
        """
        Main api. Turns the class into and parser and returns the and instance of the class.
        :param args:
        :param namespace:
        :return:
        """
        parser = cls._build_argument_parser()
        args = parser.parse_args(args=args, namespace=namespace)
        return cls(**args.__dict__)
