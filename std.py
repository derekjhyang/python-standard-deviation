#!/usr/bin/env python


def std(list):
    avg = sum(list)/float(len(list))
    return math.sqrt(sum(map(lambda x: (x-avg)**2,list))/len(list))
