from string import ascii_lowercase, ascii_uppercase

def capitalize(sentence: str) -> str:

    if not sentence:
        return ""
    lower_to_upper = {lc: uc for lc, uc in zip(ascii_lowercase, ascii_uppercase)}
    print(lower_to_upper)
    return lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:]

if __name__ == "__main__":
    print(capitalize('hello world'))
    print(capitalize('123hello world'))
    print(capitalize(' hello world'))