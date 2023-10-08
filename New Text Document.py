# Morse code dictionary (character to Morse code)
char_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': ' '
}

# Morse code dictionary (Morse code to character)
morse_to_char = {v: k for k, v in char_to_morse.items()}


# Function to translate text to Morse code
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in char_to_morse:
            morse_code.append(char_to_morse[char])
    return ' '.join(morse_code)


# Function to translate Morse code to text
def morse_to_text(morse_code):
    words = morse_code.split('  ')
    text = []
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in morse_to_char:
                text.append(morse_to_char[letter])
        text.append(' ')
    return ''.join(text)


# Main program
while True:
    print("Morse Code Translator")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter the text: ")
        morse_code = text_to_morse(text)
        print("Morse Code:", morse_code)
    elif choice == '2':
        morse_code = input("Enter Morse code (use space between words): ")
        text = morse_to_text(morse_code)
        print("Text:", text)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")