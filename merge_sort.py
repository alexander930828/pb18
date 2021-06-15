def merge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])
    # 두 그룹을 하나로 병합
    result = []  # 두 그룹을 합쳐 만들 최종 결과
    while g1 and g2: # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞자료 값을 비교
            # g1 값이 더 작으면 그 값을 빼내어 결과로추가
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    # 아직 남아 있는 자욜들은 결과에 추가
    # g1과g2중 이미 빈 것은 while을 바로 지나감
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))