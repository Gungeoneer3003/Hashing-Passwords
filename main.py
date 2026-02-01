from Crypto.Hash import SHA256
from Crypto.Random.random import randint
from binascii import hexlify, unhexlify

STR = "Arbitrary Input"
FLAG = True
PLEASESKIP = False

def printDigest(str):
    sha256_hash = SHA256.new()
    sha256_hash.update(str.encode())
    digest = sha256_hash.digest()
    print(digest.hex())

'''
The purpose of HammingEquivalent is to make a string 
that has a Hamming distance of (num) from (str)
'''
def HammingEquivalent(str, num):
    changed = []
    count = 0
    L = list(bin(int(hexlify(str.encode()),16)))

    while (count < num or count == len(L) - 2):
        index = randint(2, len(L))
        if index in changed:
            continue
        else:
            changed.append(index)
            if (L[index] == '0'):
                L[index] = '1'
            else:
                L[index] = '0'
        count += 1

    str2 = unhexlify(format(int(''.join(L), 2), "x")).decode()
    return str2

def partA():
    print("Part A.")
    if (FLAG):
        str = STR
    else:
        str = input("Enter some arbitrary input:\n")

    print("\nThe result is as follows:")
    printDigest(str)
    print("\n----------------")

def partB():
    print("Part B.")
    if (FLAG):
        str1 = STR
    else:
        str1 = input("Enter some arbitrary input:\n")

    str2 = HammingEquivalent(str1, 1)
    print("The first string is:", str1)
    print("The second string is:", str2)

    print("")

    print("For the first string: ", end="")
    printDigest(str1)

    print("For the second string: ", end="")
    printDigest(str2)

    print("\n----------------")


def main():
    if (not(PLEASESKIP)):
        partA()
        partB()





if __name__ == '__main__':
    main()
