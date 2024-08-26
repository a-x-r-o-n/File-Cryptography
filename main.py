def ceaserCipher(msg):
    cipher = ''
    for i in msg:
        cipher = cipher + chr(ord(i) + 11)
    return cipher

def ceaserCipherRev(msg):
    plain = ''
    for i in msg:
        plain = plain + chr(ord(i) - 11)
    return plain


def encryption():
    with open('D:\\scraps\\PY\\P R O J E C T S\\File-Encryption\\message.txt','r') as file:
        msg = file.read()
        cipher = ceaserCipher(msg)
        print(cipher)
        pass
    pass

def decryption():
    with open('D:\\scraps\\PY\\P R O J E C T S\\File-Encryption\\cipher.txt','r') as file:
        print(ceaserCipherRev(file.read()))

while True:
    progressChoice = input("\n\nAvailable Modules\n\nENCRYPTION\t\tDECRYPTION\n\nE OR D\nEnter Your choice:").lower()
    if progressChoice == "e":
        encryption()

    elif progressChoice == "d":
        decryption()

    elif progressChoice == "quit":
        break