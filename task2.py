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
    salts = []
    values = []

    for i in L:
        input = i.split("$")

        users.append(input[0])
        allButUser = i[len(input[0]):]
        values.append(allButUser.encode('utf-8'))

        salt = "$2b$" + input[2] + "$" + input[3][:22]
        salts.append(salt.encode('utf-8'))

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
        #print(i, end="\t")
        hash = bcrypt.hashpw(i.encode('utf-8'), salt)
        #print(hash)
        #print(i, end="\t")
        #print(value.encode('utf-8'))
        if (hash == value):
            return i

    raise Exception("Something's wrong, no password found")


def main():

    #Task 2
    UnexpectedParty, count = loadData()
    print("In this unexpected party, there are", count)
    users, salts, values = divideLines(UnexpectedParty)

    words = getWords()
    #print("The first word of words is", words[0])
    #salt = bcrypt.gensalt()
    #hash = bcrypt.hashpw(words[0].encode('utf-8'), salt)

    #print(salt)
    #print(hash)


    print("\nNow for the password cracking:")
    for i in range(count):
        t1 = time.time()

        pw = findPassword(words, salts[i], values[i])

        t2 = time.time()
        timediff = round((t2 - t1)/60, 1)

        pw = pw + ")"
        print("The attack on", users[i],"took", timediff, "minutes. (PW =", pw)

    print("All passwords have been broken and printed above")

if __name__ == '__main__':
    main()