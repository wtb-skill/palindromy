# Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False,
# mówiącą, czy podany tekst jest palindromem.
import string
import re


def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.

    :param text: any string.
    :return: True if palindrome, False if not.
    """
    return text == text[::-1]


def modify_text(text: str) -> str:
    """
    Removes whitespace, space, new lines, tabs and punctuation from the user input. Only uses lowercase letters.

    :param text: any str.
    :return: modified input.
    """
    text = text.lower()  # Only use lowercase
    text = text.strip()  # Removes whitespace
    text = text.replace(' ', '')  # Remove spaces
    text = text.replace("\n", "")  # Removes new lines
    text = text.replace("\t", "")  # Removes tabs
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)  # Remove punctuation
    return text


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


def palindrome() -> None:
    """
    Prints a message if a given string is a palindrome or not.
    :return: print message.
    """
    user_string = input("Let's check if your input is a palindrome.\n"
                        ">If you give an empty string it will check the contents of the 'palindrom-poemat.txt'.<\n"
                        "Give me a text to check:")
    if user_string == '':
        user_string = test()
    input_type = check_input(user_input=user_string)
    modified_text = modify_text(user_string)
    if is_palindrome(text=modified_text):
        print(f"The {input_type} '{user_string}' is a palindrome.")
    else:
        print(f"The {input_type} '{user_string}' is not a palindrome.")


def test() -> str:
    """
    Loads the 'palindrom-poemat.txt' as a string.

    :return: contents of palindrom-poemat as a string.
    """
    with open('palindrom-poemat.txt', encoding='utf-8') as file:
        contents = file.read()
    return contents


if __name__ == "__main__":
    print("Palindrome: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or "
          "nurses run.")
    end: str = 'y'
    while end.lower()[0] != 'n':
        palindrome()
        end = input("Would you like to continue checking? y/n: ")
