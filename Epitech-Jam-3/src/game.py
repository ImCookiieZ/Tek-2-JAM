import sys
import json
import random
from .encrypt import *


def print_right_answer(index):
    if index == '1':
        print("[My beginning is very important]\n")
    elif index == '2':
        print("[the best comes at the end]\n")
    elif index == '3':
        print("[sex rhymes with six]\n")
    elif index == '4':
        print("[all beginning is difficult]\n")
    elif index == '5':
        print("[the end is near]\n")
    elif index == '6':
        print("[If you are looking for a good, understanding and beautiful human, you are looking for not one, but three]\n")
    elif index == '7':
        print("Array[1][0]\n")


def print_wrong_answer():
    n = random.randint(0, 2)
    if n == 0:
        print("!!! Ah I think you should take your time to get the right answer\n")
    elif n == 1:
        print("!!! Nope, that’s not what I want to hear\n")
    elif n == 2:
        print("!!! Think of your files, if you continue like that you will never get them back\n")


def pass_check():
    print("Okay lets try. What do you think is the password?")
    i = input()
    print("This gets you to the message: " + decrypt("=YKi\x06M\\\x06eRZ\x06RJSV\ndL\x04V_\x11YgMEWOdKiOSW%", i))
    if i == decrypt("/RWCUX=", "IamNotTheSectret"):
        return True
    else:
        print_wrong_answer()
        return False


def game_loop():
    print("There is a suspicious text document...\n"
          "\"To get out of the room you will acquire a password. To encrypt this message:\n"
          "'=YKi\x06M\\\x06eRZ\x06RJSV\ndL\x04V_\x11YgMEWOdKiOSW%'.\n"
          "Whenever you think you got the password, type 'password:'.\"\n")

    decrypt_files()
    with open('dialogue/dialogue.json') as file:
        data = json.load(file)
    encrypt_files()
    for node in data['dialogue']:
        success = False
        while not success:
            print(node['text'])
            i = input()
            if i == node['answer'] or (node['index'] == '0'):
                success = True
                print_right_answer(node['index'])
            elif i == "password:":
                if pass_check():
                    return
            else:
                print_wrong_answer()