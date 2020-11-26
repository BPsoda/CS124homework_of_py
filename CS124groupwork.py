class NumList:
    def __init__(self, num):
        self.num = str2list(num)
    
    def printNum(self):
        print(list2str(self.num))
    
    def add(self, other):
        if self.num[0] and other.num[0]:
            self.num = [True] + addList(self.num[1:], other.num[1:])
        elif self.num[0] == False and other.num[0] == False:
            self.num = [False] + addList(self.num[1:], other.num[1:])

        
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
        lst = [False]
        for i in stri[-1: 0: -1]:
            lst.append(int(i))
    else:
        lst = [True]
        for i in stri[-1:: -1]:
            lst.append(int(i))
    return lst

def list2str(lst): #turns a list number into a string
    if lst[0] == False:
        return "-" + "".join(str(i) for i in lst[-1: 0: -1])
    else:
        return "".join(str(i) for i in lst[-1: 0: -1])