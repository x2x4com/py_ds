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

from random import randint
from .decorator import count_run_time


@count_run_time
def random_int_array(l: int) -> list:
    """
    生成一个指定或者随机长度的数组，并在内填充不重复的数字

    :param l:
    :return:
    """
    assert type(l) == int
    x = list()
    if l == 0:
        l = randint(1000, 2000)
    # print("Create a list, l = %d" % l)
    for _i in range(l):
        # print("number %d" % _i)
        d = randint(1, l*2)
        while d in x:
            # print("%d in x" % d)
            d = randint(1, l*2)
        x.append(d)
        # print(x)
    return x


@count_run_time
def test_for_range(l: int=0):
    # if l < 100000:
    #    l = 100000
    y = 0
    x = 0
    for _i in range(l):
        # y = _i + 1
        x += _i
    return x, y


@count_run_time
def test_while(l: int=0):
    # if l < 100000:
    #     l = 100000
    """
    测试结果，在<=10**5下，

    :param l:
    :return:
    """
    y = 0
    x = 0
    while x < l:
        # y += x
        x += 1
    return x, y
