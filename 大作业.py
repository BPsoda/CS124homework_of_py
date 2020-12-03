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
        if sum==[0]:
            return [0]
        sum.append(self.sign)
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
        if mina ==[0]:
            return [0]
        mina.append(self.sign)
        return mina

    def mul(self, other):
        if self.sign and other.sign:
            prod= mulList(self.num, other.num)
        elif self.sign == False and other.sign == False:
            prod = mulList(self.num, other.num)
            self.sign=True
        else:
            prod=mulList(self.num,other.num)
            self.sign=False
        if prod[-1] ==0:
            return [0]
        prod.append(self.sign)
        return prod

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
    result=[]
    carryFlag=0
    for i in range(len(b)):
        temp=[0]*i+[]
        carryFlag=0
        for j in range(len(a)):
            newDigit=a[j]*b[i]+carryFlag
            carryFlag=newDigit//10
            newDigit=newDigit%10
            temp.append(newDigit)
        if carryFlag>0:
            temp.append(carryFlag)
        result=addList(result,temp)
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

def compare(a, b): #returns True if a is bigger , False if b is bigger 
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
n=NumList("1000")
t=NumList("-923")
print(n.add(t))