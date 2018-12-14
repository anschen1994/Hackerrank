#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author anschen
"""

class BinaryTree:
    """Binary tree class"""
    def __init__(self,rootkey):
        self.key = rootkey
        self.left = None
        self.right = None

    def insertLeft(self,newnode):
        """ insert left node """
        if self.left is None:
            self.left = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.left = self.left
            self.left = t

    def insertRight(self,newnode):
        """ insert right node """
        if self.right is None:
            self.right = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.right = self.right
            self.right = t

    def getLeft(self):
        """return left node"""
        return self.left

    def getRight(self):
        """return right node"""
        return self.right

    def getRoot(self):
        """return root key"""
        return self.key

    def reSetRoot(self,obj):
        """reset root key"""
        self.key = obj
        return
