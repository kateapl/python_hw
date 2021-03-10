# """
# Given a file containing text. Complete using only default collections:
#     1) Find 10 longest words consisting from largest amount of unique symbols
#     2) Find rarest symbol for document
#     3) Count every punctuation char
#     4) Count every non ascii char
#     5) Find most common non ascii char for document

# """
import re
from typing import Dict, List


def get_longest_diverse_words(file_path: str) -> List[str]:
    text = ""
    with open(file_path, "r") as fi:
        text = fi.read()
    if text == []:
        return []
    text = (
        text.replace(".", "")
        .replace(",", "")
        .replace(":", "")
        .replace("!", "")
        .replace("?", "")
        .replace(";", "")
    )
    wordlist = text.split()

    # print(wordlist)
    uniqlist = list(set(wordlist))
    # sort list on word length
    uniqlist = sorted(uniqlist, key=len)
    uniqletters = dict()
    for word in uniqlist:
        uniqletters[word] = count_uniq_letters(word)
    listdict = list(uniqletters.items())
    listdict.sort(key=lambda i: i[0])
    listdict.sort(key=lambda i: i[1], reverse=True)
    result = []
    if len(uniqlist) >= 10:
        for i in range(10):
            result.append(listdict[i][0])
    else:
        for i in listdict:
            result.append(i[0])
    # print(result)
    return result


def count_uniq_letters(word: str):
    unique = []
    for char in word:
        if char not in unique:
            unique.append(char)
    return len(unique)


def get_rarest_char(file_path: str) -> str:
    text = ""
    with open(file_path, "r") as fi:
        text = fi.read()
    if text == []:
        return ""
    symbols = dict()

    for letter in text:
        symbols[letter] = symbols.get(letter, 0) + 1
        # .get(letter, 0) вернет значение по ключу letter или 0, если такого ключа нет
    # Выводим ключ, которому соответствует наибольшее из значений
    return min(symbols.items(), key=lambda item: item[1])[0]


def count_punctuation_chars(file_path: str) -> int:
    text = ""
    with open(file_path, "r") as fi:
        text = fi.read()
    if text == []:
        return 0
    count = 0
    punctuation = [".", ",", "!", "?", ":", ";"]
    for char in punctuation:
        count += text.count(char)
    return count


def count_non_ascii_chars(file_path: str) -> int:
    text = ""
    with open(file_path, "r") as fi:
        text = fi.read()
    if text == []:
        return 0
    return text.count("\\")


def get_most_common_non_ascii_char(file_path: str) -> str:
    text = ""
    with open(file_path, "r") as fi:
        text = fi.read()
    if text == []:
        return ""
    unitext = str(text.encode("utf-8"))
    non_ascii = {}
    i = 0
    start = -1
    while unitext:
        start = unitext.find("\\u", start + 1)
        if start == -1:
            break
        non_ascii[unitext[start : start + 6]] = (
            non_ascii.get(unitext[start : start + 6], 0) + 1
        )
    print(non_ascii)
    common = max(non_ascii, key=non_ascii.get)
    return common
