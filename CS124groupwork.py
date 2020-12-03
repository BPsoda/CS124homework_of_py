  
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
            sum = addList(self.num, other.num)
        elif self.sign == False and other.sign == False:
            sum = addList(self.num, other.num)
        elif self.sign == False and other.sign == True:
            if compare(self.num, other.num):
                self.sign = False
                sum = subList(self.num, other.num)
            else:
                self.sign = True
                sum = subList(other.num, self.num)
        elif self.sign == True and other.sign == False:
            if compare(self.num, other.num):
                self.sign = True
                sum = subList(self.num, other.num)
            else:
                self.sign = False
                sum = subList(other.num - self.num)
        return sum
                    
    def sub(self, other):
        if self.sign and other.sign:
            if compare(self.num, other.num):
                self.sign = True
                mina = subList(self.num, other.num)
            else:
                self.sign = False
                mina = subList(other.num, self.num)
        elif self.sign == False and other.sign == False:
            if compare(self.num, other.num):
                self.sign = False
                mina = subList(self.num, other.num)
            else:
                self.sign = True
                mina = subList(other.num, self.num)
        elif self.sign == False and other.sign == True:
            mina = addList(self.num, other.num)
        elif self.sign == True and other.sign == False:
            mina = addList(self.num, other.num)
        return mina

    def mul(self, other):
        pass

    def div(self, other):
        pass

    def pow(self, power):
        pass

def addList(a, b): # adds two positive numlists
    result = []
    carryFlag = 0
    for i in range(min(len(a), len(b))):
        newDigit = (a[i] + b[i] + carryFlag)%10
        carryFlag = (a[i] + b[i] + carryFlag)-newDigit
        result.append(newDigit)
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            newDigit = (a[i] + carryFlag)%10
            carryFlag = (a[i] + carryFlag)-newDigit
        result.append(newDigit)
    elif len(b) > len(a):
        for i in range(len(a), len(b)):
            newDigit = (b[i] + carryFlag)%10
            carryFlag = (b[i] + carryFlag)-newDigit
        result.append(newDigit)
    if carryFlag == 1:
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