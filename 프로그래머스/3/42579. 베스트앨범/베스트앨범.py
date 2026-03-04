from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    total_genres = defaultdict(int)
    in_genres = defaultdict(list)
    
    for k, v in enumerate(zip(genres, plays)):
        g, p = v
        total_genres[g] += p
        in_genres[g].append((p, k))
    
    list_total_genres = list(total_genres.items())
    list_total_genres.sort(key=lambda x: -x[1])
    
    for g, tp in list_total_genres:    
        now_genres = in_genres[g]
        now_genres.sort(key=lambda x: (x[0], -x[1]))
        
        cnt = 2
        while cnt and now_genres:
            p, idx = now_genres.pop()
            answer.append(idx)
            cnt -= 1
    
    return answer