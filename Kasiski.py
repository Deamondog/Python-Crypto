from collections import defaultdict
import re

def getsubs(loc, s):
    substr = s[loc:]
    i = -1
    while(substr):
        yield substr
        substr = s[loc:i]
        i -= 1


def longestRepetitiveSubstring(r):
    occ = defaultdict(int)
    # tally all occurrences of all substrings
    for i in range(len(r)):
        for sub in getsubs(i,r):
            occ[sub] += 1
    # filter out all sub strings with fewer than 3 occurrences
    filtered = {k for k,v in occ.items() if v >= 2}
    #print(filtered)

    if filtered:
        maxkey =  max(filtered, key=len) # Find longest string
        res = [i.start()+1 for i in re.finditer(maxkey, r)]
        #print(res)
        return maxkey, res
    else:
        print("no repetitions of any substring of '%s' with 2 or more occurrences" % (r))


# Function to calculate gcd of two numbers
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

# Function to prall the common divisors
def printAllDivisors(arr, N):
    # Variable to find the gcd of N numbers
    g = arr[0]
    # Set to store all the common divisors
    divisors = dict()
    # Finding GCD of the given N numbers
    for i in range(1, N):
        g = gcd(arr[i], g)
    # Finding divisors of the HCF of n numbers
    for i in range(1, g + 1):
        if i*i > g:
            break
        if (g % i == 0):
            divisors[i] = 1
            if (g // i != i):
                divisors[g // i] = 1
    # Prall the divisors
    for it in sorted(divisors):
        print(it, end=" ")

def calcsub(arr): #subs the occurances
    q = []
    z=0


    for i in range(len(arr)-1):
        #while z <= len(q):
        q.append(arr[z+1]-arr[z])
        z=z+1

    return q

def main():
    while True:
        strx = input("Enter String or 'Q' to quit-> ")
        if strx == "Q":
            print("Ending Kaiski...")
            break
        elif strx != "Q":
            strx_alpha = ""
            for char in strx:
                if char.isalpha():
                    strx_alpha += char

            
            x = longestRepetitiveSubstring(strx_alpha)
            arr = x[1]
            y = calcsub(arr)
            n = len(y)
            print("The repeated string is: "+ x[0]+"\nThe locations are: "+str(x[1]))
            print("The factors are: ")
            printAllDivisors(y,n)
            print("\n")

if __name__ == "__main__":
    main()
