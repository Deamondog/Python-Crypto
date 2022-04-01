import hashlib
import itertools


def calcPerm(hashList, target):
    for i in itertools.permutations(hashList):
        currentChain = calChain(i)[0]
        initial_Chain = calChain(i)[1]
        if currentChain.hexdigest().upper() == target:
            for x in range(len(hashList)):
                print(str(x+1)+':',i[x].hexdigest().upper())
            print('Inital Chain: ',initial_Chain)
            print('Final: ',target)
            break;
        
def calChain(perm):
    chain = hashlib.sha256()
    ini_Chain = chain.hexdigest().upper()
    # print("Inital Chain: ", ini_Chain)

    for x in range(5):
        chain.update(perm[x].digest())
    return chain,ini_Chain

def main():

    #create 5 hashes
    hash1 = hashlib.sha256(b"This is my first hash")
    hash2 = hashlib.sha256(b"This is my second hash")
    hash3 = hashlib.sha256(b"This is my third hash")
    hash4 = hashlib.sha256(b"This is my forth hash")
    hash5 = hashlib.sha256(b"This is my fifth hash")
    hashList = [hash1,hash2,hash3,hash4,hash5]
    while True:

        target = input("Enter target Hash or 'Q' to quit: ") #'15C6F6C338FEB2C1F6312EEECD1D111CBED0183AC087C3305E70F93B2E8268AF'
        if target == 'Q':
            print("Ending....")
            break;
        elif target == '' or len(target) < 2:
            print("Enter Valid Hash")
        else:
            calcPerm(hashList,target)


if __name__ == "__main__":
    main()
