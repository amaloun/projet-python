#!usr/bin/env python3
"""
    ce fichier contient toutes les fonctions
    qui realisent les operations mathematiques
"""
def symetrie_point(point, axe):
    """
        renvoie la symetrie vertical d'un ponit
    """
    return point - 2*(point - axe)

def symetrie(segements, axe):
    """
        une fonction qui prend une liste de segments
        et renvoie une listes des segements symétriques
        par rapport à l'axe vertical
    """
    segments_symetrique = []
    for segement in segements:
        abscisse11 = symetrie_point(segement[0][0], axe)
        abscisse22 = symetrie_point(segement[1][0], axe)
        segments_symetrique.append([[abscisse11, segement[0][1]],
                                    [abscisse22, segement[1][1]]])
    return segments_symetrique
