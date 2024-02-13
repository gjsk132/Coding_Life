from itertools import combinations, product
from collections import defaultdict, deque


def get_count_of_each_combo(dices, indices):
    num_combos: Dict[int, int] = defaultdict(int)
    
    for pips in product(range(6), repeat=len(indices)):
        sum_combo: int = sum(dices[i][j] for i, j in zip(indices, pips))  # i번째 주사위 j번째 눈
        num_combos[sum_combo] += 1
        
    return num_combos

def change_sort_list(combo):
    return sorted(combo.items())

def make_prefix_sum(combo, cnt):
    num_combos, limit = combo, max(combo.keys())
    for i in range(2,cnt):
        num_combos[i] += num_combos[i-1]
    
    return num_combos
    

def solution(dice):
    answer: List[int] = []
    
    n: int = len(dice)
    dice_indices: Set[int] = set(range(n))
    max_win_cnt: int = 0
    for A in combinations(range(n), n // 2):
        B: Set[int] = dice_indices.difference(A)
        
        A_combos: List[Tuple[int, int]] = change_sort_list(get_count_of_each_combo(dice, A))
        B_combos: Dict[int, int] = make_prefix_sum(get_count_of_each_combo(dice, B), A_combos[-1][0])
        win_cnt: int = 0
        for A_combo_sum, A_combo_cnt in A_combos:
            win_cnt += A_combo_cnt * B_combos[A_combo_sum-1]
        
        if win_cnt > max_win_cnt:
            max_win_cnt = win_cnt
            answer = A
        
    return [i + 1 for i in answer]