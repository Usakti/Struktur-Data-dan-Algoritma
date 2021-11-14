# -*- coding: utf-8 -*-
"""
@Materi: AVL Tree
@Judul: Praktikum 9 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
 
class AVLTree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
     
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        if T2 == None:
            var = "None"
        else:
            var = T2.val
        print("Tadinya", z.val, "root dari unbalance node")
        print("kemudian", z.val, "menjadi kanannya dari", y.val)
        print("lalu", var, "menjadi kirinya dari", z.val, "\n")
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
     
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        if T3 == None:
            var = "None"
        else:
            var = T3.val
        print("Tadinya", z.val, "root dari unbalance node")
        print("kemudian", z.val, "menjadi kanannya dari", y.val)
        print("lalu", var, "menjadi kirinya dari", z.val, "\n")
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def preOrder(self, root):
        if not root:
            return
        print("{0} ". format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

NayTree = AVLTree()
root = None
angka = [13, 10, 15, 5, 11, 16, 4, 8, 3]
for num in angka:
    root = NayTree.insert(root, num)
print("Preorder traversal of the constructed AVL Tree is:")
NayTree.preOrder(root)
