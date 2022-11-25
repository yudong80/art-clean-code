def bubblesort_clever(l):
    for boundary in range(len(l)-1, 0, -1):
        for i in range(boundary):
            l[i], l[i+1] = (l[i+1], l[i]) if l[i] > l[i+1] else (l[i], l[i+1])
    return l

l = [5, 3, 4, 1, 2, 0]
print(bubblesort_clever(l))
# [0, 1, 2, 3, 4, 5]