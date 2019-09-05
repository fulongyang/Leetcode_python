# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 11:07
# @Author  : yangfulong
# @FileName: 链表.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/

--------------------- 
版权声明：
原文链接：
"""


'''
根据结构的不同，链表可以分为单向链表、单向循环链表、双向链表、双向循环链表等。
在Python中，则可以采用“引用+类”来实现链表。

链表的主要功能包括：节点的增加、删除和查询，返回链表的长度，返回链表是否为空等。

必须连续，动态改变，

[200]

[400]

[600]


[200][ox34]  [600][0x21]    [数据区][地址区，下一个节点的位置] 
        [400][ox21]          [数据区][]
        
链表操作
    add(item)     链表头部添加元素
    append(item)  链表尾部添加元素
    insert(pos,item) 指定位置添加元素
    
    remove(item)  删除节点，删除找到的第一个节点
    
    length()      链表的长度
    travel()      遍历整个链表
    search(item)  查找节点是否存在
    is_empty()    链表是否为空

理解：
    链表的数据结构由数据区和地址区组成
    第一个节点叫头节点
    尾结点地址区会保存一个特殊的符号
    

'''

#实现链表类

# 节点类
class Node(object):
    # 初始化，需要传入节点的数据
    def __init__(self, data):
        self.data = data
        self.next = None

    # 返回节点的数据
    def get_data(self):
        return self.data

    # 更新节点的数据
    def set_data(self, new_data):
        self.data = new_data

    # 返回后继节点
    def get_next(self):
        return self.next

    # 变更后继节点
    def set_next(self, new_next):
        self.next = new_next



class Linked_list(object):
    # 初始化，头结点为空
    def __init__(self,node=Node):
        self.head = node

    # 添加节点，添加的新节点作为新的头结点
    def add(self, data):
        #将节点类进行赋值
        new_node = Node(data)
        #将节点类中的地址位置设置成头节点 [200][none]
        new_node.set_next = self.head
        #节点类赋值给头节点  ? 这个将类赋值给参数是什么意思  1.指向第一个节点
        self.head = new_node


    # 包含查询，传入值，返回该值在链表中是否存在
    def search(self, data):
        checking = self.head  # 从头结点开始查询
        while checking != None:
            if checking.get_data() == data:  # 查找到，返回True
                return True
            checking = checking.get_next()  # 查询下一个节点
        return False  # 遍历到最后也未能找到，返回False

    # 删除节点，将第一个具有传入值的节点从链表中删除
    def remove(self, data):
        checking = self.head  # 从头结点开始查询
        previous = None  # 记录前一个节点，头结点的前一个节点为None
        while checking != None:
            if checking.get_data() == data:  # 查找到，跳出查找循环
                break
            previous = checking  # 更新前一个节点
            checking = checking.get_next()  # 查询下一个节点

        if previous == None:  # 如果头结点便是查找的节点
            self.head = checking.get_next()

        else:  # 查找的节点不在头结点，即，存在前驱节点
            previous.set_next(checking.get_next())


    # 判断链表是否为空
    def isEmpty(self):
        return self.head == None



    # 返回链表长度
    def travel(self):
        count = 0
        counting = self.head  # 从头结点开始计数
        while counting != None:
            count += 1
            counting = counting.get_next()
        return count

    #链表尾部添加元素
    def append(self,item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head = None
            while cur.next != None:
                cur = cur.next
            cur.next = node




if __name__ == "__main__":
    LinkList = Linked_list()
    print(LinkList.isEmpty())

    LinkList.add('1')
    LinkList.add('2')
    LinkList.add('3')
    LinkList.add('4')

    print(LinkList.travel())











