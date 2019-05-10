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


class Counter(object):
    c = 0

    def increment(self):
        self.c += 1

    def __str__(self):
        return str(self.c)


def fib(n, c):
    c.increment()
    if n < 3:
        return 1
    return fib(n-1, c) + fib(n-2, c)


p = 2
print("%12s%15s" % ("Problem Size", "Calls"))

for count in range(5):
    counter = Counter()

    fib(p, counter)

    print("%12d%15s" % (p, counter))
    p *= 2
