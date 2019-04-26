#!/usr/bin/env python
# encoding: utf-8
# ===============================================================================
#
#         FILE:
#
#        USAGE:
#
#  DESCRIPTION:
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  YOUR NAME (),
#      COMPANY:
#      VERSION:  1.0
#      CREATED:
#     REVISION:  ---
# ===============================================================================


class Node(object):
    """二叉树节点"""
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree(object):
    """二叉树"""

    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                    return
                elif cur.right is None:
                    cur.right = node
                    return
                else:
                    # 如果左右子树都不为空，往判断列表加入子树，循环进行子树的判断
                    queue.append(cur.left)
                    queue.append(cur.right)

    @staticmethod
    def pre_order(node):
        """递归实现先序遍历"""
        if node is None:
            return
        print(node.elem)
        Tree.pre_order(node.left)
        Tree.pre_order(node.right)

    @staticmethod
    def in_order(node):
        """递归实现中序遍历"""
        if node is None:
            return
        Tree.in_order(node.left)
        print(node.elem)
        Tree.in_order(node.right)

    @staticmethod
    def post_order(node):
        """递归实现后续遍历"""
        if node is None:
            return
        Tree.post_order(node.left)
        Tree.post_order(node.right)
        print(node.elem)

    @staticmethod
    def breadth_travel(node):
        """利用队列实现树的层次遍历"""
        if node is None:
            return
        queue = list()
        queue.append(node)
        while queue:
            n = queue.pop(0)
            print(node.elem)
            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)
