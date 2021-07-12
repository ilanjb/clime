import sys

import pytest

from clime.clime_exceptions import (
    ClassesCanOnlyHaveOneInitArgumentBesidesSelfToBeConverted,
)
from docs_src.integers_floats_and_other_simple_classes.tutorial_004 import main


def test_custome_class_init_cannot_be_converted(set_cli_sys_argv, capsys):
    """
    no args with when one ar is mandatory will fail on argparser
    """
    sys.argv.append("no i am not")
    with pytest.raises(ClassesCanOnlyHaveOneInitArgumentBesidesSelfToBeConverted):
        main()
