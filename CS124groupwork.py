  
class NumList:
    def __init__(self, target):
        if target[0] == "-":
            self.sign = False
        else:
            self.sign=True
        self.num = str2list(target)
    
    def printNum(self):
        print(list2str(self.num, self.sign))
    
    def add(self, other):
        if self.sign and other.sign:
            self.num = addList(self.num, other.num)
        elif self.sign == False and other.sign == False:
            self.num = addList(self.num, other.num)
        elif self.sign == False and other.sign == True:
            if compare(self.num, other.num):
                self.sign = False
                self.num = subList(self.num, other.num)
            else:
                self.sign = True
                self.num = subList(other.num, self.num)
        elif self.sign == True and other.sign == False:
            if compare(self.num, other.num):
                self.sign = True
                self.num = subList(self.num, other.num)
            else:
                self.sign = False
                self.num = subList(other.num - self.num)
                    
    def sub(self, other):
        if self.sign and other.sign:
            if compare(self.num, other.num):
                self.sign = True
                self.num = subList(self.num, other.num)
            else:
                self.sign = False
                self.num = subList(other.num, self.num)
        elif self.sign == False and other.sign == False:
            if compare(self.num, other.num):
                self.sign = False
                self.num = subList(self.num, other.num)
            else:
                self.sign = True
                self.num = subList(other.num, self.num)
        elif self.sign == False and other.sign == True:
            self.num = addList(self.num, other.num)
        elif self.sign == True and other.sign == False:
            self.num = addList(self.num, other.num)

    def mul(self, other):
        pass

    def div(self, other):
        pass

    def pow(self, power):
        pass

def addList(a, b): # adds two positive numlists
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

def subList(a, b): # substracts a small positive list number from a big one
    pass

def str2list(stri): #turns a string number into a list, adds a bool as the first element to state if it's pos
    lst = []
    if stri[0] == "-":
        for i in stri[-1: 0: -1]:
            lst.append(int(i))
    else:
        for i in stri[-1:: -1]:
            lst.append(int(i))
    return lst

def list2str(lst, sign): #turns a list number into a string
    if sign== False:
        return "-" + "".join(str(i) for i in lst[-1: :-1])
    else:
        return "".join(str(i) for i in lst[-1: :-1])

def compare(a, b): #returns 1 if a is bigger , -1 if b is bigger , 0 if a == b
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    else:
        for i in range(len(a)):
            if a[-1 * i] < b[-1 * i]:
                return True
            elif a[-1 * i] > b[-1 * i]:
                return False
        return True