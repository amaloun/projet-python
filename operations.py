#!usr/bin/env python3
from math import sin, cos
from point import point_aleatoire, Point
from segment import Segment
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

def rotation(segement, centre, alpha):
    """
        renvoie un segement qui coresspont
        a la rotation de ce segemnt autour de centre
    """
    segement1 = []
    for point in segement:
        abs = point[0]
        ord = point[1]
        abs1 = (abs - centre[0])*cos(alpha) - (ord - centre[1])*sin(alpha) + centre[0]
        ord1 = (abs - centre[0])*sin(alpha) + (ord - centre[1])*cos(alpha) + centre[1]
        segement1.append([abs1, ord1])
    return  segement1
def supprimer_seg(segments, carre):
    """
        une fonction qui prend une liste des segements et renvoie une listes
        des segements tels que l'un ou les deux points de segemnts
        sont dans le carre
    """
    # les 4 segments de carre
    segemnt1 = Segment([Point(carre[0][0], carre[0][1]), Point(carre[1][0], carre[1][1])])
    segemnt2 = Segment([Point(carre[1][0], carre[1][1]), Point(carre[2][0], carre[2][1])])
    segemnt3 = Segment([Point(carre[2][0], carre[2][1]), Point(carre[3][0], carre[3][1])])
    segemnt4 = Segment([Point(carre[3][0], carre[3][1]), Point(carre[0][0], carre[0][1])])
    carre1 = [segemnt1, segemnt2, segemnt3, segemnt4]
    segemnt_filtre = []
    for seg in segments:
        valeur = False
        for point in seg:
            if (point[0] >= carre[0][0] and point[0] <= carre[1][0] ) and (point[1] >= carre[0][1] and point[1] <= carre[2][1]):
                valeur = True
        if valeur:
            segemnt_filtre.append(seg)
    for seg in segemnt_filtre:
        changer = False
        for index,point in enumerate(seg) :
            if not(((point[0] >= carre[0][0]) and (point[0] <= carre[1][0])) and ((point[1] >= carre[0][1]) and (point[1] <= carre[2][1]))):
                changer = True
                indice = index
        if changer:
            point1 = Point(seg[0][0], seg[0][1])
            point2 = Point(seg[1][0], seg[1][1])
            segemntt = Segment([point1, point2])
            for seg1 in carre1:
                pointt = segemntt.intersection_avec(seg1)
                if pointt is not None:
                    seg[indice] = [pointt.abscisse, pointt.ordonnee]
    return segemnt_filtre

def duplications(segments, point):
    """
        elle prend une liste de segments et renvoie
        une listes des duplication de ces segments en réalisants
        des translation
    """
    segments_dup = []
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            for seg in segments:
                point1 = seg[0]
                point2 = seg[1]
                point11 = [point1[0] + j*point[0], point1[1] + i*point[1]]
                point22 = [point2[0] + j*point[0], point2[1] + i*point[1]]
                segments_dup.append([point11, point22])
    return segments_dup

def sup_deg(segments):
    """
        elle prend une liste de segments et renvoie une liste de segments
        avec supression de degre 1
    """
    segments1 = []
    for seg in segments:
        segments1.append(Segment([Point(seg[0][0], seg[0][1]), Point(seg[1][0], seg[1][1])]))
    for seg1 in segments1:
        # pour tous segments on va calculer tous les points d'intersections avec les autres segments
        distances = []
        for seg2 in segments1:
            inter = seg2.intersection_avec(seg1)
            if inter is not None:
                vect = ((inter.distance_a(seg1.points[0]), inter.distance_a(seg1.points[1])))
                if vect[0] > vect[1]:
                    distances.append((1, vect[1], inter))
                else:
                    distances.append((0, vect[0], inter))
        distances.sort(key=lambda x: x[1])
        if len(distances) >= 2:
            point = distances[0]
            seg1.points[point[0]] = point[2]
    return segments1
