ALPHABET = {
    'а': 'a',
    'б': 'b',
    'w': 'v',
    'в': 'w',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ч': 'cz',
    'ш': 'sh',
    'щ': 'sch',
    'ъ': '',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'u',
    'я': 'ja',
    'А': 'A',
    'Б': 'B',
    'W': 'V',
    'В': 'W',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'C',
    'Ч': 'CZ',
    'Ш': 'SH',
    'Щ': 'SCH',
    'Ъ': '',
    'Ы': 'y',
    'Ь': '',
    'Э': 'E',
    'Ю': 'U',
    'Я': 'YA',
}


def transliterate(string, from_ru):
    """Transliterate russian text from string and vice versa.

    Args:
        string (str): full cyrilyc of latinic text.
        from_ru (bool): trigger, that shows rus text or not.

    Returns:
        str: translited text.

    Examples:
        >>> print(transliterate('Эта строка будет подвержена транслитерации?', from_ru=True))
        Eta stroka budet podwerzhena transliteracii?
        >>> print(transliterate('Eta stroka budet podwerzhena transliteracii?', from_ru=False))
        Ета строка будет подвержена транслитерации?

    """
    if from_ru:
        for key, value in ALPHABET.items():
            string = string.replace(key, value)
    else:
        for key, value in ALPHABET.items():
            if value == '':
                continue
            string = string.replace(value, key)

    return string
