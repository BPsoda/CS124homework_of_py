# 计算导论大作业：无限制整数
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
组员：  刘忱锴 520030910010  山澍 520030910011  黄浩栩520030910014  
本次作业实现的主要功能是无限长度的整数运算  
**longinteger**为主模组，**examples**包含了所有测试用例  
该项目已在github上开源[戳这里](https://github.com/BPsoda/CS124homework_of_py/tree/sumission)
***
## 使用指南
### 主要变量名
- **target**  *str* 输入的数
- **self.sign** *bool* 符号
- **self.num** *list* 倒序存储数的每位数字
- **other** *class* 用于运算的其他数
- **sm** *class* 加法的结果
- **mina** *class* 减法的结果
- **prod** *class* 乘法的结果
- **qu** *class* 整除的结果
### 方法名
- **\_\_init\_\_(self, target)**  初始化变量
- **\_\_str\_\_(self)**  print时调用**list2str**直接输出字符串
- **\_\_add\_\_(self, other)** 重载“+”
- **\_\_sub\_\_(self, other)** 重载“-”
- **\_\_mul\_\_(self, other)** 重载“*”
- **\_\_floordiv\_\_(self, other)** 重载“//”
- **\_\_pow\_\_(self, power)** 重载“**”

### 函数
- **str2list(stri)** 将字符串转化为列表
- **list2str(lst, sign)** 将列表转化为字符串
- **addList(a, b)** 列表加法（不带符号，下同）
- **subList(t, b)** 列表减法
- **mulList(a, b)** 列表乘法
- **divList(a, b)** 列表除法
- **powList(a, b)** 列表幂次
- **compare(a, b)** 比较两个数的大小，$a \geq b$时输出True

### 使用步骤
- 将数添加到类中
``` python
a = longinteger.NumList('2')
b = longinteger.NumList('100')
```
- 按一般方法进行运算，得到的结果也属于这个类
``` python
c = a * b
```
- print输出结果时，自动调用**\_\_str\_\_**，显示正常的字符
``` python
print(c)
#output:200
```
***
## 原理
- 初始化变量  
  我们将一个数分为符号（sign）和数字（num）两个部分。
  $$ -123456 \rightarrow False,[6,5,4,3,2,1]$$
  我们规定0的符号为True
- 加法  
  1. 判断符号  
  (1) 若符号相同，保留原符号，调用**addList**进行列表加法  
  (2) 若符号不同,先调用**compare**判别两个列表数字的大小，取用较大数的符号，再调用**subList**进行列表减法  

  2. 列表加法 addList  
  根据我们小学二年级学过的竖式加法  

    1 2 3 4  
    <u>+ &nbsp; 3 9</u>  
    1 2 7 3  
    进位 1

  注意到第一位相加大于10，需进位。我们用**carryFlag**表示是否需要进位  
  3. 列表减法 subList  
  与加法类似，但在被减数不够大时需向下一位借一，直接在下一位减去1.  
  完成减法后，可能会出现许多不需要的0（如1111-1110=0001）。用while循环，当列表数的长度大于1时，删去最后的0。  

- 减法  
  与加法类似，只是在判断符号，调用**addList**与**subList**时相反 
 
- 乘法
  1. 判断符号  
   符号相同取正，相反取负
  2. 列表乘法  mulList    
   ![multiple](1.png "乘法竖式")  
    每行结果保存到列表**temp**中，预先加上i个0，i对应行数减一。  
    对乘数每个数字进行乘法，进位保存在**carryFlag**中。乘完最后一位后若**carryFlag**不等于0，则将它加到最后一位。  
    将**temp**和**result**进行列表加法

- 除法  
  1. 判断符号  
   符号相同取正，相反取负  
  2. 列表除法  divList
   - 若$a<b$,直接返回0
   - **remainder**表示当前步除完的余数，初始值为被除数的前 len(b)-1 位。  
   - **Newdigit**表示当前在计算的商的某一位
   - **dividednum**表示当前步正在被除的数 ，由**remainder**和被除数的下一位构成 
   - **currnum**表示当前除数的n倍
   - 对于每个**dividenum**将其与**currnum**进行比较。若**dividenum**>**currnum**,则**currnum**由除数的n倍变为n+1倍；若**dividenum**$\leq$**currnum**，则n为最终的**Newdigit**，转到下一位继续以上步骤。  
  ![divide](2.png "除法竖式")  
   - 我们注意到最终结果可能包含首位0，因此依然需要将其删去  

- 幂次  
  1. 判断符号  
   若底数为正，则符号取正  
   若底数为负，则考虑幂的奇偶性。奇数取负，偶数取正。  
  2. 列表快速幂 powlist  
   - 对于幂为0，1，2分别直接输出$1,a,a^2$  
   - 若b为偶数，则有： 
    $$a^b=a^{b/2} \times a^{b/2}$$  
   - 若b为奇数，则有：  
    $$a^b=a^{(b-1)/2} \times a^{(b-1)/2} \times a$$  
   - 对$a^b$或$a^{(b-1)/2}$进行递归，直至变成$1,a,a^2$  
   - 由此可将时间复杂度由$O(n)$变为$O(\log_2n)$  

- 比较列表数大小  
  1. 比较长度，长度大的数较大  
  2. 若两者长度相同，则由高位开始逐位比较


     
 
