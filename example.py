import csv
from collections import OrderedDict
from parsing import parsing
from approximate_algorithms import normalize

def numberofparents(node):
    CPTs["parents"]={"AN":None,"PP":None,"YF":None,"BED":None,"S":"AN,PP,YF","G":None,"LC":"S,G","AD":"G","AL":None,"CO":"AL,LC","F":"CO,LC","CA":"F,AD"}
    if CPTs["parents"][node] == None:
        number = 0
        parents = 0
    elif len(CPTs["parents"][node].split(',')) == 1:
        number = len(CPTs["parents"][node].split(','))
        parents = CPTs["parents"][node].split(',')
    else:
        number = len(CPTs["parents"][node].split(','))
        parents = CPTs["parents"][node].split(',')
    return number , parents

def count(list):
    pos = 0
    neg = 0
    for i in range(len(list)):
        if "+" == list[i]:
            pos = pos + 1
        else:
            neg = neg + 1
    return pos,neg,len(list)


def findprob(sign,numberofparents=0,list1=[],list2=[],list3=[]):
    if numberofparents == 0:
        pos,neg,size = count(list1) 
        pos_prob = (pos + 1)/(size+2)
        neg_prob = (neg + 1)/(size+2)
    x = OrderedDict()
    x["+"] = pos_prob
    x["-"] =neg_prob
    x=normalize(x)
    return x["+"],x["-"]





CPTs={}
CPTs["AN"]={"+an":None,"-an":None}
CPTs["PP"]={"+pp":None,"-pp":None}
CPTs["BED"]={"+bed":None,"-bed":None}

CPTs["G"]={"+g":None,"-g":None}
CPTs["S"]={"+s|+an+pp":None,"+s|+an-pp":None,"+s|-an+pp":None,"+s|-an-pp":None,"-s|+an+pp":None,"-s|+an-pp":None,"-s|-an+pp":None,"-s|-an-pp":None}
CPTs["YF"]={"+yf|+s":None, "+yf|-s":None,"-yf|+s":None, "-yf|-s":None}

CPTs["AL"]={"+al":None,"-al":None}
CPTs["LC"]={"+lc|+s+g":None,"+lc|-s+g":None,"+lc|+s-g":None,"+lc|-s-g":None,"-lc|+s+g":None,"-lc|-s+g":None,"-lc|+s-g":None,"-lc|-s-g":None}
CPTs["AD"]={"+ad|+g":None,"+ad|-g":None,"-ad|+g":None,"-ad|-g":None}

CPTs["CO"]={"+co|+al+lc":None,"+co|-al+lc":None,"+co|+al-lc":None,"+co|-al-lc":None,"-co|+al+lc":None,"-co|-al+lc":None,"-co|+al-lc":None,"-co|-al-lc":None}
CPTs["F"]={"+f|+co+lc":None,"+f|-co+lc":None,"+f|+co-lc":None,"+f|-co-lc":None,"-f|+co+lc":None,"-f|-co+lc":None,"-f|+co-lc":None,"-f|-co-lc":None}
CPTs["CA"]={"+ca|+f+ad":None,"+ca|-f+ad":None,"+ca|+f-ad":None,"+ca|-f-ad":None,"-ca|+f+ad":None,"-ca|-f+ad":None,"-ca|+f-ad":None,"-ca|-f-ad":None}

CPTs["order"]=["AN","PP","YF","BED","S","G","LC","AD","AL","CO","F","CA"]
CPTs["parents"]={"AN":None,"PP":None,"YF":None,"BED":None,"S":"AN,PP,YF","G":None,"LC":"S,G","AD":"G","AL":None,"CO":"AL,LC","F":"CO,LC","CA":"F,AD"}

pairing = {
    'Smoking': 'S',
    'Yellow_Fingers': 'YF',
    'Anxiety': 'AN',
    'Peer_Pressure': 'PP',
    'Genetics': 'G',
    'Attention_Disorder': 'AD',
    'Born_an_Even_Day': 'BED',
    'Car_Accident': 'CO',
    'Fatigue': 'F',
    'Allergy': 'AL',
    'Coughing': 'CA',
    'Lung_cancer': 'LC',
}
allData = []

with open('lucas0_train.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    title = next(csv_reader)
    for num, item in enumerate(title):
        title[num] = pairing[item]
    print(title)

    for row in csv_reader:
        row[:] = ["+" if x == '1' else "-" for x in row]
        allData.append(dict(zip(title, row)))
print(CPTs["parents"])

for node in CPTs['parents']:
    print(node,numberofparents(node))

list=[]
for i in range(len(allData)):
    list.append(allData[i]["PP"])

number , parents = numberofparents("PP")
print("CPTs[PP][+pp] and CPTs[PP][-pp]",findprob("+",number,list))

for node in CPTs['parents']:
    number , parents = numberofparents(node)
    print(node,number,parents)
    if number == 0:
        pos,neg=findprob("+",number,list)
        for cond in CPTs[node]:
            print(node,cond)
number , parents = numberofparents("YF")
print(CPTs["parents"]["YF"],number)