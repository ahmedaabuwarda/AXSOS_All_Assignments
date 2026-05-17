def areOccurrencesEqual(s: str) -> bool:
    s = sorted(s)
    auc = {}
    i = 0
    j = 1 
    counter = 1
    while (i <= len(s)-1):
        if (j >= len(s)):
            auc[s[i]] = counter
            break
        if (s[i] == s[j]):
            counter += 1
            j += 1
        elif (j == len(s)-1):
            auc[s[i]] = counter
            i += counter
            j = i + 1
            counter = 1
        else:
            j += 1

    auc_list = set(auc.values())

    return len(auc_list) == 1
    
print(areOccurrencesEqual(s="abacbc"))