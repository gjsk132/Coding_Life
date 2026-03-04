from collections import defaultdict

def solution(phone_book):
    prefix = defaultdict(bool)
    
    phone_book.sort(key = lambda x : (len(x), x), reverse = True)
    
    for phone in phone_book:
        if prefix[phone]:
            return False
        
        now = ''
        for num in phone:
            now += num
            prefix[now] = True
            
    return True