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

import time

problem_size = 1000
print("%12s%15s%16s" % ('Problem size', 'Iterations', 'Seconds'))

for c in range(5):
    n = 0
    start = time.time()

    work = 1

    for x in range(problem_size):
        for y in range(problem_size):
            n += 1
            work += 1
            work -= 1

    e = time.time() - start

    print("%12d%15d%16.3f" % (problem_size, n, e))

    problem_size *= 2
