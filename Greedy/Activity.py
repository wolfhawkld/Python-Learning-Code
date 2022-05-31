# 活动使用同一会议室，时间可能出现重叠，需尽可能安排更多活动
# | Acts | act1 | act2 | act3 | act4 | act5 | act6 |
# | (s)  |  1   |  3   |  0   |  5   |  3   |  7   |
# | (f)  |  3   |  4   |  4   |  7   |  6   |  8   |
# 分析后得出贪心选择标准：最早结束

# 冒泡排序算法,将活动集合按结束时间进行排序
def bubble_sort(s, f):
    for i in range(len(f)):
        for j in range(0, len(f) - 1 - i):
            if f[j] > f[j+1]:
                f[j], f[j+1] = f[j+1], f[j]
                s[j], s[j+1] = s[j+1], s[j]
    return s, f


# 根据输入值构造活动数据
def init_acts(arr):
    if len(arr) == 0:
        global s, f
        s = [0, 3, 1, 5, 3, 7]
        f = [4, 4, 3, 7, 6, 8]
        return s, f
    else:
        for ar in arr:
            ar = ar[1:-1]
            start = int(ar.split(',')[0])
            end   = int(ar.split(',')[1])
            s.append(start)
            f.append(end)
        return s, f


# 贪心算法实现
def greedy(s, f, n):
    a = [True for x in range(n)]
    # 初始选择第一个活动
    j = 0
    for i in range(1, n):
        # 如果下一个活动开始时间大于等于上一个活动结束时间
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
    return a

# 6(回车)   
# (1,3) (3,4) (0,4) (5,7) (3,6) (7,8)
n = int(input("请输入活动数量及s-f时间(活动数量与s-f用回车分隔, s-f间用空格分隔, 如不输入s-f, 则按6个活动默认构造数据)"))
arr = input().split()

s = []
f = []
s, f = init_acts(arr)
s, f = bubble_sort(s, f)
A = greedy(s, f, n)
res = []
for k in range(len(A)):
    if A[k]:
        res.append('({},{})'.format(s[k], f[k]))
print(' '.join(res))
