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

