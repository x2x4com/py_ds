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
def index_of_min(lyst: list):
    min_index = 0
    current_index = 1
    while current_index < len(lyst):
        if lyst[current_index] < lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index


@count_run_time
def index_of_max(lyst: list):
    max_index = 0
    current_index = 1
    while current_index < len(lyst):
        if lyst[current_index] > lyst[max_index]:
            max_index = current_index
        current_index += 1
    return max_index


@count_run_time
def sequential_search(t, lyst: list):
    _p = 0
    while _p < len(lyst):
        if t == lyst[_p]:
            return _p
        _p += 1
    return -1


@count_run_time
def binary_search(t, lyst: list) -> int:
    print(t >= lyst[0])
    if t < lyst[0] or t > lyst[-1]:
        raise ValueError("%d <= t <= %d" % (lyst[0], lyst[-1]))
    left = 0
    right = len(lyst) - 1
    _count = 1
    print("搜索开始，left = %d, right = %d" % (left, right))
    while left <= right:
        print("第%d次搜索" % _count)
        # 整除
        mid = (left + right) // 2
        print("中间数为%d，值为%d" % (mid, lyst[mid]))
        if t == lyst[mid]:
            print("第%d次找到了%d" % (_count, t))
            return mid
        elif t < lyst[mid]:
            right = mid - 1
            print("%d < %d, set right = %d (%d - 1)" % (
                t, lyst[mid], right, mid))
        else:
            left = mid + 1
            print("%d > %d, set left = %d (%d + 1)" % (
                t, lyst[mid], left, mid))
        _count += 1
    raise ValueError("lyst not sorted")

