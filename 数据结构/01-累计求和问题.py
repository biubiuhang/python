"""
完成从1到n的累加
设置累计变量=0
从1到n循环，逐次累加到累计变量
返回累计变量
"""
def sum0fN(n):
    theSum = 0
    for i in range (1,n+1):
        theSum = theSum + i
    return theSum

print(sum0fN(10))

# 比较程序的"好坏"，有更多因素
# 代码风格、可读性等
# 算法分析主要就是从计算资源消耗的角度来评判和比较算法
# 更高效利用计算资源，或者更少占用计算资源的算法就是好算法
# 从这个角度，前述两段程序实际上是基本相同的，它们都采用了一样的算法来解决累计求和问题

# python中有一个time模块，可以获取计算机系统当前时间
# 在算法开始前和结束后分别记录系统时间，即可得到运行时间

"""
# 记录当前时间，是一个浮点数

# 累计求和程序的运行时间检测
# 用time检测总运行时间
# 返回累计和，以及运行时间(秒)

"""
import time 

def sum0fN2(n):
    start = time.time()
    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end - start


for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum0fN2(10000))
