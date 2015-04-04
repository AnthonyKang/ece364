#$Author: ee364f03 $
#$Date: 2015-03-25 11:18:28 -0400 (Wed, 25 Mar 2015) $
#$Revision: 78251 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Lab09/typeDict.py $
class Entry:

    def __init__(self, k=0, v=''):
        if(type(k) is not int):
            raise TypeError('key must be an integer')
        if(type(v) is not str):
            raise TypeError('value must be a string')     
        self.key = k
        self.value = v

    def __str__(self):
        string = '(' + str(self.key) + ': "' + self.value + '")'
        return string

    def __hash__(self):
        t = (self.key, self.value)
        return hash(t)

class Lookup:

    def __init__(self, name):
        
        if(len(name) <= 0):
            raise ValueError('Name can not be empty')
        
        self._name = name
        self._entrySet = set()

    def __str__(self):
        return '["' + self._name + '": ' + str('{0:02d}'.format((len(self._entrySet)))) + ' Entries]' 

    def addEntry(self, entry):
        for curr_entry in self._entrySet:
            if(entry.key is curr_entry.key):
                raise ValueError("Entry already exists")
        else:
            self._entrySet.add(entry)

    def updateEntry(self, entry):
        set_keys = []
        for curr_entry in self._entrySet:
            if(entry.key is curr_entry):
                (self._entrySet).remove(curr_entry)
            set_keys.append(curr_entry.key)
        if(entry.key not in set_keys):
            raise KeyError('entry not in set')
        (self._entrySet).add(entry)

    def addOrUpdateEntry(self, entry):
        set_keys = []
        for curr_entry in self._entrySet:
            set_keys.append(curr_entry.key)
        #print(set_keys)
        if (entry.key in set_keys):
            self.updateEntry(entry)
        else:
            self.addEntry(entry) 

    def removeEntry(self, entry):
        set_keys = []
        for curr_entry in self._entrySet:
            set_keys.append(curr_entry.key)
        if(entry.key not in set_keys):
            raise KeyError('Entry does not exist')
        else:
            (self._entrySet).remove(entry)

    def getEntry(self, entry):
        for curr_entry in self._entrySet:
            if(curr_entry.key == entry.key):
                return curr_entry
        raise KeyError('Entry does not exist') 

    def addOrUpdateFromDictionary(self, someDict):
        for item in someDict:
            my_entry = Entry(item, someDict[item])
            self.addOrUpdateEntry(my_entry)

    def getAsDictionary(self):
        mydict = {}
        myentries = []
        for curr_entry in self._entrySet:
            mydict.update({curr_entry.key:curr_entry.value})
        
        
        return mydict

    def getKeys(self):
        set_keys = []
        for curr_entry in self._entrySet:
            set_keys.append(int(curr_entry.key))
        return sorted(set_keys)

    def getValues(self):
        set_values = []
        for curr_entry in self._entrySet:
            set_values.append(curr_entry.value)
        return sorted(set_values)

    def getElementCount(self):
        return len(self._entrySet)

def main():
    #print(type(3))

    my_entry = Entry(8, 'Anthony')
    print(my_entry)

    my_lookup = Lookup('my_lookup')
    print(my_lookup)
    my_lookup.addEntry(my_entry)
    print(my_lookup)
    my_entry1 = Entry(9, 'hi')
    my_entry2 = Entry(10, 'asd')
    my_lookup.addEntry(my_entry1)
    my_lookup.updateEntry(my_entry)
    my_lookup.addOrUpdateEntry(my_entry2)
    print(my_lookup)
    my_lookup.removeEntry(my_entry)
    print(my_lookup)
    print(my_lookup.getEntry(my_entry2))
    my_lookup.addOrUpdateFromDictionary({1:'as',2:'boobs'})
    print(my_lookup)
    print(my_lookup.getAsDictionary())
    a = my_lookup.getKeys()
    print(a)
    print(my_lookup.getValues())
   

if __name__ == "__main__":
    main()