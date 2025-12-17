import argparse
import os
import readline
import shutil


#copy=1 move=2 erase=3 edit=4 create=5
def modifyArchive(path, option, archive, message):
    if not option:
        print("[ZeroSpec] No input Error")
        return False
    match option:
        case 1:
            try:
                shutil.copy(archive, path)
                print(f"[ZeroSpec] Archive copied to {path}...")
                return True
            except FileNotFoundError:
                print("[ZeroSpec] Archive not found...")
                return False
        case 2:
            try:
                shutil.move(archive, path)
                print(f"[ZeroSpec] Archive moved to {path}...")
                return True
            except FileNotFoundError:
                print("[ZeroSpec] Archive not found...")
                return False
        case 3:
            try:
                os.remove(archive)
                print(f"[ZeroSpec] Archive {archive} erased...")
                return True
            except FileNotFoundError:
                print("[ZeroSpec] Archive not found...")
                return False
        case 4:
            try:
                with open(path, "x") as f:
                    f.write(message)
            except FileExistsError:
                print("[ZeroSpec] The file already exist, you want to continue? This will erase the old information [y][N]")
                response = str(input()).lower()
                if response == "y":
                    with open(path, "w") as f:
                        f.write(message)
                    return True
                elif response == "n":
                    print("[ZeroSpec] Exiting...")
                    return False
                else:
                    print("[ZeroSpec] invalid input, Exiting...")
                    return False
            except FileNotFoundError:
                print("[ZeroSpec] Archive not found...")
                return False
        case 5:
            try:
                with open(path, "x") as f:
                    f.write("")
                return True
            except FileExistsError:
                print(f"[ZeroSpec] The File on {path} already exist")
                return False
            
def archiveCommands(input, arguments):
    match input:
        case "copy":
            def copy():
                try:
                    parts = arguments.split()
                    argument1 = parts[0]
                    argument2 = parts[1]
                    os.system("cp " + argument1+" " + "-t " + argument2)
                    return True
                except Exception:
                    print("[ZeroSpec] Undentified error")
                    return False
            copy()
        case "move":
            try:
                parts = arguments.split()
                argument1 = parts[0]
                argument2 = parts[1]
                os.system("mv " + argument1+" " + "-t " + argument2)
                return True
            except Exception:
                print("[ZeroSpec] Undentified error")
                return False
        case "erase":
            try:
                part = arguments.split()
                arg = part[1]
                os.remove(arg)

def terminal():
    commands = {
        "copy":("copy a file to a different or same folder"),
        "move":("move a file to a folder"),
        "erase":("erase a file"),
        "edit":("edit a text or code file"),
        "create":("create a new file"),
        "cd":("move yourself to another folder"),
        "ls":("list the folder"),
        "pwd":("show the path to current folder"),
        "read":("read and show the choosen file")
    }
    while True:
        print()
        userInput = input("[ZeroSpec] > ")