import time
def error_message(e):

    print("somthing went wrong! :(")
    ch = input("/n Do you want to know the specifics ? \nY or N\nEnter:")

    if ch.lower() == 'y':
        print(e)
def ceaserCipher(msg):
    cipher = ''
    for i in msg:
        cipher = cipher + chr(ord(i) - 11)
    return cipher
def ceaserCipherRev(msg):
    plain = ''
    for i in msg:
        plain = plain + chr(ord(i) + 11)
    return plain
def writeFile(path,msg):
    with open(path,'w') as file:
        file.write(msg)
def encryption():
    try:
        with open('D:\\scraps\\PY\\P R O J E C T S\\File-Encryption\\input\\message.txt','r') as file:
            writeFile('D:\\scraps\\PY\\P R O J E C T S\\File-Encryption\\output\\cipher.txt',ceaserCipher(file.read()))
            print("Encrypting the message....")
            time.sleep(3)
            print("SUCCESSFULLY ENCRYPTED, CHECK THE \"cipher.txt\" FILE ON THE OUTPUT FOLDER")

    except FileNotFoundError:
        print("A FILE IS MISSING CHECK THE GUIDELINES AT THE START OF THE PROGRAM\nIF THE PROBLEM WAS NOT RESOLVED VISIT THE OWNER'S GITHUB REPO\n\n\tGITHUB README -> \"https://github.com/a-x-r-o-n/File-Cryptography/\"")
    except Exception as e:
        error_message(e)
def decryption():
    try:
        with open('D:\\scraps\\PY\\P R O J E C T S\\File-Encryption\\input\\cipher.txt','r') as file:
            writeFile('D:\\scraps\\PY\\P R O J E C T S\\File-Encryption\\output\\plain.txt',ceaserCipherRev(file.read()))
            print("DECODING THE FILE....")
            time.sleep(3)
            print("SUCCESSFULLY DECODED, CHECK THE \"plain.txt\" FILE ON THE OUTPUT FOLDER")
        
    except FileNotFoundError:
        print("A FILE IS MISSING CHECK THE GUIDELINES AT THE START OF THE PROGRAM\nIF THE PROBLEM WAS NOT RESOLVED VISIT THE OWNER'S GITHUB REPO\n\n\tGITHUB README -> \"https://github.com/a-x-r-o-n/File-Cryptography/\"")
    except Exception as e:
        error_message(e)
def userInstructions():
    ch = input("|------------|GUIDELINE|------------|\n\nMAKE SURE YOU ENTERED YOUR TEXT ON THE ALLOCATED FILE\n\nFOR ENCRYPTION ACTIVITY\n\t->ENTER THE PLAIN TEXT TO BE ENCRYPTED ON THE FOLLOWING PATH\t\"..\\projectFileName\\input\\message.txt\"\n\nENTER THE CIPHER TEXT TO BE DECODED ON THE FOLLOWING PATH\t\"..\\projectFileName\\input\\cipher.txt\"\n\nTHE OUTPUT FOR THE ENCRYPTION ACTIVITY IS STORED ON THE \"cipher.txt\" ON THE OUTPUT FOLDER\n\nTHE OUTPUT FOR THE DECRYPTION ACTIVITY IS STORED ON THE \"plain.txt\" ON THE OUTPUT FOLDER\n\nIF YOU'VE READ ALL THE GUIDELINES ENTER \"YES\" TO CONTINUE: ").lower()
    if ch == "yes":
        return True
    else:
        return False

