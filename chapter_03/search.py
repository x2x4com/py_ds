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

from comm.decorator import count_run_time


@count_run_time
def index_of_min(lyst: list) -> int:
    """
    3.3.1 搜索最小值

    :param lyst:
    :return:
    """
    min_index = 0
    current_index = 1
    while current_index < len(lyst):
        if lyst[current_index] < lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index


@count_run_time
def index_of_max(lyst: list) -> int:
    """
    3.3.1 拓展 搜索最大值

    :param lyst:
    :return:
    """
    max_index = 0
    current_index = 1
    while current_index < len(lyst):
        if lyst[current_index] > lyst[max_index]:
            max_index = current_index
        current_index += 1
    return max_index


@count_run_time
def sequential_search(t, lyst: list) -> int:
    """
    3.3.2 顺序搜索一个列表

    :param t:
    :param lyst:
    :return:
    """
    _p = 0
    while _p < len(lyst):
        if t == lyst[_p]:
            return _p
        _p += 1
    return -1


@count_run_time
def binary_search(t, sorted_list: list) -> int:
    """
    3.3.4 二叉树搜索，要求列表是排序过的

    :param t:
    :param sorted_list:
    :return:
    """
    print(t >= sorted_list[0])
    if t < sorted_list[0] or t > sorted_list[-1]:
        raise ValueError("%d <= t <= %d" % (sorted_list[0], sorted_list[-1]))
    left = 0
    right = len(sorted_list) - 1
    _count = 1
    print("搜索开始，left = %d, right = %d" % (left, right))
    while left <= right:
        print("第%d次搜索" % _count)
        # 整除
        mid = (left + right) // 2
        print("中间数为%d，值为%d" % (mid, sorted_list[mid]))
        if t == sorted_list[mid]:
            print("第%d次找到了%d" % (_count, t))
            return mid
        elif t < sorted_list[mid]:
            right = mid - 1
            print("%d < %d, set right = %d (%d - 1)" % (
                t, sorted_list[mid], right, mid))
        else:
            left = mid + 1
            print("%d > %d, set left = %d (%d + 1)" % (
                t, sorted_list[mid], left, mid))
        _count += 1
    raise ValueError("sorted_list not sorted")

