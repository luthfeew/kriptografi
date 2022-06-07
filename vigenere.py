from pyodide import create_proxy
from js import console

input = Element('input')
choice = Element('choice')
kunci = Element('key')
mode = Element('mode')
output = Element('output')
t_enkripsi = Element('tab_enkripsi')
t_dekripsi = Element('tab_dekripsi')
title_in = Element('title_in')
title_out = Element('title_out')


def switch_input():
    a = input.element.value
    b = output.element.value
    input.element.value = b
    output.element.value = a


def tab_enkripsi_click(event):
    t_enkripsi.element.classList.add('is-active')
    t_dekripsi.element.classList.remove('is-active')
    title_in.element.innerHTML = 'Plainteks'
    title_out.element.innerHTML = 'Cipherteks'
    choice.element.value = 0
    switch_input()


def tab_dekripsi_click(event):
    t_dekripsi.element.classList.add('is-active')
    t_enkripsi.element.classList.remove('is-active')
    title_in.element.innerHTML = 'Cipherteks'
    title_out.element.innerHTML = 'Plainteks'
    choice.element.value = 1
    switch_input()


def main():
    choice.element.value = 0
    t_enkripsi.element.addEventListener(
        'click', create_proxy(tab_enkripsi_click))
    t_dekripsi.element.addEventListener(
        'click', create_proxy(tab_dekripsi_click))


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
    inputan = input.value
    key0 = kunci.value

    num_key = []

    key = key0.lower()
    for i in range(len(key)):
        key1 = key[i]
        num_key.append(ord(key1) - 97)

    # console.log(num_key)
    # console.log(key0)
    # console.log(mode.value)

    match int(choice.value):
        case 0:
            x = enkripsi(inputan, num_key)
        case 1:
            x = dekripsi(inputan, num_key)

    match int(mode.value):
        case 0:
            x = x
        case 1:
            x = x.replace(' ', '')
        case 2:
            x = x.replace(' ', '')
            x = [x[i:i + 5] for i in range(0, len(x), 5)]
            x = ' '.join(x)

    output.element.value = x


main()
