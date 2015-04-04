#$Author: ee364f03 $
#$Date: 2015-03-04 10:50:17 -0500 (Wed, 04 Mar 2015) $
#$Revision: 77308 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Lab07/Laboratory.py $
class Experiment:

    def __init__(self, experimentNo, experimentDate, virusName, unitCount, unitCost):
        self.experimentNumber = experimentNo
        self.experimentDate = experimentDate
        self.virusName = virusName
        self.unitCount = unitCount
        self.totalCost = unitCost * unitCount

    def __str__(self):
        exnum = '{0:03d}'.format((self.experimentNumber))
        excost = '{0:06.2f}'.format((self.totalCost))
        string = exnum + ', ' + self.experimentDate + ', $' + excost + ': ' + self.virusName
        return string

class Technician:

    def __init__(self, techName, techID):
        self.techName = techName
        self.techID = techID
        self.experiments = {}

    def __str__(self):
        numex = '{0:02d}'.format(len(self.experiments))
        string = self.techID + ', ' + self.techName + ': ' + numex + ' Experiments'
        return string

    def addExperiment(self, experiment):
        if(not (self.experiments).get(experiment.experimentNumber)):
            (self.experiments).update({experiment.experimentNumber:experiment})
        elif((self.experiments).get(experiment.experimentNumber)):
            self.experiments[experiment.experimentNumber] = experiment

    def generateTechActivity(self):
        experiment_list = []
        for ex_num in (self.experiments).keys():
            experiment_list.append(ex_num)
        experiment_list.sort()
        #print (experiment_list)
        activity_string = self.techID + ', ' + self.techName
        for ex in experiment_list:
            excost = '{0:06.2f}'.format((self.experiments[ex]).totalCost)
            exnum = '{0:03d}'.format(int(ex))
            activity_string = activity_string + '\n' + exnum + ', ' + (self.experiments[ex]).experimentDate + ', $' + excost + ': ' + (self.experiments[ex]).virusName

        return activity_string

    def loadExperimentsFromFile(self, fileName):
        with open(fileName, 'r') as myfile:
            lines = myfile.readlines()
            lines = lines[2:]
            experiments = []
            for line in lines:
                ex = line.split()
                experiments.append(ex)
            for experiment in experiments:
                newExp = Experiment(experiment[0], experiment[1], experiment[2], float(experiment[3]), float(experiment[4][1:]))
                self.addExperiment(newExp)            
        
class Laboratory:

    def __init__(self, labName):
        self.labName = labName
        self.technicians = {}

    def __str__(self):
        num_techs = '{0:02d}'.format(len(self.technicians))
        string = self.labName + ': ' + num_techs + ' Technicians'
        techid = []
        names = []
        for tech in self.technicians:
            techid.append(int((self.technicians[tech]).techID[0:4]))
        #print (techid)
        techid.sort()
        for i in techid:
            for techs in self.technicians:
                if((int(self.technicians[techs].techID[0:4])) == i):
                    names.append(techs)
        #print (names)
        for tech in names:
            numex = '{0:02d}'.format(len(self.technicians[tech].experiments))
            string = string + '\n' + self.technicians[tech].techID + ', ' + tech + ': ' + numex + ' Experiments'

        return string

    def addTechnician(self, technician):
        if(not (self.technicians).get(technician.techName)):
            (self.technicians).update({technician.techName:technician})
        elif((self.technicians).get(technician.techName)):
            self.technicians[technician.techName] = technician

    def generateLabActivity(self):
        tech = []
        for keys in self.technicians:
            print(keys)
            tech.append(keys)
        print (tech)
        tech.sort()
        string = ''
        for t in tech:
            #print (self.technicians[t])
            string = string + (self.technicians[t]).generateTechActivity() + '\n\n'
        return string

def main():
   # print ('hi')
    myExp = Experiment(123, '04/01/2015', 'ebola', 5.0, 5.0)
    myExp1 = Experiment(154, '04/01/2015', 'ebola2', 5.0, 5.0)
    #print (myExp)
    myTech = Technician('Irene Adler', '69069-29232')
    #print (myTech)
    myTech.addExperiment(myExp)
    myTech.addExperiment(myExp1)
    #print (myTech.experiments)
    a = myTech.generateTechActivity()
    #print(a)
    myTech1 = Technician('Anthony Kang', '123123123')
    myTech1.loadExperimentsFromFile('report 55926-36619.txt')
    myLab = Laboratory('Purdue')
    myLab.addTechnician(myTech)
    myLab.addTechnician(myTech1)
    #print (myLab)
    print (myLab.generateLabActivity())


if __name__ == "__main__":
    main()