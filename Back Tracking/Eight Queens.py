# 在8*8的棋盘上放置8枚皇后，使得棋盘中每个纵向、横向、左上至右下斜向、右上至左下斜向均只有一枚皇后

# 判断下一行皇后是否与此前皇后在同一列或同一对角线上
def conflict(state, nextColumn):
    '''
    判断是否冲突
    因为坐标是从0开始，所以state长度代表下一行的行坐标
    :param state: 如果用(7, 4, 6, 0, 2)标记每行皇后所在位置，则皇后坐标为:(0, 7), (1, 4), (2, 6), (3, 0), (4, 2)
    :param nextColumn:下一行皇后的列坐标
    :return: 是否冲突
    '''
    nextRow = rows = len(state)
    for row in range(rows):
        column = state[row]
        '''
        判断冲突：
        1. 列差值为0，则为同列冲突
        2. 列差值=行差值，则为对角线冲突
        '''
        if abs(column - nextColumn) in [0, nextRow - row]:
            return True
    return False


# 生成器产生每个皇后的位置，并用递归实现回溯算法计算每种结果的皇后位置
def queens(num, state=()):
    '''
    基于递归实现回溯算法，算出每种n皇后的可能结果
    :param num: 皇后数量
    :param state: 皇后列坐标，初始为空，参数为元组(不可变序列)
    :return: 返回yield函数式的迭代器
    '''
    # 按列遍历: 0 -> num-1
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1: # 到达倒数第二行,返回最后一行皇后的列坐标pos
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    # 自顶向下递归
                    yield (pos,) + result


# 友好界面展示棋盘，画出每种结果的皇后位置
def prettyprint(solution):
    '''
    X表示皇后，O表示空格
    :param solution: 元组形式的棋盘皇后数据
    :return:
    '''
    def line(pos, length=len(solution)):
        return 'O ' * (pos) + 'X ' + 'O ' * (length - pos -1)


    for pos in solution:
        print(line(pos))


# main流程调用各函数
if __name__ == '__main__':
    solutions = queens(8)
    for index, solution in enumerate(solutions):
        print('第%d种解决方案：' %(index + 1), solution)
        prettyprint(solution)
        print('*' * 50)
