# Large Integer Multiplation
def mul(a, b):
    N = 3 # 大整数拆分位数限制，到此数字时则开始实际计算，不再二分大整数
    if len(b) > len(a): # 确保位数大的数乘位数小的数
        a, b = b, a
    if(len(a) <= N):    # 递归结束条件，一个数只要能被二分为3位数，则回溯
        return str(int(a) * int(b))
    mid = len(a)//2 # 二分大数,取整
    a1 = a[:mid]    # 高位部分，后面需补零
    a2 = a[mid:]
    return add(mul(a1, b) + "0" * len(a2), mul(a2, b))


def add(a, b):
    return str(int(a) + int(b))


a = input("请输入一个大整数a=")
b = input("请输入一个大整数b=")
w = mul(a, b)
print(w)
