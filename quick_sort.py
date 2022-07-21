# tab = [21,41,33,38,11,6,57]
# def quick_sort(tab,debut,fin):
#     if debut<fin:
#         iPivot = (debut+fin)//2
#         for i in range(debut, iPivot):
#             tmp = tab[i]
#             if tmp > iPivot:
#                 tab[i+1]=i-1
#                 while (i < iPivot):        
#     quick_sort(tab,debut,iPivot-1)
#     quick_sort(tab,iPivot+1,fin)


# correction

def tri_rapide(tab,debut,fin):
    
    if debut < fin :
        iPivot = (debut+fin)//2
        iPivotOrigine = iPivot
        i = debut
        
        while i < iPivot :
           
            if tab[i] > tab[iPivot] :
                tmp = tab[i]
                j = i
                
                while (j < iPivot) :
                    tab[j] = tab[j+1]
                    j = j+1
                
                tab[iPivot] = tmp
                iPivot = iPivot-1
                i = i - 1
            i = i+1
        
        i = iPivotOrigine+1
        
        while i < fin+1:
            if tab[i] < tab[iPivot] :
                tmp = tab[i]
                j = i
                while (j > iPivot):
                    tab[j] = tab[j-1]
                    j = j - 1
                tab[iPivot] = tmp
                iPivot = iPivot+1
            i = i + 1
        tri_rapide(tab, debut, iPivot-1)
        tri_rapide(tab, iPivot+1, fin)
    return tab
tab = [21,41,33,38,11,6,57]
print(tri_rapide(tab, 0, len(tab)-1))