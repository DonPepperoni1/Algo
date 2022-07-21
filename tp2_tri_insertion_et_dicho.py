#def tri_insertion(tab):
#    tab = [34,10,8,29,37,4,11,76,55]
#    for i in range (len(tab)) :
#        if tab[i+1] < tab[i]:
#            tmp1 = tab[i]
#            tab[i+1] = tab[i]
#            tab[i+1] = tmp1
#        while tab[i] != (len(tab)):
#            if tab[i+1] > tab[i+2]:
#                tmp2 = tab[i+1]
#                tab[i+2] = tab[i+1]
#                tab[i+2] = tmp2
#            return tab
#    tri_insertion(tab)


# correction 
# def tri_insertion(tab):
#    tab = [34,10,8,29,37,4,11,76,55]
#    for i in range (1, len[tab]):
#        tmp = tab[i]
#        for j in range(i,0,-1):
#            if tmp<tab[j-1]:
#                tab[j]=tab[j-1]
#                tab[j]=tmp


def tri_insertion(tab):
    for i in range(1,len(tab)):
        tmp=tab[i]
        j=i-1
        while(j >= 0 and tmp < tab[j]):
            tab[j+1] = tab[j]
            j = j-1
            tab[j+1] = tmp
    return tab

tab = [34,10,8,29,37,4,11,76,55]
tri_insertion(tab)
print(tab)

valeur = 8
# def recherche_seq(tab,valeur):
#     for i in range (len(tab)):
#         if tab[i] == valeur:
#             return "trouvé"
#         if tab[i]>valeur :
#             return "non trouvé"
#     return "non trouvé"
# print(recherche_seq(tab,valeur))


def recherche_dicho(tab,valeur,debut,fin):
    if debut<=fin:
        iPivot=(debut+fin)//2
        if tab[iPivot]==valeur:
            return "trouvé !!!"
        if tab[iPivot]>valeur:
            recherche_dicho(tab,valeur,debut,fin,iPivot=1)
        else : 
            recherche_dicho(tab,valeur,iPivot+1,fin)
        return "non trouvé :("
print(recherche_dicho(tab,valeur))