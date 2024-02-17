from collections import deque
import sys
jobs = deque(list(map(int, input().split(", "))))
index = int(input())
cycles = 0

cpu_found = False

while cpu_found == False:

    min_num = min(jobs)
    min_num_index = jobs.index(min_num)
    cycles += min_num
    jobs[min_num_index] = 500
    if min_num_index == index:
        cpu_found = True

print(cycles)