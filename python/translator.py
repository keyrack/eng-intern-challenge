import sys

# Braille mapping tables for lowercase letters and digits.
english_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
    'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
    'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
    'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.",
    'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
    'y': "OO.OOO", 'z': "O..OOO"
}

number_to_braille = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
    '9': ".OO...", '0': ".OOO.."
}

braille_to_english = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd',
    "O..O..": 'e', "OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h',
    ".OO...": 'i', ".OOO..": 'j', "O...O.": 'k', "O.O.O.": 'l',
    "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o', "OOO.O.": 'p',
    "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
    "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x',
    "OO.OOO": 'y', "O..OOO": 'z'
}

braille_to_number = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4',
    "O..O..": '5', "OOO...": '6', "OOOO..": '7', "O.OO..": '8',
    ".OO...": '9', ".OOO..": '0'
}

# Special Braille symbols for capitalization and number indication
SPACE = "......"
CAPITAL_INDICATOR = ".....O"
NUMBER_INDICATOR = ".O.OOO"

# Function to determine if the input is Braille or English
def is_braille(input_string):
    for c in input_string:
        if c != 'O' and c != '.':
            return False  # If any character isn't O or ., it isn't Braille.
    return True

# Function to translate Braille to English
def braille_to_english_translator(braille):
    english = ""
    braille_words = []
    current_braille = ""
    capitalize_next = False
    number_mode = False

    for c in braille:
        current_braille += c
        if len(current_braille) == 6:
            braille_words.append(current_braille)
            current_braille = ""

    if current_braille:
        braille_words.append(current_braille)

    for word in braille_words:
        if word == SPACE:
            english += ' '
            number_mode = False  # Reset number mode after a space
        elif word == CAPITAL_INDICATOR:
            capitalize_next = True
        elif word == NUMBER_INDICATOR:
            number_mode = True
        else:
            if number_mode:
                translated_char = braille_to_number.get(word, '?')  # Translate as number
            else:
                translated_char = braille_to_english.get(word, '?')  # Translate as letter
                if capitalize_next:
                    translated_char = translated_char.upper()
                    capitalize_next = False  # Only capitalize the next character

            english += translated_char
    return english

# Function to translate English to Braille
def english_to_braille_translator(english):
    braille = ""
    in_number_mode = False

    for c in english:
        if c.isspace():
            braille += SPACE
            in_number_mode = False  # Reset number mode after a space
        elif c.isdigit():
            if not in_number_mode:
                braille += NUMBER_INDICATOR
                in_number_mode = True
            braille += number_to_braille[c]
        else:
            if in_number_mode:
                braille += SPACE  # Add space to exit number mode
                in_number_mode = False  # Reset number mode after a space
            if c.isupper():
                braille += CAPITAL_INDICATOR + english_to_braille[c.lower()]
            else:
                braille += english_to_braille[c]
    return braille

def main():
    if len(sys.argv) <= 1:
        print("Usage: python translator.py <string_to_translate>")
        return 1

    input_text = " ".join(sys.argv[1:])
    
    if is_braille(input_text):
        print(braille_to_english_translator(input_text))
    else:
        print(english_to_braille_translator(input_text))

if __name__ == "__main__":
    main()

