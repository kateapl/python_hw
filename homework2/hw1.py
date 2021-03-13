# """
# Given a file containing text. Complete using only default collections:
#     1) Find 10 longest words consisting from largest amount of unique symbols
#     2) Find rarest symbol for document
#     3) Count every punctuation char
#     4) Count every non ascii char
#     5) Find most common non ascii char for document

# """
import string
import unicodedata
from collections import defaultdict
from typing import Dict, List


def get_text(file_path: str):
    text = ""
    with open(file_path, "r", encoding="unicode-escape") as fi:
        text = fi.read()
    return text


def get_punctuation(text):
    punc = set()
    for char in text:
        if unicodedata.category(char).startswith("P"):
            punc.add(char)
    punctuation = "".join(punc)
    return str(punctuation)


def get_longest_diverse_words(file_path: str) -> List[str]:
    text = get_text(file_path)
    for p in get_punctuation(text):
        if p in text:
            text = text.replace(p, "")

    wordlist = text.split()
    uniqlist = list(set(wordlist))
    uniqletters = dict()
    for word in uniqlist:
        uniqletters[word] = (count_uniq_letters(word), len(word))
    listdict = list(uniqletters.items())
    listdict.sort()
    listdict.sort(key=lambda item: item[1], reverse=True)
    result = []
    if len(uniqlist) >= 10:
        for i in range(10):
            result.append(listdict[i][0])
    else:
        for i in listdict:
            result.append(i[0])
    print(result)
    return result


def count_uniq_letters(word: str):
    unique = []
    for char in word:
        if char not in unique:
            unique.append(char)
    return len(unique)


def get_rarest_char(file_path: str) -> str:
    text = get_text(file_path)
    symbols = defaultdict(int)

    for letter in text:
        symbols[letter] += 1
    return min(symbols.items(), key=lambda item: item[1])[0]


def count_punctuation_chars(file_path: str) -> int:
    text = get_text(file_path)
    if text == []:
        return 0
    count = 0
    for char in get_punctuation(text):
        count += text.count(char)
    return count


def count_non_ascii_chars(file_path: str) -> int:
    text = get_text(file_path)
    if text == []:
        return 0
    count = 0
    for char in text:
        if ord(char) > 128:
            count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    text = get_text(file_path)
    non_ascii = defaultdict(int)
    for char in text:
        if ord(char) > 128:
            non_ascii[char] += 1
    return max(non_ascii, key=non_ascii.get)
