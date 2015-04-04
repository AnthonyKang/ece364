def getListProduct(numList):
    product = 1
    print (numList)
    for num in numList:
        product = int(num)*product
    return product    

def partition(numList,n):
    
    partitionlist = []
    for i in range(len(numList)):
        if((i + n) <= len(numList)):
            parition = numList[i:i+n]
            partitionlist.append(parition)
    return partitionlist

def getLargestPartition(nums,n):
    partitionlist = partition(nums,n)
    product = 0
    product_tup = (0,0)
    for partitions in partitionlist:
        new_product = getListProduct(partitions)
        if(new_product > product):
            product = new_product
            product_tup = (partitions, product)
    return product_tup

def readFile(filename):
    with open(filename, 'r') as myFile:
        lines = myFile.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][0:59]
            lines[i] = lines[i].split()
    return lines

def calculate_hsum(lines):
    largest = 0
    for line in lines:
        new_product = getLargestPartition(line,4)
        if new_product[1] > largest:
            largest = new_product[1]
            ltup = new_product
    return ltup

def calculate_vsum(lines):
    v = []
    vlines = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            v.append(lines[j][i])
        vlines.append(v)
    largest = 0
    for line in vlines:
        new_product = getLargestPartition(line,4)
        if new_product[1] > largest:
            largest = new_product[1]
            ltup = new_product
    return ltup

def getLargestProduct():
    lines = readFile('Number Grid.txt')
    hsum = calculate_hsum(lines)
    vsum = calculate_vsum(lines)
    if (hsum[1] > vsum[1]):
        return tuple([hsum[0],hsum[1], 'H'])
    else:
        return tuple([vsum[0], vsum[1], 'V'])

def getPhonebyPartialName(partialName):
    dic = getDirectory()
    #print(dic[('Margaret', 'G', 'Howard')])
    a = dic.keys()
    phonelist = []
    for entry in a:
        first, m, last = entry
        if(first == partialName or last == partialName):
            phonelist.append(dic[entry])
    print(phonelist)

def reverseLookup(areaCode):
    dic = getDirectory()
    numbers = []
    match = []
    for key in dic:
        if(dic[key][1:4] == areaCode):
            match.append(key)
     
    return match

def getDirectory():
    with open('Phone Directory.txt', 'r') as myFile:
        lines = myFile.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split()
        #print (lines)
    entry_dict = {}
    for line in lines:
        entry_dict.update({(line[0],line[1],line[2]):line[3] + ' '+ line[4]})
    #print (entry_dict)
    return entry_dict

def main():
    lines = readFile('Phone Directory.txt')
    print (lines)
    a = getLargestProduct()
    print(a)
    #getDirectory()
    #getPhonebyPartialName('George')
    print(reverseLookup('512'))

if __name__ == "__main__":
    main()
