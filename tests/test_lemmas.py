import pytest

from grammar import lemmas


def test_get_base_noun():
    noun = 'women'
    exp = 'woman'
    ret = lemmas.get_base_noun(noun)

    assert ret == exp
