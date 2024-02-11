from person import patientdischarged
from person import patient
from person import person
from datetime import date
import csv
import re

def mainmenu():
    print('============= JED Hospital =============\n')
    print('[1] Enter Patient')
    print('[2] Discharge Patient')
    print('[3] Records')
    print('[0] Exit\n')

def chargepatient():
    print('============= Charge a patient =============\n')
    name = str(input('\nEnter Person\'s Name : '))
    
    age = str(input('\nEnter Person\'s age : '))
    while checkcharacters(age):
        print('Invalid Input')
        age = str(input('\nEnter Person\'s age : '))
    
    sex = str(input('\nEnter Person\'s Sex [F/M] : '))
    while sex not in ['M', 'F']:
        print('Invalid Input')
        sex = str(input('\nEnter Person\'s Sex [F/M] : '))
        
    number = str(input('\nEnter Person\'s Number : '))
    while checkcharacters(number):
        print('Invalid Input')
        number = str(input('\nEnter Person\'s Number : '))
    person_ = person(name,age,sex,number)
    
    person_.hello()
    
    emnum = str(input('\nEnter Person\'s Emergence Number : '))
    while checkcharacters(emnum):
        print('Invalid Input')
        emnum = str(input('\nEnter Person\'s Emergence Number : '))
    
    relative = str(input('\nEnter Person\'s Owner of Emrgency Number : '))
    relation = str(input('\nEnter Person\'s Relation : '))
    chargeby = str(input(f'\n{person_.getname()} is being charge in the hospital with : '))
    date_ = date.today().strftime("%B %d, %Y")
    
    with open('patients.csv', 'a', newline='') as file:
        wrt = csv.writer(file, delimiter=',')
        data = [name,age,sex,number,emnum,relative,relation,date_,chargeby]
        wrt.writerow(data)
    
    newpatient = patient(name,age,sex,number,emnum,relative,relation,chargeby,date_)
    
    print()
    newpatient.ischarge()
    newpatient.charged()
    print()

def checkcharacters(inputed:str) -> bool:
    
    notallnum = False
    for cha in inputed:
        if re.match('\d', cha):
            continue
        else:
            notallnum = True
            break
    
    return notallnum

def dischargepatient():
        while True:
            with open('patients.csv', 'r') as file:
                readfile = csv.DictReader(file)
                Data = list(readfile)
                patients = [i['NAME'] for i in Data]
                
                def removepatient(tobedischarged):
                    patient_ = None
                    
                    for p in Data:
                        if p['NAME'] == tobedischarged:
                            patient_ = patient(
                                p['NAME'],p['AGE'],p['SEX'],p['NUMBER'],
                                p['EMERGENCYNUMBER'],p['EMERGENCYNUMBEROWNER'],
                                p['RELATIONSHIPWITHENO'],p['DATEOFCHARGE'],
                                p['CHARGEDBY']
                                )
                    print(f'============= {patient_.getname()} =============\n')
                    print(f'Patient\'s Name : {patient_.getname()}')
                    print(f'Patient\'s Age : {patient_.getage()}')
                    print(f'Patients\'s Sex : {patient_.getsex()}')
                    print(f'Patient\'s Health issue : {patient_.getchargeby()}')
                    
                    print('\nEnter [0] to exit')
                    print('[1] Disharge by Health Restored')
                    print('[2] Disharge by Deceadse')
                    dischargedby = str(input('\n>> '))
                    while dischargedby not in ['2', '1', '0']:
                        print('Invalid Input')
                        print('\nEnter [0] to exit')
                        dischargedby = str(input('\n>> '))
                    
                    if dischargedby == '0':
                        return
                    elif dischargedby == '1':
                        dischargedby = 'Health Restored'
                    elif dischargedby == '2':
                        dischargedby = 'Deceadse'
                    
                    date_ = date.today().strftime("%B %d, %Y")
                    Person_ = patientdischarged(
                        patient_.getname(), patient_.getage(), patient_.getsex(), patient_.getnum(),
                        patient_.getemnum(), patient_.getrelative(), patient_.getrelation(),
                        patient_.getchargeby(), patient_.getchargedate(), dischargedby, date_
                    )
                    
                    NewData = []
                    for i in Data:
                        if i['NAME'] == Person_.getname():
                            continue
                        NewData.append(i)
                    
                    with open('patientsdischarge.csv', 'a', newline='') as dfile:
                        dwrt = csv.writer(dfile, delimiter=',')
                        dwrt.writerow([
                            Person_.getname(), Person_.getage(), Person_.getsex(), Person_.getnum(),
                            Person_.getemnum(), Person_.getrelative(), Person_.getrelation(),
                            Person_.getchargedate(), Person_.getchargeby(), Person_.getdateofdischarge(),
                            Person_.getdiscargeby()
                        ])
                    
                    with open('patients.csv', 'w', newline='') as newfile:
                        field = [
                            'NAME','AGE','SEX','NUMBER','EMERGENCYNUMBER',
                            'EMERGENCYNUMBEROWNER','RELATIONSHIPWITHENO','DATEOFCHARGE',
                            'CHARGEDBY','DISCHARGEBY','DATEOFDISCHARGE'
                            
                        ]
                        wrt = csv.DictWriter(newfile, fieldnames=field, delimiter=',')
                        wrt.writeheader()
                        wrt.writerows(NewData)
                    
                    Person_.discharge()
                    
                    if Person_.getdiscargeby() == 'Health Restored':
                        Person_.gb()
                
                
                print('========================== Discharge a patient ==========================\n')
                print('[1] Search   |[0] Exit\n')
                
                if len(patients) % 4 == 0:
                    for i in range(0,len(patients),4):
                        print(f'[{i+2}] {patients[i]}   [{i+3}] {patients[i+1]}    [{i+4}] {patients[i+2]}  [{i+5}] {patients[i+3]}')
                elif len(patients) % 3 == 0:
                    for i in range(0,len(patients),3):
                        print(f'[{i+2}] {patients[i]}   [{i+3}] {patients[i+1]}    [{i+4}] {patients[i+2]}')
                elif len(patients) % 2 == 0:
                    for i in range(0,len(patients),2):
                        print(f'[{i+2}] {patients[i]}   [{i+3}] {patients[i+1]}')
                elif len(patients) % 1 == 0:
                    for i, p in enumerate(patients):
                        print(f'[{i+2}] {p}')
                
                
                Input = str(input('\n>> '))
                while Input not in [str(i) for i in range(0,len(patients)+2)]:
                    print('Invalid Input')
                    Input = str(input('\n>>'))
                
                tobedischarged = None
                
                if Input == '0':
                    break
                elif Input == '1':
                    searchpatient = str(input('Search patient : '))
                    tobedischarged = searchingpatient(searchpatient)
                    while type(tobedischarged) is None:
                        print('No Result, Enter [0] to exit')
                        searchpatient = str(input('Search patient : '))
                        if searchpatient == '0':
                            tobedischarged = None
                            break
                        tobedischarged = searchpatient(searchpatient)
                else:
                    tobedischarged = patients[int(Input)-2]
                
                if type(tobedischarged) is None:
                    continue
                elif type(tobedischarged) is str:
                    removepatient(tobedischarged)
                    continue
                elif type(tobedischarged) is list:
                    print(f'============= Result =============\n')
                    print('[0] Exit\n')
                    if len(tobedischarged) % 4 == 0:
                        for i in range(0,len(tobedischarged),4):
                            print(f'[{i+1}] {tobedischarged[i]}   [{i+2}] {tobedischarged[i+1]}    [{i+3}] {tobedischarged[i+2]}  [{i+4}] {tobedischarged[i+3]}')
                    elif len(tobedischarged) % 3 == 0:
                        for i in range(0,len(tobedischarged),3):
                            print(f'[{i+1}] {tobedischarged[i]}   [{i+2}] {tobedischarged[i+1]}    [{i+3}] {tobedischarged[i+2]}')
                    elif len(tobedischarged) % 2 == 0:
                        for i in range(0,len(tobedischarged),2):
                            print(f'[{i+1}] {tobedischarged[i]}   [{i+2}] {tobedischarged[i+1]}')
                    elif len(patients) % 1 == 0:
                        for i, p in enumerate(tobedischarged):
                            print(f'[{i+1}] {p}')
                    
                    choosen = str(input('\n>> '))
                    while choosen not in [str(i) for i in range(0,len(tobedischarged)+1)]:
                        print('Invalid Input')
                        choosen = str(input('\n>> '))
                    
                    if choosen == '0':
                        continue
                    
                    patientperson = tobedischarged[int(choosen)-1]
                    removepatient(patientperson)
                    continue
            
