input = Element('input')
output = Element('output')
kunci = Element('key')


def enkripsi(plaintext, num_key):
    count = 0
    ciphertext = ''
    for i in range(len(plaintext)):
        char0 = plaintext[i]
        char = char0.lower()
        if char == " ":
            ciphertext += ' '
        elif char.isdigit():
            ciphertext += char
        elif char.isalpha():
            if count < len(num_key):
                key1 = num_key[count]
                ciphertext += chr((ord(char) + key1 - 97) % 26 + 97)
                count += 1
            if count == len(num_key):
                count = 0

    return ciphertext


def dekripsi(ciphertext, num_key):
    count = 0
    plaintext = ''
    for i in range(len(ciphertext)):
        char0 = ciphertext[i]
        char = char0.lower()
        if char == " ":
            plaintext += ' '
        elif char.isdigit():
            plaintext += char
        elif char.isalpha():
            if count < len(num_key):
                key1 = num_key[count]
                plaintext += chr((ord(char) - key1 - 97) % 26 + 97)
                count += 1
            if count == len(num_key):
                count = 0

    return plaintext


def proses(*args, **kwargs):
    plaintext = input.value
    key0 = kunci.value

    num_key = []

    key = key0.lower()
    for i in range(len(key)):
        key1 = key[i]
        num_key.append(ord(key1) - 97)

    # console.log(num_key)
    # console.log(key0)

    ciphertext = enkripsi(plaintext, num_key)
    output.element.value = ciphertext
