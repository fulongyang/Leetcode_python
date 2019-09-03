






"""
#定义好节点类
#默认节点为空，利用重写构造函数的策略，使得每次定义一个节点，
#对应节点都包含了元素，左右儿子。
"""
class Node(object):#新式类
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild





"""
#定义树类
#每颗树的构造函数都会初始化一个根节点
#并且会利用层序的策略定义添加节点构建已知树函数
"""
class Tree(object):
    def __init__(self, root=None):
        self.root = root
        self.MyQueue = []
    #把一个节点添加到树中的策略（层序）
    def add(self,elem):
        #定义一个带有给定元素elem的节点
        node = Node(elem)
        if self.root.elem == -1:#如果树是空的
            self.root = node #那么当前节点就是根节点
            self.MyQueue.append(self.root)#并把当前根节点放入自己构造的队列中
        #如果当前树为非空
        else:
            #把当前队列中的第一个节点取出来
            treeNode = self.MyQueue[0]
            #如果取出的节点没有左子树，则把当前节点赋值给取出节点的左子树,
            #并将该节点加入到自制对列中（因为后续还要给该节点添加左右子树）
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.MyQueue.append(treeNode.lchild)
            #如果取出的节点已经有左子树了，那就把当前节点赋值给其右子树
            #并将该节点加入到自制对列中（因为后续还要给该节点添加左右子树）
            #而和左子树插入不同，右子树插入后，当前被取出节点就被填满了（因为是二叉树），
            #所以该被取出节点需要从自制队列中弹出（注意这就是用对列不用栈的原因：先进先出）
            else:
                treeNode.rchild = node
                self.MyQueue.append(treeNode.rchild)
                self.MyQueue.pop(0)



if __name__ == '__main__':
    tree = Tree()
    tree.add('A')
    tree.add('B')
    tree.add('C')
    tree.add('D')
    tree.add('E')
    tree.add('F')
    tree.add('G')






