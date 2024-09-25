def solution(distance, rocks, n):

    rocks.sort()
    rocks.append(distance)

    def binary_search(start, end):
        
        if (start > end):
            return start

        mid = (start + end)//2

        remove_cnt = 0
        pos = 0

        for rock in rocks:
            if rock-pos <= mid:
                remove_cnt += 1
            else:
                pos = rock
        
        if remove_cnt <= n:
            return binary_search(mid+1, end)
        else:
            return binary_search(start, mid-1)
    

    return binary_search(0, distance)