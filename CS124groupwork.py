class NumList:
    def __init__(self, num):
        self.num = str2list(num)
    
    def printNum(self):
        print(list2str(self.num))
    
    def add(self, other):
        pass

    def sub(self, other):
        pass

    def mul(self, other):
        pass

    def div(self, other):
        pass

    def pow(self, power):
        pass

def str2list(stri): #turns a string number into a list, adds a False as the first element to state if it's neg
    if stri[0] == "-":
        lst = [False]
        for i in stri[1:]:
            lst.append(int(i))
    else:
        lst = []
        for i in stri:
            lst.append(int(i))
    return lst

def list2str(lst): #turns a list number into a string
    if type(lst[0]) == bool:
        return "-" + "".join(str(i) for i in lst[1:])
    else:
        return "".join(str(i) for i in lst)