from module import *
if userInstructions():
    while True:
        print("\n\n|----------| FILE CRYPTOGRAPHY |----------|")
        progressChoice = input("\n\nAvailable Modules\n\nENCRYPTION\t\tDECRYPTION\n\nE OR D\nEnter Your choice:").lower()
        if progressChoice == "e":
            encryption()

        elif progressChoice == "d":
            decryption()
        elif progressChoice == "q" or "quit":
            break
        else:
            print("please enter correct command!!")