import attr

from attrsargparser.attrsargparser import AttrsArgparser


def test_first_sample_no_default_means_positional_argument():
    @attr.s(auto_attribs=True)
    class SampleParser(AttrsArgparser):
        name: str

    args: SampleParser = SampleParser.getargs(["joe"])
    assert isinstance(args, SampleParser)
    assert args.name == "joe"
