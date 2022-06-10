import sys
sys.path.append("..")
from Local_lib import logo_print

# Single Source Short Path, 单源最短路径
'''
在有向图G.PNG中，每一边都有一个非负边权。要求图G的从源顶点s到目标顶点t之间的最短路径
BFS搜索树见BFS.PNG
输入：
vertex=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edge=[[0,1,2],[0,2,3],[0,3,4],[1,2,3],[1,4,7],[1,5,2],[2,5,9],[2,6,2],[3,6,2],[4,7,2],[4,8,3],[5,6,1],[5,8,3],[6,8,5],[6,9,1],[7,10,1],[8,10,2],[9,8,2],[9,10,2]]
s=0
t=10
输出：8
'''
import sys, queue, copy

class PathNode(object):
    def __init__(self, path, x, length):
        self.path = path
        self.label = x
        self.length = length


    # 由于PriorityQueue优先级队列实现堆进行操作，因此需要有__xt__方法
    def __gt__(self, other):
        return self.length > other.length


def ShortestPath(vertexset, edgeset, s, t):
    # 构建邻接矩阵
    vertexNum = len(vertexset)
    adjmat = [([sys.maxsize] * vertexNum) for i in range(vertexNum)]
    edgeNum = len(edgeset)
    # 对邻接矩阵赋值
    for i in range(edgeNum):
        adjmat[edgeset[i][0]][edgeset[i][1]] = edgeset[i][2]
    
    # 初始化优先队列
    q = queue.PriorityQueue()
    res = None
    for i in range(vertexNum):
        if i != s and adjmat[s][i] != sys.maxsize:
            q.put(PathNode([s], i, adjmat[s][i]))
    # 寻找最短路径
    while not q.empty():
        # 剪枝操作
        cur = q.get()
        while res != None and cur.length >= res.length:
            if not q.empty():
                cur = q.get()
            else:
                cur = None
                break
        if cur == None:
            continue

        # 访问到目的节点，则记录当前的最短路径
        if cur.label == t:
            res = cur

        # 将当前节点的相邻节点放入队列中
        for i in range(vertexNum):
            if i != cur.label and adjmat[cur.label][i] != sys.maxsize:
                tmp = copy.deepcopy(cur.path)
                tmp.append(cur.label)
                q.put(PathNode(tmp, i, cur.length + adjmat[cur.label][i]))  

    res.path.append(t)
    print('Shortest path length:%d, node order:%s'%(res.length, res.path))
    return res

logo_print.Print()
vertex=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edge=[[0,1,2],[0,2,3],[0,3,4],[1,2,3],[1,4,7],[1,5,2],[2,5,9],[2,6,2],[3,6,2],[4,7,2],[4,8,3],[5,6,1],[5,8,3],[6,8,5],[6,9,1],[7,10,1],[8,10,2],[9,8,2],[9,10,2]]
s=0
t=10
ShortestPath(vertex, edge, s, t)    
