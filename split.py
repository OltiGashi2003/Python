def split_func(string: str, separator: str = "-") -> list:

    split_words = []
    last_index = 0
    for index, char in enumerate(string):
        if char == separator:
            split_words.append(string[last_index : index])
            last_index = index + 1
        elif index + 1 == len(string):
            split_words.append(string[last_index : index + 1])
    print(split_words)

if __name__ == "__main__":
    split_func("Olti-Gashi-hat-vor-ein-paar-Jahren-Fussball-Gespielt")
    split_func("DuBistEinfachDieBeste")
