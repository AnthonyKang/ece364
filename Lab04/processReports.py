import glob

def generateReportForAllUsers():
    users = []
    userDict = {}
    with open('users.txt','r') as myFile:
        lines = myFile.readlines()
        for line in range(2,len(lines)):
            users.append(lines[line].split())
        for i in range(0,len(users)):
            #print(users[i])
            userDict.update({users[i][0][:-2] + ' ' + users[i][1]:users[i][3]})
    filelist = []
    for files in glob.glob('reports/*'):
        filelist.append(files)
    #print (filelist)
    report = []
    reportDict = {}
    
    for filename in filelist:
        total_units = 0
        total_cost = 0
        with open(filename,'r') as reportFile:
            lines = reportFile.readlines()
            for line in range(4,len(lines)):
                report.append(lines[line].split())
            userid = lines[0][9:-1]
            #print (userid)
            for i in range(0,len(report)):
                total_units = int(report[i][2]) + total_units
                total_cost = float(report[i][3][1:]) + total_cost
        if(not reportDict.get(userid)):
                reportDict.update({userid:(total_units,total_cost)})
        elif(reportDict.get(userid)):
            reportDict[userid] = (total_units,total_cost)
    #print (reportDict)
      
    #for user_id in reportDict:
    #    print(user_id)
    finalDict = {}
    for user_id in userDict:
        #userDict[usersKey] = reportDict[userDict[usersKey]]
        #print (user_id)
        if userDict[user_id] in reportDict:
            finalDict.update({user_id:reportDict[userDict[user_id]]})
    #print (finalDict)
    return finalDict

def generateReportForAllViruses():
    filelist = []
    for files in glob.glob('reports/*'):
        filelist.append(files)
    #print (filelist)
    report = []
    virusDict = {}

    for filename in filelist:
        total_count = 0
        total_cost = 0
        with open(filename,'r') as reportFile:
            lines = reportFile.readlines()
            for line in range(4,len(lines)):
                report.append(lines[line].split())
            for i in range(0,len(report)):
                virus = report[i][1]
                if(not virusDict.get(virus)):
                    virusDict.update({virus:(int(report[i][2]),float(report[i][3][1:]))})
                elif(virusDict.get(virus)):
                    count , price = virusDict[virus]
                    count = count + int(report[i][2])
                    price = price + float(report[i][3][1:])
                    virustuple = (count,price)
                    virusDict[virus] = virustuple
    #print (virusDict)
    return virusDict

def RefStrainSummaryReport():
    users = []
    userDict = {}
    with open('users.txt','r') as myFile:
        lines = myFile.readlines()
        for line in range(2,len(lines)):
            users.append(lines[line].split())
        for i in range(0,len(users)):
            #print(users[i])
            userDict.update({users[i][0][:-2] + ' ' + users[i][1]:users[i][3]})
    filelist = []
    for files in glob.glob('reports/*'):
        filelist.append(files)
    #print (filelist)
    report = []
    reportDict = {}
    
    for filename in filelist:
        total_units = 0
        total_cost = 0
        with open(filename,'r') as reportFile:
            lines = reportFile.readlines()
            for line in range(4,len(lines)):
                report.append(lines[line].split())
            userid = lines[0][9:-1]
            #print (userid)
            for i in range(0,len(report)):
                total_units = int(report[i][2]) + total_units
                total_cost = float(report[i][3][1:]) + total_cost
        if(not reportDict.get(userid)):
                reportDict.update({userid:(total_units,total_cost)})
        elif(reportDict.get(userid)):
            reportDict[userid] = (total_units,total_cost)
    finalset = set()
    for user_id in userDict:
        #userDict[usersKey] = reportDict[userDict[usersKey]]
        #print (user_id)
        if userDict[user_id] not in reportDict:
            finalset.add(user_id)
    #print (finalDict)
    #print (finalset)
    return finalset

def getTotalSpending():
    report = generateReportForAllUsers()
    cost = 0
    for user in report:
        count, newcost = report[user]
        cost = newcost + cost
    #print (cost)
    return cost

def main():
    print ('hi')
    print (generateReportForAllViruses())
    print (generateReportForAllUsers())
    print (RefStrainSummaryReport())
    print (getTotalSpending())

if __name__ == "__main__":
    main()
