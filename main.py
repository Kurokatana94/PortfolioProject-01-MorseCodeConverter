morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
              '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', ':': '---...', ';': '-.-.-.', '=': '-...-', '&': '.-...',
              '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-.', ' ': '/', '+': '.-.-.'
}

def ttm(text: str) -> str:
    conv_words_list = [f'{morse_dict[l]} ' if l in morse_dict.keys() else '' for l in list(text.lower())]
    conv_txt = ''.join(conv_words_list)
    return conv_txt

def mtt(text: str) -> str:
    conv_morse_list = [''.join([key for key, value in morse_dict.items() if morse_dict[key] == l ])for l in text.split()]
    conv_txt = ''.join(conv_morse_list)
    return conv_txt

isRunning = True

while isRunning:
    while True:
        service = input('Would you like to use Morse To Text (mtt) or Text To Morse (ttm)?\n'
                 'Please type the needed service as \"mtt\" or \"ttm\":\n')
        if service == 'ttm':
            print(f'{ttm(input('Please, type a text to translate to morse code:\n'))}')
            break
        elif service == 'mtt':
            print(f'{mtt(input('Please, type or paste your morse code to decode it into text.\n'
                           '(each morse code letter must be separated by a space, and each word by a \"/\")\n'))}'.upper())
            break
        else:
            input_ = input('The input was not accepted, please press enter try again or type \"exit\" to end the program.\n')
            if input_.lower() == 'exit':
                isRunning = False
                break
    if isRunning and input('Do you want to continue?\nType Y/N\n').lower() == 'n':
        isRunning = False
