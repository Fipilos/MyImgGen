import pkgutil

import entities


def get_submodules_names(module):
    mod_iter = pkgutil.iter_modules(module.__path__)
    names = [n for (_, n, _) in mod_iter if '_' not in n]

    return names


if __name__== '__main__':
    print(get_submodules_names(entities))
