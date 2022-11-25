import matplotlib.pyplot as plt
import math
import time
import random


def bubblesort(l):
    # 소스: https://blog.finxter.com/daily-python-puzzle-bubble-sort/
    lst = l[:] # Work with a copy, don’t modify the original
    for passesLeft in range(len(lst)-1, 0, -1):
        for i in range(passesLeft):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def qsort(lst):
    # 설명: https://blog.finxter.com/python-one-line-quicksort/
    q = lambda lst: q([x for x in lst[1:] if x <= lst[0]]) \
                    + [lst[0]] \
                    + q([x for x in lst if x > lst[0]]) if lst else []
    return q(lst)


def timsort(l):
    # 팀 정렬은 내부적으로 sorted()을 사용
    return sorted(l)


def create_random_list(n):
    return random.sample(range(n), n)


n = 500
xs = list(range(1, n, n//10))
y_bubble = []
y_qsort = []
y_tim = []

for x in xs:
    # 리스트를 생성
    lst = create_random_list(x)

    # 버블 정렬 시간 측정
    start = time.time()
    bubblesort(lst)
    y_bubble.append(time.time()-start)
    
    # 퀵 정렬 시간 측정
    start = time.time()
    qsort(lst)
    y_qsort.append(time.time()-start)

    # 팀 정렬 시간 측정
    start = time.time()
    timsort(lst)
    y_tim.append(time.time()-start)

plt.plot(xs, y_bubble, '-x', label='Bubblesort')
plt.plot(xs, y_qsort, '-o', label='Quicksort')
plt.plot(xs, y_tim, '--.', label='Timsort')
plt.grid()
plt.xlabel('List Size (No. Elements)')
plt.ylabel('Runtime (s)')
plt.legend()
plt.savefig('alg_complexity_new.pdf')
plt.savefig('alg_complexity_new.jpg')
plt.show()
