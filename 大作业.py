class NumList:
    def __init__(self, target):
        if target[0]=="-":
            self.sign=False
        else:
            self.sign=True
        self.num = str2list(target)
    
    def printNum(self):
        print(list2str(self.num,self.sign))
    
    def add(self, other):
        if self.sign and other.sign:
            self.num = addList(self.num, other.num)
            self.sign=True
        elif self.sign == False and other.sign == False:
            self.num = addList(self.num, other.num)
            self.sign=False
        else:
            pass
            

        
    def sub(self, other):
        pass

    def mul(self, other):
        pass

    def div(self, other):
        pass

    def pow(self, power):
        pass

def addList(a, b): # add two positive numlists(without the initial bool)
    result = []
    carryFlag = False
    for i in range(min(len(a), len(b))):
        newDigit = a[i] + b[i] + carryFlag
        if newDigit >= 10:
            newDigit = newDigit - 10
            carryFlag = True
        else:
            carryFlag = False
        result.append(newDigit)
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            newDigit = a[i] + carryFlag
            if newDigit >= 10:
                newDigit = newDigit - 10
                carryFlag = True
            else:
                carryFlag = False
            result.append(newDigit)
    elif len(b) > len(a):
        for i in range(len(a), len(b)):
            newDigit = b[i] + carryFlag
            if newDigit >= 10:
                newDigit = newDigit - 10
                carryFlag = True
            else:
                carryFlag = False
            result.append(newDigit)
    if carryFlag == True:
        result.append(1)
    return result

def subList(a, b):
    pass

def str2list(stri): #turns a string number into a list, adds a bool as the first element to state if it's pos
    if stri[0] == "-":
        lst=[]
        for i in stri[-1: 0: -1]:
            lst.append(int(i))
    else:
        lst=[]
        for i in stri[-1:: -1]:
            lst.append(int(i))
    return lst

def list2str(lst,sign): #turns a list number into a string
    if sign== False:
        return "-" + "".join(str(i) for i in lst[-1: :-1])
    else:
        return "".join(str(i) for i in lst[-1: :-1])