def searchingpatient(name:str):
    with open('patients.csv', 'r') as file:
        readfile = csv.DictReader(file)
        Data = list(readfile)
        result = []
        
        for p in Data:
            if re.search(name, p['NAME'] , re.IGNORECASE) != None:
                result.append(p['NAME'])
        
        if len(result) == 0:
            return None
        elif len(result) == 1:
            return result[0]
        elif len(result) > 1:
            return result
          
def record():
    while True:
        print('================== Records ==================\n')
        print('[1] Current Patients')
        print('[2] Discharged Patients')
        print('[0] Exit')
        
        Input = str(input('\n>> '))
        while Input not in ['0', '1', '2']:
            print('Invalid Input')
            Input = str(input('\n>> '))
        
        if Input == '0':
            break
        elif Input == '1':
            while True:
                with open('patients.csv', 'r') as file:
                    pread = csv.DictReader(file)
                    Data = list(pread)
                    print('========================================= Patients =========================================\n')
                    print('Name     Age     Sex     Number      Date of charge      Cost of Charge')
                    for i in Data:
                        print(f'{i['NAME']}     {i['AGE']}     {i['SEX']}     {i['NUMBER']}      {i['DATEOFCHARGE']}      {i['CHARGEDBY']}')
                    print('\n[0] Exit')
                    newInput = str(input('>> '))
                    while newInput != '0':
                        print('Invalid Input')
                        print('\n[0] Exit')
                        newInput = str(input('>> '))
                    if newInput == '0':
                        break
        elif Input == '2':
            while True:
                with open('patientsdischarge.csv', 'r') as file:
                    pread = csv.DictReader(file)
                    Data = list(pread)
                    print('============================================== Discharged Patients ==============================================\n')
                    print('Name     Age     Sex     Number      Date of charge      Cost of Charge          Date of discharge       Discharge by')
                    for i in Data:
                        print(f'{i['NAME']}     {i['AGE']}     {i['SEX']}     {i['NUMBER']}      {i['CHARGEDBY']}       {i['DATEOFCHARGE']}     {i['DATEOFDISCHARGE']}   {i['DISCHARGEBY']}')
                    print('\n[0] Exit')
                    newInput = str(input('>> '))
                    while newInput != '0':
                        print('Invalid Input')
                        print('\n[0] Exit')
                        newInput = str(input('>> '))
                    if newInput == '0':
                        break                      
                                
if __name__ == '__main__':
    while True:
        mainmenu()
        
        Input = str(input('>> '))
        
        while Input not in ['0','1','2','3']:
            print('Invalid Input\n')
            Input = str(input('>> '))
        
        match Input:
            case '0':
                print('Goodbye :)')
                break
            case '1':
                chargepatient()
                continue
            case '2':
                dischargepatient()
                continue
            case '3':
                record()
                continue