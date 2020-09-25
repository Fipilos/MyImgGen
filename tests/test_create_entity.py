import pytest

import create_entity


@pytest.mark.parametrize("noun,expected", [('man', 'man'), ('woman', 'woman'), ('people', ['man', 'woman']),
                                           ('person', ['man', 'woman'])])
def test_get_entity_singular(noun, expected):
    result = create_entity._get_entity_singular(noun)

    print(f'returned {result} for {noun}')

    assert result == expected or result in expected