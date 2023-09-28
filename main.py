# Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False,
# mówiącą, czy podany tekst jest palindromem.

def check_if_palindrome(word: str) -> bool:
    """
    Checks if a given string is a palindrome.
    :param word: any string.
    :return: True if palindrome, False if not.
    """
    length = len(word)
    for index in range(0, length//2):
        if word[index].lower() == word[length - 1 - index].lower():
            continue
        else:
            return False
    return True


def check_input(user_input: str) -> str:
    """
    Checks what is the type of the string: is it a word, a number, a phrase or uncategorized.
    :param user_input: any str.
    :return: the type as a string.
    """
    if user_input.isalpha():
        return "word"
    if user_input.isdigit():
        return "number"
    if any(char.isalnum() or char.isspace() for char in user_input):
        return "phrase"
    return "uncategorized input"


def modify_word(word: str) -> str:
    """
    Removes whitespace, space and punctuation from the user input.
    :param word: any str.
    :return: modified input.
    """
    punctuation = [' ', ',', '.', '!', '?']
    word = word.strip()      # Remove leading and trailing whitespace
    for sign in punctuation:      # Remove punctuation
        word = word.replace(sign, "")
    return word


def palindrome() -> None:
    """
    Prints a message if a given string is a palindrome or not.
    :return: print message.
    """
    user_string = input("Please enter a word: ")
    input_type = check_input(user_input=user_string)
    modified_string = modify_word(user_string)
    if check_if_palindrome(word=modified_string):
        print(f"The {input_type} '{user_string}' is a palindrome.")
    else:
        print(f"The {input_type} '{user_string}' is not a palindrome.")


palindrome()

# TODO 1️: ✔ Write the main function.
# TODO 2: ✔ Check if the input is a string.
# TODO 3️: ✔ Add docstring, check typing.

