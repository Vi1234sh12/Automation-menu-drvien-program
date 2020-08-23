""" this code basically automates various system opertions.
it is a very interactive and user-firendly program.
ten two  modules used are os and pyttsx3.
"""
def system_opertions():
    import pyttsx3
    import os
    pyttsx3.speak("Feel free to type in any statement !")
    while(True):
        opertions =input("please type which opertions you want to perform : ")

        print()
        opertions = opertions.lower()

        if("chrome" in opertions) or ("browser" in opertions):
            pyttsx3.speak("please wait opening chrome for you")
            os.system("chrome")
        elif("notepad"in opertions) or("text editor" in opertions):
            pyttsx3.speak("please wait opening notepad for you")
            os.system("notepad")
        elif("media player"in opertions) or ("player" in opertions):
            pyttsx3.speak("please wait opening media player for you")
            os.system(" media player")
        elif("viusal studio code" in opertions) or ("vs code" in opertions):
            pyttsx3.speak("please wait opening visual studio code for you")
        elif("exit" in opertions) or ("return" in opertions) or("close"in opertions):
            pyttsx3.speak("thank you! hope to see you again")
            break
        else:
            print("Error : try some other opertions available form the list :")
            pyttsx3.speak("please enter some other opertion")
            print()

def main():
    import os
    import pyttsx3
    print()
    pyttsx3.speak("Welcome to the automation world !")
    print("              this is a Menu Drive Program")
    print()
    print("available opertions :")
    print("1] open Chrome \n2] open notepad \n 3]media player\n 4] open vs code \n 5] exit")
    print()
    print("you can type a statement and interact !")
    print()

    system_opertions()

if __name__ == "__main__":
    main()
