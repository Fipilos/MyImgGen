from word2number import w2n


def get_number_from_numeral(numeral):
    whole_text = _get_whole_text(numeral)
    print(whole_text)
    number = w2n.word_to_num(whole_text)
    print(f'{number}={whole_text}')
    return number


def _get_whole_text(numeral):
    whole_text = numeral.text

    for child in numeral.children:
        whole_text = ' '.join([whole_text, _get_whole_text(child)])

    return whole_text


if __name__ == '__main__':
    for num in ['one twenty', 'one hundred', 'hundred two and nine thirty', 'five and four']:
        print(f'{w2n.word_to_num(num)}={num}')