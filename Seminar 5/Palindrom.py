word = "12321"

def proverka(x):
    if len(x) <= 1:
        return True
    if x[0] == x[-1]:
        return proverka(x[1:-1])
    else:
        return False
    
print(proverka(word))