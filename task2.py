from nltk.corpus import words
import time
import bcrypt

#NOTE: ntlk.corpus requires downloading the words
#This can be done by running these commands:
#import nltk
#nltk.download("words")

FILE = "shadow"

def loadData():
    L = []
    count = 0
    with open(FILE, 'r') as file:
        for line in file:
            #print("Reading in:", line.strip())
            L.append(line.strip())
            count += 1
    return L, count

def divideLines(L):
    users = []
    WF = []
    salts = []
    values = []

    for i in L:
        input = i.split("$")

        users.append(input[0])
        values.append(input[3][22:])

        salt = "$2b$" + input[2] + "$" + input[3][:22]
        salts.append(salt)

    return users, salts, values


def getWords():
    L = []
    sizes = list(range(6,11,1))
    # print(sizes)
    for i in words.words():
        if len(i) in sizes:
            L.append(i)
    return L

def findPassword(words, salt, value):
    for i in words:
        hash = bcrypt.hashpw(i.encode('utf-8'), salt.encode('utf-8'))
        if (hash == value):
            return i

    raise Exception("Something's wrong, no password found")


def main():
    #Task 2
    UnexpectedParty, count = loadData()
    print("In this unexpected party, there are", count)
    users, salts, values = divideLines(UnexpectedParty)

    words = getWords()

    print("\nNow for the password cracking:")
    for i in range(count):
        t1 = time.time()

        pw = findPassword(words, salts[i], values[i])

        t2 = time.time()
        timediff = round(t2 - t1/60, 1)

        pw = pw + ")"
        print("The attack on", users[i],"took", timediff, "minutes. (PW =", pw)

    print("All passwords have been broken and printed above")

if __name__ == '__main__':
    main()