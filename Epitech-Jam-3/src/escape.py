import json
from .ascii_art import *
from .game import game_loop
from .encrypt import *
from .game import print_wrong_answer
safeKey = False
computerUnlocked = False
doorUnlocked = False


def list_options(data, place):
    print("\nWhat should I do?\nOptions:")
    for object in data["objects"]:
        if object["name"] == place:
            for node in object["options"]:
                print("[" + node + "]")
    print("[back]\n[quit]\n")


def door(data, first=False):
    if first:
        print_ascii_door()
        list_options(data, "door")
    i = input()
    global doorUnlocked
    if i == "open door" or i == "1":
        if not doorUnlocked:
            print("\nThe door is locked. I need to find a way to open it.\n")
            door(data)
        else:
            decrypt_files()
            print("\nCongratulations your files got decrypted!")
            exit(0)
    if i == "read note" or i == "2":
        print('\nThere is a note on the door. It says "I won\'t let you out that easy.\n'
              'I\'ll let you free, when you manage the challenge on the computer.\n'
              'Good luck ~ Mr. Anonymous"\n'
              'PS: in case you need a key: look in the book that bears the name of what it should open\n')
        door(data)
    if i == "back" or i == "3":
        room(data, True)
    if i == "quit" or i == "4":
        print("\nYou will never get out hahaha!!\n")
        exit(0)
    print("\nI can't do that.\n")
    door(data)


def shelf(data, first=False):
    if first:
        print_ascii_shelf()
        list_options(data, "shelf")
    global safeKey
    i = input()
    if i == "investigate" or i == "1":
        print("\nThere are so many books. I probably need some information about which books are important...\n")
        shelf(data)
    if i == "grab book" or i == "2":
        print("\nWhich book should I take?\n")
        j = input()
        foundBook = False
        for node in data["objects"][1]["books"]:
            if j == "safe":
                safeKey = True
            if j == node["name"]:
                print(node["content"])
                foundBook = True
        if not foundBook:
            print("\nThere is no book named \"" + j + "\"\n")
        shelf(data)
    if i == "back" or i == "3":
        room(data, True)
    if i == "quit" or i == "4":
        print("\nYou will never get out hahaha!!\n")
        exit(0)
    print("I can't do that.")
    shelf(data)


def desk(data, first=False):
    if first:
        print_ascii_desk()
        list_options(data, "desk")
    i = input()
    if i == "investigate computer" or i == "1":
        computer(data, True)
    if i == "investigate plate" or i == "2":
        print("\nThere is nothing on it. Just mouse and keyboard...\n")
        desk(data)
    if i == "back" or i == "3":
        room(data, True)
    print("\nI can't do that.\n")
    if i == "quit" or i == "4":
        print("\nYou will never get out hahaha!!\n")
        exit(0)
    desk(data)


def computer(data, first=False):
    global computerUnlocked
    global doorUnlocked
    if first:
        print_ascii_computer()
        print("\nWhat should I do here?")
        for node in data["objects"][2]["computer_options"]:
            print("[" + node + "]")
        print("[back]\n[quit]\n")
    i = input()
    if i == "enter password" or i == "1":
        print("\n[Please enter the password]:")
        j = input()
        if j == "1234":
            print("\nWelcome home Sir!\n"
                  "I should be able to fully use the computer now!\n")
            computerUnlocked = True
            computer(data, True)
        else:
            print("\nPlease retry.\n"
                  "Damn I should look if I find the password in here.\n")
            computer(data, True)
    if i == "back" or i == "5":
        desk(data, True)
    if i == "quit" or i == "6":
        print("\nYou will never get out hahaha!!\n")
        exit(0)
    if not computerUnlocked:
        print("\nI cannot do that if the Computer is locked...\n"
              "I should look for the password.\n")
        computer(data)
    if i == "look for hints" or i == "2":
        game_loop()
        print("Do you know the answer?")
        gotIt = False
        while (not gotIt):
            i = input()
            if (i == decrypt("LdYXOI]_", decrypt("/RWCUX=", "IamNotTheSectret"))):
                gotIt = True
            else:
                print_wrong_answer()
                print("Try again, what is my organisation called?\n")
        doorUnlocked = True
        print("\nThe door clicked! It's open!\n")
        computer(data, True)
    if i == "play genshin impact" or i == "3":
        print("\nIt's pretty fun, but I rather should look for a way to get out of here.\n"
              "Add me (UID: 707510531)\n")
        computer(data)
    if i == "watch Karl's livestream (ImCookiieZz)" or i == "4":
        print("\nWow Karl is streaming again! He's really good. I should leave a sub and then find a way out of here.\n")
        computer(data)
    print("\nI can't do that.\n")
    computer(data)


def carpet(data, first=False):
    if first:
        print_ascii_carpet()
        list_options(data, "carpet")
    i = input()
    if i == "sit on it" or i == "1":
        print("\nWow he is soft and cozy. But I should rest, when I know how to get out of here.\n")
        carpet(data)
    if i == "pull it" or i == "2":
        print("\nWow there is a safe under it! I probably need a key to unlock it.\n")
        safe(data, True)
    if i == "back" or i == "3":
        room(data, True)
    if i == "quit" or i == "4":
        print("\nYou will never get out hahaha!!\n")
        exit(0)
    print("\nI can't do that.\n")
    desk(data)


def safe(data, first=False):
    global safeKey
    if first:
        print("\nWhat should I do here?")
        for node in data["objects"][3]["safe_options"]:
            print("[" + node + "]")
        print("[back]\n[quit]\n")
    i = input()
    if i == "unlock" or i == "1":
        if safeKey:
            print("\nIt works! There is a note inside it.\n"
                  "\"Note to my future me:\n"
                  "If you forget any password, you can find it in the book named 'passwords'\"\n")
        else:
            print("\nI need a key first...\n")
            safe(data)
    if i == "back" or i == "2":
        carpet(data)
    if i == "quit" or i == "3":
        print("\nYou will never get out hahaha!!\n")
        exit(0)
    print("\nI can't do that.\n")
    safe(data)


def room(data, first=False):
    if first:
        print_ascii_art()
        print("What should I do?\nOptions:")
        for node in data['objects']:
            print("[" + node['name'] + "]")
        print("[quit]\n")
    i = input()
    if i == "door" or i == "1":
        door(data, True)
    if i == "shelf" or i == "2":
        shelf(data, True)
    if i == "desk" or i == "3":
        desk(data, True)
    if i == "carpet" or i == "4":
        carpet(data, True)
    if i == "quit" or i == "5":
        print("\nYou will never get out hahaha!!\n")
        exit(0)
    print("\nI can't do that.\n")
    room(data)


def escape_loop():
    decrypt_files()
    with open('dialogue/escape.json') as file:
        data = json.load(file)
    encrypt_files()
    print(data['opening'])
    room(data, True)


