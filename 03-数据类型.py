#数据类型
#数值 int（整型） float（浮点型）
#布尔型 True False
#字符串 str
#列表   list
#元组   tuple
#集合   set
#字典   dict
"""
1.将不同的变量存储不同的类型的数据

2.验证这些数据是什么类型 -- 检测数据类型 -- type(数据)

"""

# int -- python整数类型
# float -- 浮点数，就是小数

num1 = 1
num2 = 1.1
type(num1)
print(type(num1))
print(type(num2))

# str -- 字符串，特点：数据都要带引号
a = 'hello world'
print(type(a))

# bool -- 布尔型，通常判断使用，布尔型有两个取值 True 和 False
b = True
print(type(b))

# list -- 列表
c = [10,20,30]
print(type(c))

# tuple -- 元组
d = (10,20,30)
print(type(d))

# set -- 集合
e = {10,20,30}
print(type(c))