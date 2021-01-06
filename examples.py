import longinteger
'''
22222222222222+8773849905050505
11111111-9877344555
345676778778-222222
123456*789
8773849905050505//123
2**66
2**100+3**50
2*100 +123456*789-8773849905050505//123
'''
test={'+':['22222222222222','8773849905050505'],
'-':['11111111','9877344555'],
'*':['123456','789'],
'//':['8773849905050505','123'],
'**':['2','66']}

for i in test:
    a=longinteger.NumList(test[i][0])
    b=longinteger.NumList(test[i][1])
    print(test[i][0],i,test[i][1],'=',str(eval('a'+i+'b')))

a1=longinteger.NumList('2')
b1=longinteger.NumList('100')
c1=longinteger.NumList('3')
d1=longinteger.NumList('50')
print('2**100+3**50 = ',end='')
print(a1**b1+c1**d1)

a2=longinteger.NumList('2')
b2=longinteger.NumList('100')
c2=longinteger.NumList('123456')
d2=longinteger.NumList('789')
e2=longinteger.NumList('8773849905050505')
f2=longinteger.NumList('123')
print('2*100 +123456*789-8773849905050505//123 = ',end='')
print(a2 * b2 + c2 * d2 - e2 // f2)