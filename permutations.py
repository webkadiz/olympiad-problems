s = input()
k = len(s)


def per(use):
    
    if len(use) == k:
        print(use)

    for i in range(k):
        if s[i] in use: continue;

        cuse = use + s[i]
        
        per(cuse)

per('')
