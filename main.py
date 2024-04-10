# Read a file until a specific Character in Python

with open('example.txt', 'r', encoding='utf-8') as file:
    contents = file.read()

    character = '!'

    result = contents.split(character)
    print(result)  # 👉️ ['bobby\nhadz\n.com\n', '\none\ntwo\nthree']

    # bobby
    # hadz
    # .com
    print(result[0])