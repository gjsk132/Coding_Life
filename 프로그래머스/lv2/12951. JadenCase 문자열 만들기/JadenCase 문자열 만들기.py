def solution(s):
    
    s = s.lower()
    
    result = [s[0].upper()]
    
    for i in range(len(s)):
        if (i < len(s)-1):
            if (s[i] == ' ' and s[i+1] != ' '):
                result.append(s[i+1].upper())
            else:
                result.append(s[i+1].lower())
    
    return "".join(result)
    
