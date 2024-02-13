from itertools import combinations, product
from collections import defaultdict


def get_count_of_each_combo(dices, indices):
    num_combos: Dict[int, int] = defaultdict(int)
    for pips in product(range(6), repeat=len(indices)):
        sum_combo: int = sum(dices[i][j] for i, j in zip(indices, pips))  # i번째 주사위 j번째 눈
        num_combos[sum_combo] += 1
    return sorted(num_combos.items())


def solution(dice):
    answer: List[int] = []
    
    n: int = len(dice)
    dice_indices: Set[int] = set(range(n))
    max_win_cnt: int = 0
    for A in combinations(range(n), n // 2):
        
        if A[0]:
            break
        
        B: Set[int] = dice_indices.difference(A)
        
        A_combos: List[Tuple[int, int]] = get_count_of_each_combo(dice, A)
        B_combos: List[Tuple[int, int]] = get_count_of_each_combo(dice, B)
        
        A_win_cnt: int = 0
        B_win_cnt: int = 6**n
        
        for A_combo_sum, A_combo_cnt in A_combos:
            for B_combo_sum, B_combo_cnt in B_combos:
                if B_combo_sum >= A_combo_sum:
                    B_win_cnt -= (A_combo_cnt * B_combo_cnt) if B_combo_sum == A_combo_sum else 0
                    break
                    
                A_win_cnt += A_combo_cnt * B_combo_cnt
        
        B_win_cnt -= A_win_cnt
        
        if A_win_cnt > max_win_cnt:
            max_win_cnt = A_win_cnt
            answer = A
            
        if B_win_cnt > max_win_cnt:
            max_win_cnt = B_win_cnt
            answer = B
        
    return [i + 1 for i in answer]