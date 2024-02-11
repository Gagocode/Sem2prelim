import random

class person:
    
    def __init__(self,name,age,sex,number) -> None:
        self._name = name
        self._age = age
        self._sex = sex
        self._number = number
    
    def getname(self):
        return self._name
    
    def getage(self):
        return self._age
    
    def getsex(self):
        return self._sex
    
    def getnum(self):
        return self._number
    
    def gb(self):
        i = random.randint(1,3)
        if i == 1:
            print('Goodbye Nurse')
        elif i == 2:
            print('Thank you for your service')
        elif i == 3:
            print('Thank god im discrage!')
    
    def hello(self):
        i = random.randint(1,3)
        if i == 1:
            print('Hello nurse')
        elif i == 2:
            print('Good day to you')
        elif i == 3:
            print('I think I have a sickness')

class patient(person):
    
    def __init__(self, name, age, sex, number, emnumber, relative, relationrelative, chargeby, dateofcharge) -> None:
        super().__init__(name, age, sex, number)
        self._emnumber = emnumber
        self._relative = relative
        self._relationrelative = relationrelative
        self._chargeby = chargeby
        self._dateofcharge = dateofcharge
    
    def getemnum(self):
        return self._emnumber
    
    def getrelative(self):
        return self._relative
    
    def getrelation(self):
        return self._relationrelative
    
    def getchargeby(self):
        return self._chargeby
    
    def getchargedate(self):
        return self._dateofcharge
    
    def charged(self):
        i = random.randint(1,3)
        if i == 1:
            print('I\'ll be goin to my room now, Thank you')
        elif i == 2:
            print('Thank you!')
        elif i == 3:
            print('Okay, ill go to my room now have a nice day')
    
    def ischarge(self):
        print(f'{self._name} is now charge with {self._chargeby} in this hostpital')

class patientdischarged(patient):
    
    def __init__(self, name, age, sex, number, emnumber, relative, relationrelative, chargeby, dateofcharge, dateofdischarge, dischargeby) -> None:
        super().__init__(name, age, sex, number, emnumber, relative, relationrelative, chargeby, dateofcharge)
        self._dateofdischarge = dateofdischarge
        self._discargeby = dischargeby
    
    def getdateofdischarge(self):
        return self._dateofdischarge
    
    def getdiscargeby(self):
        return self._discargeby
    
    def discharge(self):
        if self._discargeby == 'DECEASED':
            print('Patient is deceased')
        else:
            print('Patient is now feeling well')