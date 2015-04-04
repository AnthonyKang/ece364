
# Add all numbers between 1 and 1000 inclusive 
def addNumbers():
    nsum = 0
    for i in range(1001):
        nsum = nsum + i
    return nsum

# calculates and return the sum of all multiples of input that are between 0 and 1000 
def addMultiplesOf(n):
    multiples = range(0,1001,n)
    total = sum(multiples)
    return total

# Find occurence of a number in a string 
def getNumberFrequency(n):
    s = "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1"
    occurences = s.count(str(n))
    return occurences    

# Get Digital Sum of a number 
def getDigitalSum(n):
    n = str(n)
    total = 0
    for i in range(0,len(n)):
        total = int(n[i]) + total
    s = n[0]
    for i in range(1,len(n)):
        s  = s + " + " + n[i] 
    s = s + " = " + str(total)
    return s

# Takes a single digit, returns a string containing the longest streak of numbers that does not contain digit
def getSequenceWithoutDigit(n):
    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982","943020914707361894793269276244518656023955905370512897816345542332011497599489","627842432748378803270141867695262118097500640514975588965029300486760520801049","153788541390942453169171998762894127722112946456829486028149318156024967788794","981377721622935943781100444806079767242927624951078415344642915084276452000204","276947069804177583220909702029165734725158290463091035903784297757265172087724","474095226716630600546971638794317119687348468873818665675127929857501636341131"] 
    s = ''
    for i in range(0,len(strList)):
        s = strList[i] + s
    split = []
    split = max(s.split(str(n)),key=len)
    return split

# Capitalizes first and last letter of each word in a string
def capitalizeMe(s):
    s = s.title()
    result = ''
    for word in s.split():
        result = result + word[:-1] + word[-1].upper() + " "
    return result[:-1]

def main():
    total = addNumbers()
    print total
    total = addMultiplesOf(1)
    print total
    occurences = getNumberFrequency(3)
    print occurences
    digisum = getDigitalSum(12341234)
    print digisum
    sequence = getSequenceWithoutDigit(9)
    print sequence
    capit = capitalizeMe("lorem ipsum dolor a sit amet, vocent civibus has eu")
    print capit

if __name__ == "__main__":
    main()
    