# 计算导论大作业：无限制整数
## 原理
## 使用指南
### 主要变量名
- **target**  *str* 输入的数
- **self.sign** *bool* 符号
- **self.num** *list* 倒叙存储数的每位数字
- **other** *class* 用于运算的其他数
- **sm** *class* 加法的结果
- **mina** *class* 减法的结果
- **prod** *class* 乘法的结果
- **qu** *class* 整除的结果
### 方法名
- **\_\_init\_\_(self, target)**
- **\_\_str\_\_(self)**
- **\_\_add\_\_(self, other)**
- **\_\_sub\_\_(self, other)**
- **\_\_mul\_\_(self, other)**
- **\_\_truediv\_\_(self, other)**
- **\_\_pow\_\_(self, power)**
### 函数
- **addList(a, b)**
- **subList(t, b)**
- **mulList(a, b)**
- **divList(a, b)**
- **powList(a, b)**
- **str2list(stri)**
- **list2str(lst, sign)**
- **compare(a, b)**
