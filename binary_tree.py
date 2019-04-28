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
    elem = None
    left = None
    right = None
    is_root = False

    def __init__(self, elem=None, left=None, right=None, root=False):
        self.elem = str(elem)
        self.left = left
        self.right = right
        self.is_root = root

    def __str__(self):
        return self.elem

    def __repr__(self):
        return '<Node %s @ 0x%016x>' % (self.elem, id(self))


class Tree(Node):
    """二叉树"""

    def __init__(self, root: Node=None):
        if root is not None:
            assert type(root) in [str, int], "%s not str or int" % root
            super().__init__(elem=root, root=True)

    def __str__(self):
        # if hasattr(self, 'elem'):
        if self.elem is not None:
            return self.elem
        return self.__repr__()

    def __repr__(self):
        # if hasattr(self, 'elem'):
        if self.elem is not None:
            return '<Tree %s @ 0x%016x>' % (self.elem, id(self))
        return '<Empty Tree @ 0x%016x>' % id(self)

    def p_add(self, l: list):
        for _l in l:
            self.add(_l)

    def add(self, e):
        """
        为二叉树添加元素

        :param e: 添加元素
        :return:
        """
        assert type(e) in [str, int], "%s not str or int" % e

        # 如果树是空的，则对根节点赋值
        if self.elem is None:
            self.elem = str(e)
            self.is_root = True
            # self.left = node.left
            # self.right = node.right
            return

        node = Node(e)
        queue = list()
        queue.append(self)
        while queue:
            # print(queue)
            # 弹出队列的第一个元素
            c = queue.pop(0)
            # print('弹出队列的第一个元素, %s' % c.elem)
            if c.left is None:
                # print('左节点为空，设置%s' % node)
                c.left = node
                return
            if c.right is None:
                # print('右节点为空，设置%s' % node)
                c.right = node
                return
            # 如果左右子树都不为空，往判断列表加入子树，循环进行子树的判断
            queue.append(c.left)
            queue.append(c.right)
            # print("左右子树都不为空，将左右节点加入队列, l=%s, r=%s" % (c.left.elem, c.right.elem))


def pre_order_recursive(node: Node, level=0, d='root', ret: list=None, silent=True):
    """递归实现先序遍历"""
    if ret is None:
        ret = list()

    if node is None:
        return ret

    ret.append(node.elem)
    if not silent:
        if d == 'left':
            print('%d - Left: %s' % (level, node.elem))
        elif d == 'right':
            print('%d - Right: %s' % (level, node.elem))
        else:
            print("ROOT: %s" % node.elem)
    level += 1
    ret = pre_order_recursive(node.left, level, 'left', ret=ret)
    ret = pre_order_recursive(node.right, level, 'right', ret=ret)
    return ret


def in_order_recursive(node: Node, level=0, d='root', ret: list=None, silent=True):
    """递归实现中序遍历"""
    if ret is None:
        ret = list()

    if node is None:
        return ret

    level += 1
    ret = in_order_recursive(node.left, level, 'left', ret=ret)
    ret.append(node.elem)
    if not silent:
        if d == 'left':
            print('%d - Left: %s' % (level, node.elem))
        elif d == 'right':
            print('%d - Right: %s' % (level, node.elem))
        else:
            print("ROOT: %s" % node.elem)
    ret = in_order_recursive(node.right, level, 'right', ret=ret)
    return ret


def post_order_recursive(node: Node, level=0, d='root', ret: list=None, silent=True):
    """递归实现后序遍历"""
    if ret is None:
        ret = list()

    if node is None:
        return ret

    level += 1
    ret = post_order_recursive(node.left, level, 'left', ret=ret)
    ret = post_order_recursive(node.right, level, 'right', ret=ret)
    ret.append(node.elem)
    if not silent:
        if d == 'left':
            print('%d - Left: %s' % (level, node.elem))
        elif d == 'right':
            print('%d - Right: %s' % (level, node.elem))
        else:
            print("ROOT: %s" % node.elem)
    return ret


def breadth_travel(node):
    """利用队列实现树的层次遍历"""
    if node is None:
        return
    q = list()
    q.append(node)
    while q:
        n = q.pop(0)
        print(node.elem)
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

    return q

