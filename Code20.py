
while True:
    chat = input('> ')
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
    print(output)
    decision = input('Quit? (Y/N): ').upper()
    if decision != 'N':
        break
