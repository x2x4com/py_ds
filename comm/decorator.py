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
from functools import wraps


def count_run_time(func):
    """
    计时修饰器

    :param func:
    :return:
    """
    @wraps(func)
    def _func(*args, **kwargs):
        _start = time.time()
        rt = func(*args, **kwargs)
        print("[func: %s] cost @%.6fs" % (func.__name__, time.time() - _start))
        return rt
    return _func
