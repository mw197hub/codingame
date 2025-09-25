# https://www.codingame.com/ide/puzzle/binary-search-tree-traversal

import sys,math

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    @property
    def left(self):
        return self.left
    @left.setter
    def left(self, left):
        self.left = left
    @property
    def right(self):
        return self.right
    @right.setter
    def right(self, right):
        self.right = right


#####

viList=[135, 151, 128, 13, 201, 260, 158, 195]

#####
root = Node(viList.pop(0))
if viList[0] < root.data:
    rootL = Node(viList[0])

