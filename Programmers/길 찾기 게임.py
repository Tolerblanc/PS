import sys

def solution(nodeinfo):
    nodes = sorted([(x, y, (i + 1)) for i, (x, y) in enumerate(nodeinfo)], key = lambda x : x[0])
    answer = [[], []]
    sys.setrecursionlimit(100001)
    
    def traversal(nodes):
        if not nodes:
            return
        
        root = (0, -1, 0) #idx, y, nodeIndex
        for i, node in enumerate(nodes):
            if root[1] < node[1]:
                root = (i, node[1], node[2])
        
        answer[0].append(root[2])
        traversal(nodes[:root[0]]) #left Subtree
        traversal(nodes[root[0] + 1:]) #right Subtree
        answer[1].append(root[2])
    
    traversal(nodes)
    return answer