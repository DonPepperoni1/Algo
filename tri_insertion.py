def tri_insertion(tab):
    for i in range(1,len(tab)):
        tmp=tab[i]
        j=i-1
        while(j >= 0 and tmp < tab[j]):
            tab[j+1] = tab[j]
            j = j-1
            tab[j+1] = tmp
    return tab

tab = [5,6,10,40,37,22,14,8,9]
tri_insertion(tab)
print(tab)