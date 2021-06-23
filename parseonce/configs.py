from pathlib import Path

KNOWN_CLASS_TYPES_THAT_WILL_WORK_WELL = {
    # adapted from https://docs.python.org/3/library/argparse.html#type
    str,
    int,
    float,
    bool,
    Path,
    ord,
}
