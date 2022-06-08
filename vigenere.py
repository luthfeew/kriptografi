from pyodide import create_proxy
from js import console, document, FileReader, window, encodeURIComponent

input = Element('input')
file_upload = Element('upload')
upload_name = Element('upload_name')
choice = Element('choice')
kunci = Element('key')
mode = Element('mode')
output = Element('output')
title_in = Element('title_in')
title_out = Element('title_out')
t_enkripsi = Element('tab_enkripsi')
t_dekripsi = Element('tab_dekripsi')


def switch_input():
    input.element.value = output.element.value
    proses()


def tab_enkripsi_click(e):
    if t_enkripsi.element.classList.contains('is-active'):
        pass
    else:
        t_enkripsi.element.classList.add('is-active')
        t_dekripsi.element.classList.remove('is-active')
        title_in.element.innerHTML = 'Plainteks'
        title_out.element.innerHTML = 'Cipherteks'
        choice.element.value = 0
        switch_input()


def tab_dekripsi_click(e):
    if t_dekripsi.element.classList.contains('is-active'):
        pass
    else:
        t_dekripsi.element.classList.add('is-active')
        t_enkripsi.element.classList.remove('is-active')
        title_in.element.innerHTML = 'Cipherteks'
        title_out.element.innerHTML = 'Plainteks'
        choice.element.value = 1
        switch_input()


def read_complete(e):
    input.element.value = e.target.result


async def process_file(x):
    fileList = document.getElementById('upload').files

    # console.log(fileList)

    for f in fileList:
        reader = FileReader.new()
        reader.onloadend = read_complete
        reader.readAsText(f)
        upload_name.element.innerHTML = f.name


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


def unduh_file(*args, **kwargs):
    link = window.document.createElement('a')
    link.setAttribute('href', 'data:text/plain;charset=utf-8,' +
                      encodeURIComponent(output.element.value))
    link.setAttribute('download', 'output.txt')
    link.click()


def main():
    choice.element.value = 0
    t_enkripsi.element.addEventListener(
        'click', create_proxy(tab_enkripsi_click))
    t_dekripsi.element.addEventListener(
        'click', create_proxy(tab_dekripsi_click))
    file_upload.element.addEventListener(
        'change', create_proxy(process_file))


main()
