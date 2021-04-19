# Morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '@': '.--.-.',
                   '!': '-.-.--', '&': '.-...', ':': '---...',
                   ';': '-.-.-.', '`': '.----.', '"': '.-..-.',
                   '_': '..--.-', '=': '-...-', '+': '.-.-.',
                   ' ': '', '': ' '
                   }

# Saving Morse code keys and values into lists for indexing
key_list = list(MORSE_CODE_DICT.keys())
val_list = list(MORSE_CODE_DICT.values())


# Code for translating Text to Morse
def encode(text):
    text = list(text.upper())
    morse = []
    for char in text:
        morse.append(val_list[key_list.index(char)])
    return ' '.join(morse)


# Code for translating Morse to Text
def decode(morse):
    morse = morse.split(' ')
    text = []
    for char in morse:
        text.append(key_list[val_list.index(char)])
    return ''.join(text)


state = True
while state:
    print('| TEXT - MORSE - TEXT Translator|\n')
    sentence = input("Enter your text:\n")
    choice = input('Choose your option:\n1: Encode\n2: Decode\n')
    if choice == '1':
        print('The translated Text to Morse is:\n' + encode(sentence))
    elif choice == '2':
        print('The translated Morse to Text is:\n' + decode(sentence))
    else:
        print('Invalid Option!')
    cont = input("Do you want to continue?\n1: Yes\n2: No\n").upper()
    if cont == '1':
        state = True
    else:
        state = False
