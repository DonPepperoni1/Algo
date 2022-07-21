def tri_bulle(tab):
    for j in range (len(tab)-1) :
        trie = True  
        for i in range (len(tab)-1-j) :
            if tab[i] > tab[i+1]:
                tmp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = tmp
                trie = False
        if trie == True :
            return tab
    return tab