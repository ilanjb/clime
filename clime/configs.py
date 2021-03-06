from pathlib import Path


CLASSES_HANDLED_DIRECTLY_BY_ARGPARSER = [
    int,
    float,
    ord,
    str,
]

OTHER_CLASSES_KNOW_TO_WORK = [
    Path,
]


KNOWN_CLASS_TYPES_THAT_WILL_WORK_WELL = (
    CLASSES_HANDLED_DIRECTLY_BY_ARGPARSER + OTHER_CLASSES_KNOW_TO_WORK
)
