def solution(coin, cards):
    cards_cnt = len(cards)
    
    target = cards_cnt + 1
    
    default_cards_cnt = len(cards)//3
    round = 0
    boundary = default_cards_cnt + 2
        
    for _ in range(default_cards_cnt+1):
        if not cards:
            continue
        
        round += 1
        go_next_round = False
        boundary = min(boundary, len(cards))
        
        for idx, val in enumerate(cards[:boundary]):
            if not target - val in cards[:boundary]:
                continue
            
            
            pair_idx = cards[:boundary].index(target-val)
            
            if pair_idx < idx:
                break
            
            if pair_idx < default_cards_cnt:
                default_cards_cnt -= 2
                
            elif idx < default_cards_cnt:
                if coin < 1:
                    continue
                coin -= 1
                default_cards_cnt -= 1
                
            else:
                if coin < 2:
                    continue
                coin -= 2
                
            del cards[pair_idx]
            del cards[idx]
            go_next_round = True
            
            break
                    
        if go_next_round:
            continue
            
        break
                    
    return round       
                    
                    
                    
                    
        