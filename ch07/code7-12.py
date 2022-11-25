def insert_sort(lst):    
    # 리스트가 비었는지 확인
    if not lst:
        return []

    # 정렬된 단일 원소 리스트로 시작
    new = [lst[0]]

    # 남은 원소 각각을 삽입
    for x in lst[1:]:
        i = 0
        while i<len(new) and x>new[i]:
            i = i + 1
        new.insert(i, x)
    
    return new

print(insert_sort([42, 11, 44, 33, 1]))
print(insert_sort([0, 0, 0, 1]))
print(insert_sort([4, 3, 2, 1]))