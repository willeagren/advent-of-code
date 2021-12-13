"""Template for the adventofcode package pipeline.
Replace answer=None with your solution.
"""
import time
import sys
import fileinput as fi

from collections import defaultdict

def fold_y(mapping, pos):
    keys = list(k for k in mapping.keys())
    for x,y in keys:
        if y > pos:
            newpos = y-pos
            mapping[(x,pos-newpos)] = True
            mapping = dict(mapping)
            del mapping[(x,y)]
    return mapping

def fold_x(mapping, pos):
    keys = [k for k in mapping.keys()]
    for x,y in keys:
        if x > pos:
            newpos = x-pos
            mapping[(pos-newpos,y)] = True
            mapping = dict(mapping)
            del mapping[(x,y)]
    return mapping

def run(data, io_time):
    t_start = time.perf_counter_ns()
    mapping = defaultdict(bool)
    splits = []
    for line in data:
        linelen = len(line)
        if linelen == 0:
            continue
        if linelen < 11:
            x,y = line.split(',')
            mapping[(int(x),int(y))] = True
        elif linelen >= 11:
            where = line.split(' ')[2]
            pos, amnt = where.split('=')
            splits.append((pos, int(amnt)))

    pos, amnt = splits[0]
    if pos == 'y':
        mapping = fold_y(mapping, amnt)
    if pos == 'x':
        mapping = fold_x(mapping, amnt)

    """
    for (x,y), val in mapping.items():
        if val:
            print(x,y)
    """
    marked = sum(map(lambda x: int(x), mapping.values()))
    answer = marked
    t_end = time.perf_counter_ns()
    sys.stdout.write(f'{answer} {io_time} {t_end-t_start}')

if __name__ == '__main__':
    t_start = time.perf_counter_ns()
    data = list(line.rstrip() for line in fi.input())
    t_stop = time.perf_counter_ns()
    run(data, t_stop-t_start)

