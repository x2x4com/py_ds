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

problem_size = 10000000
print("%12s%16s" % ('Problem size', 'Seconds'))

for c in range(10):
    start = time.time()

    work = 1

    for x in range(problem_size):
        work += 1
        work -= 1

    e = time.time() - start

    print("%12d%16.3f" % (problem_size, e))

    problem_size *= 2
