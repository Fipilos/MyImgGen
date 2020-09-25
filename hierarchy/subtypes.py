from hierarchy.data import TYPES
from hierarchy.common import choose_type


def get_subtype(given_types, supported_types):
    """
    Assumes there are no cycles in TYPES.
    """
    while given_types:
        common = given_types.intersection(supported_types)

        if common:
            subtype = choose_type(common)
            return subtype
        else:
            given_types = set([name for g in given_types.intersection(set(TYPES.keys())) for name in TYPES[g]])

    return None


