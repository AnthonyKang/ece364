import glob

def getFiles(foldername):
    filelist = []
    for name in glob.glob(foldername+'/*'):
        filelist.append(name)
    return filelist

def getWordFrequency(filelist):
    freqDict = {}
    for files in range(0,len(filelist)):
        myfile = open(filelist[files], 'r')
        wordlist = myfile.read().split()
        wordlist = [word.replace(",","") for word in wordlist]
        wordlist = [word.replace(".","") for word in wordlist]
        for word in wordlist:
            if(not freqDict.get(word)):
                freqDict.update({word:1})
            elif(freqDict.get(word)):
                freqDict[word] = freqDict[word] + 1
    return freqDict

def getDuplicates(filelist):
    duplicateDict = {}
    for files in range(0, len(filelist)):
        myfile = open(filelist[files], 'r')
        wordlist = myfile.read().split()
        wordcount = len(wordlist)
        if(not duplicateDict.get(wordcount)):
            duplicateDict.update({wordcount:[filelist[files][6:9]]})
        elif(duplicateDict.get(wordcount)):
            duplicateDict[wordcount].append(filelist[files][6:9])
    duplicateTuple = duplicateDict.items()
    duplicateDict = {}
    for groups in duplicateTuple:
        duplicateDict.update({groups[1][0]:groups})

    return duplicateDict

def getPurchaseReport():
    purchaseFiles = []
    for purchases in glob.glob('purchases/purchase*'):
        purchaseFiles.append(purchases)
    for purchases in glob.glob('purchases/Item*'):
        itemlist = purchases
    item_dict = {}
    with open(itemlist,'r') as itemfile:
        all_lines = itemfile.readlines()
        for i in range(2,len(all_lines)):
            item = all_lines[i].split()
            item_dict.update({item[0]:item[1]})
        #print item_dict
    report_dict = {}
    for i in range(0,len(purchaseFiles)):
        with open(purchaseFiles[i],'r') as purchasefile:
            item_total = 0
            purchase_list = purchasefile.readlines()
            #print purchaseFiles[i][19:22]
            for j in range(2,len(purchase_list)):
                purchase = purchase_list[j].split()
                #print float(item_dict[purchase[0]][1:])
                #print float(purchase[1])
                item_total = float(item_dict[purchase[0]][1:])*float(purchase[1])+item_total
                #print item_total
        report_dict.update({int(purchaseFiles[i][21]):"{0:.2f}".format(item_total)})
        #print purchaseFiles[i][19:22]
     

    print report_dict
    return report_dict

def getTotalSold():
    purchaseFiles = []
    for purchases in glob.glob('purchases/purchase*'):
        purchaseFiles.append(purchases)
    total_sold = {}
    for i in range(0, len(purchaseFiles)):
        with open(purchaseFiles[i],'r') as purchasefile:
            purchase_list = purchasefile.readlines()
            for j in range(2,len(purchase_list)):
                purchase = purchase_list[j].split()
                if(not total_sold.get(purchase[0])):
                    total_sold.update({purchase[0]:int(purchase[1])})
                elif(total_sold.get(purchase[0])):
                    total_sold[purchase[0]] = int(purchase[1]) + total_sold[purchase[0]]
    print total_sold


def main():
    #filelist = getFiles('files')
    #print filelist
    #freqDict = getWordFrequency(filelist)
    #print freqDict
    #print filelist[0][6:9]
    #print (["hi","asdf"] == ["hi","asdf"])
    #duplicateDict = getDuplicates(filelist)
    #print duplicateDict
    purchases = getPurchaseReport()
    total = getTotalSold()

if __name__ == "__main__":
    main()
    
