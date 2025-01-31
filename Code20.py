def emoji_converter(chat):
    words = chat.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😔",
        ";)": "😉",
        "<3": "❤️",
        ":0": "😮",
        ">:)": "😈",
        ";P": "😜",
        ":/": "😕",
        ":|": "😐"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


while True:
    chat = input('> ')
    print(emoji_converter(chat))
    decision = input('Quit? (Y/N): ').upper()
    if decision != 'N':
        print('Terminating session...')
        break
