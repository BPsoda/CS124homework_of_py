class NumList:
    def __init__(self, target):
        if target[0]=="-":
            self.sign=False
        else:
            self.sign=True
        self.num = str2list(target)
    
    def __str__(self):
        return list2str(self.num,self.sign)
    
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

    def __div__(self, other):
        pass

    def __pow__(self, power):
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
    result=[]
    for i in range(len(b)):
        if a[i]<b[i]:
            a[i]+=10
            a[i+1]-=1
        result.append(a[i]-b[i])
    for i in range(len(b),len(a)-1):
        if a[i]<0:
            a[i]+=10
            a[i+1]-=1
        result.append(a[i])
    while len(result)>1:
        if result[-1]==0:
            result.pop()
        else:
            break
    return result

def mulList(a,b): #multiplies two numlists
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

def str2list(stri): #turns a string number into a list
    lst=[]
    if stri[0] == "-":
        for i in stri[-1: 0: -1]:
            lst.append(int(i))
    else:
        for i in stri[-1:: -1]:
            lst.append(int(i))
    return lst

def list2str(lst,sign): #turns a list number into a string
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
            if a[-1 * i] > b[-1 * i]:
                return True
            elif a[-1 * i] < b[-1 * i]:
                return False
        return True 