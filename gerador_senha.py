import random
import string 
import argparse

def arguments():
    parser = argparse.ArgumentParser(description="password-generator")
    parser.add_argument("-l", "--length", dest="tamanho", type= int, required=True, help="length of the password")
    parser.add_argument("-i", "--initial-name", dest="initial", type=str, help="initial name or number to add on password")
    return parser.parse_args()

def randomizer(len, initial):
    strings = string.ascii_letters + string.digits + string.punctuation
    rand = []
    for _ in range(len):
        senha = str(random.choice(strings))
        rand.append(senha)
    
    if not initial:
        print(''.join(rand))
    else:
        print(initial + ''.join(rand))

def main():
    args = arguments()
    randomizer(args.tamanho, args.initial)

if __name__ == "__main__":
    main()