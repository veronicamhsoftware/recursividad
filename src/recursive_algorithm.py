combinations = []
limit = 0
def potency_b(n, digit, indice, new_i):    
    total = indice**n + new_i**n    
    if total == digit:
        combinations.append({"combinaciones para %s" % digit :[indice,new_i]})
    if total > digit:
        return total      
    return potency_b(n, digit, indice, new_i + 1)


def potency(digit, n, i):
    if (digit < 1 or digit > 1000) or (n < 2 or n > 10 ):
        return False        
    else:        
        result = potency_b(n,digit,i,i+1)
        if i**n > digit:
            return digit
        return potency(digit, n, i + 1)


potency(13,2,1)
print(combinations)
potency(10,2,1)
print(combinations)
potency(5,2,1)
print(combinations)
potency(35,3,1)
print(combinations)