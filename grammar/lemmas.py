import inflect

from time import time

from hierarchy.data import TYPES, SYN


def get_base_noun(noun):
    p = inflect.engine()
    singular = p.singular_noun(noun)

    return singular


def _check_if_supported(noun):
    supported = (noun in TYPES) or (noun in SYN)

    return supported
