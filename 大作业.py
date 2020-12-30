from copy import deepcopy

class NumList:
    def __init__(self, target):
        if target[0]=="-":
            self.sign=False
        else:
            self.sign=True
        self.num = str2list(target)
    
    def __str__(self):
        return list2str(self.num, self.sign)
    
    def __add__(self, other):
        sm = NumList("0")
        if self.sign and other.sign:
            sm.num = addList(self.num, other.num)
            sm.sign = True
        elif self.sign == False and other.sign == False:
            sm.num = addList(self.num, other.num)
            sm.sign = False
        elif self.sign == False and other.sign == True:
            if compare(self.num, other.num):
                self.sign = False
                sm.num = subList(self.num, other.num)
            else:
                self.sign = True
                sm.num = subList(other.num, self.num)
        elif self.sign == True and other.sign == False:
            if compare(self.num, other.num):
                self.sign = True
                sm.num = subList(self.num, other.num)
            else:
                self.sign = False
                sm.num = subList(other.num ,self.num)
        if sm.num == [0]:
            sm.sign = True
        return sm
                    
    def __sub__(self, other):
        mina = NumList("0")
        if self.sign and other.sign:
            if compare(self.num, other.num):
                mina.sign = True
                mina.num = subList(self.num, other.num)
            else:
                mina.sign = False
                mina.num = subList(other.num, self.num)
        elif self.sign == False and other.sign == False:
            if compare(self.num, other.num):
                mina.sign = False
                mina.num = subList(self.num, other.num)
            else:
                mina.sign = True
                mina.num = subList(other.num, self.num)
        elif self.sign == False and other.sign == True:
            mina.sign = False
            mina.num = addList(self.num, other.num)
        elif self.sign == True and other.sign == False:
            mina.sign = True
            mina.num = addList(self.num, other.num)
        if mina.num ==[0]:
            mina.sign = True
        return mina

    def __mul__(self, other):
        prod = NumList("0")
        if self.sign and other.sign:
            prod.sign = True
            prod.num = mulList(self.num, other.num)
        elif self.sign == False and other.sign == False:
            prod.num = mulList(self.num, other.num)
            prod.sign = True
        else:
            prod.num = mulList(self.num,other.num)
            prod.sign = False
        if prod.num == [0]:
            prod.sign = True
        return prod

    def __truediv__(self, other):
        quo = NumList("0")
        if self.sign and other.sign:
            quo.sign = True
            quo.num = divList(self.num, other.num)
        elif self.sign == False and other.sign == False:
            quo.num = divList(self.num, other.num)
            quo.sign = True
        else:
            quo.num = divList(self.num,other.num)
            quo.sign = False
        if quo.num == [0]:
            quo.sign = True
        return quo

    def __pow__(self, power):
        result = NumList("0")
        if self.sign:
            result.sign = True
            result.num = powList(self.num,power.num)
        elif self.sign==False and power.num[0]%2==0:
            result.sign = True
            result.num = powList(self.num,power.num)
        elif self.sign ==False and power.num[0]%2==1:
            result.sign = False
            result.num = powList(self.num,power.num)
        return result

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

def subList(t, b): # substracts a small positive list number from a big one
    result=[]
    a = deepcopy(t)
    for i in range(len(b)):
        if a[i] < b[i]:
            a[i] += 10
            a[i + 1] -= 1
        result.append(a[i] - b[i])
    for i in range(len(b), len(a)):
        if a[i]<0:
            a[i] += 10
            a[i+1] -= 1
        result.append(a[i])
    while len(result)>1:
        if result[-1]==0:
            result.pop()
        else:
            break
    return result

def mulList(a, b): #multiplies two numlists
    result = []
    carryFlag = 0
    for i in range(len(b)):
        temp = [0] * i + []
        carryFlag = 0
        for j in range(len(a)):
            newDigit = a[j] * b[i] + carryFlag
            carryFlag = newDigit // 10
            newDigit = newDigit % 10
            temp.append(newDigit)
        if carryFlag > 0:
            temp.append(carryFlag)
        result = addList(result, temp)
    if result[-1] == 0:
        return [0]
    return result

def divList(a, b):
    result = []
    lenb = len(b)
    if lenb == 1:
        remainder = []
    else:
        remainder = a[-lenb + 1:]
    if compare(a, b) == False:
        return [0]
    for i in range(len(a) - lenb + 1):
        newDigit = 0
        currNum = b
        dividedNum = [a[-lenb - i]] + remainder 
        while compare(dividedNum, currNum):
            currNum = addList(currNum, b)
            newDigit = newDigit + 1
        remainder = subList(b, subList(currNum, dividedNum))
        result = [newDigit] + result
        if remainder == [0]:
            remainder = []
    if result[-1] == 0:
        result.pop(-1)
    return result

def powList(a,b):
    if b==[0]:
        return [1]
    elif b==[1]:
        return a
    elif b==[2]:
        return mulList(a,a)
    elif b[0]%2==0:
        return mulList(powList(a,divList(b,[2])),powList(a,divList(b,[2])))
    elif b[0]%2==1:
        return mulList(mulList(powList(a,divList(b,[2])),powList(a,divList(b,[2]))),a)

def str2list(stri): #turns a string number into a list
    lst=[]
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

def compare(a, b): #returns True if a >= b
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    else:
        for i in range(len(a)):
            if a[-i - 1] > b[-i - 1]:
                return True
            elif a[-i - 1] < b[-i - 1]:
                return False
        return True 

a = NumList("-1234567")
b = NumList("325")
print(a ** b)
    


