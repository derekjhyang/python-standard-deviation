#!/usr/bin/env python


def std(list):
    """
        here we use 'standard deviation' to determine whether the system load is balanced,
        where the sys_load value is small better.
    """
    avg = sum(list)/float(len(list))
    return math.sqrt(sum(map(lambda x: (x-avg)**2,list))/len(list))
