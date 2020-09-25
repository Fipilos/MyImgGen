from hierarchy.data import TYPES
from hierarchy.common import choose_type


def _get_parents(name):
    parents = set()

    for t in TYPES:
        if name in TYPES[t]:
            parents.add(t)

    return parents


def get_supertypes(given_types, supported_types):
    while given_types:
        common = given_types.intersection(supported_types)

        if common:
            supertype = choose_type(common)
            return supertype
        else:
            given_types = set([i for name in given_types for i in _get_parents(name)])

    return None


if __name__ == '__main__':
    print(get_supertypes({'man'}, {'human', 'cat'}))

