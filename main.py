from Crypto.Hash import SHA256
from Crypto.Random import random, get_random_bytes
import time

STR = "Stormlight Archive"
FLAG = True
PLEASESKIP = False
BITS = 8
SAYCOLLISION = False

def Digest(str, bits = 256):
    sha256_hash = SHA256.new()
    sha256_hash.update(str.encode())
    digest = sha256_hash.digest()

    bytes = (bits + 7) // 8
    x = int.from_bytes(digest[:bytes], "big")
    x >>= (bytes * 8 - bits)

    hexlen = (bits + 3) // 4
    return format(x, f'0{hexlen}x')

'''
The purpose of HammingEquivalent is to make a string 
that has a Hamming distance of (num) from (str)
'''
def HammingEquivalent(str1, num):
    changed = []
    count = 0
    L = list(''.join(f"{x:=08b}" for x in bytearray(str1.encode("utf-8"))))

    while (count < num or count == len(L) - 2):
        index = random.randint(2, len(L)-1)
        if index in changed:
            continue
        else:
            changed.append(index)
            if (L[index] == '0'):
                L[index] = '1'
            else:
                L[index] = '0'
        count += 1

    str2 = int(''.join(L), 2).to_bytes(len(L) // 8, byteorder='big').decode(errors="ignore")
    return str2

def countMatches(a, b):
    return sum(x == y for x, y in zip(a, b))

def partA():
    print("Part A.")
    if (FLAG):
        str = STR
    else:
        str = input("Enter some arbitrary input:\n")

    print("\nThe result is as follows:")
    print(Digest(str))
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

    digest1 = Digest(str1)
    digest2 = Digest(str2)


    print("For the first string:  ", end="")
    print(digest1)

    print("For the second string: ", end="")
    print(digest2)

    count = countMatches(digest1, digest2)
    print("Matching byte count:", count)
    print("\n----------------")

#This part utilizes method 2, which should be faster
'''
Steps:
1. Set up a loop
2. Generate a random message
3. Compute hash
4. Add the has to the dictionary (hash -> message)
5. If there's no conflict, repeat
'''
def partC(bitCount):
    Dict = {}
    t1 = time.time()

    while (True):
        m = get_random_bytes(32).hex()

        h = Digest(m, bits=bitCount)

        if h in Dict:
            break
        else:
            Dict[h] = m

    if(SAYCOLLISION):
        print("Collision found! These two both produce a hash of", h)
        print(m)
        print(Dict[h])

    t2 = time.time()
    timediff = t2 - t1

    print(f"{bitCount:2d} Bits -\t {time.strftime("%H:%M:%S", time.gmtime(timediff))} {len(Dict):5d} entries")
    return


def main():
    #Task 1
    if (not(PLEASESKIP)):
        partA()
        partB()

    print("Part C.")
    for i in range(8,50,2):
        partC(i)
    print("\n----------------")

if __name__ == '__main__':
    main()
