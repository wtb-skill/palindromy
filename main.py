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
        if word[index] == word[length - 1 - index]:
            continue
        else:
            return False
    return True


def palindrome() -> None:
    """
    Prints a message if a given word is a palindrome.
    :return: print message.
    """
    user_word = input("Please enter a word: ")
    if check_if_palindrome(word=user_word):
        print(f"The word {user_word} is a palindrome.")
    else:
        print(f"The word {user_word} is not a palindrome.")


palindrome()

# TODO 1✔️: Write the main function.
# TODO 2: Check if the input is a string.
# TODO 3️: Add docstring, check typing.

