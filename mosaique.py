#!/usr/bin/env python3
import sys
from random import randint
from math import pi
from svg import start, line, rect, close
from operations import symetrie_point, symetrie, rotation, supprimer_seg, duplications, sup_deg
nom = "etape.svg"


def etape1(height, width):
    """
        création des segements aléatoire
    """
    # nom = "etape1.svg"
    # première étape : traçage des segements aléatoires
    nombre_de_segments = randint(15, 50)
    segements = []
    for _ in range(nombre_de_segments):
        point1 = [randint(width/2, width), randint(0, height)]
        point2 = [randint(width/2, width), randint(0, height)]
        segements += [[point1, point2]]
        line(point1[0], point1[1], point2[0], point2[1], nom)
    # close(nom)
    return segements


def etape2(segements, axe_vertical):
    """
        la deuxième étape de la symétrie
    """
    # nom = "etape2.svg"
    # dexime etape de travail la symetrie
    segments_symetrique = symetrie(segements, axe_vertical)
    for segement in segments_symetrique:
        point1 = segement[0]
        point2 = segement[1]
        line(point1[0], point1[1], point2[0], point2[1], nom)
    return segments_symetrique


def etape3(seg, centre):
    """
        etape3 : on tourne 8 fois
    """
    segements_final = []
    for segement in seg:
        for coef in range(8):
            alpha = coef*(45)*pi/180
            segement1 = rotation(segement, centre, alpha)
            segements_final.append(segement1)
            absc1, ord1 = segement1[0]
            absc2, ord2 = segement1[1]
            line(absc1, ord1, absc2, ord2, nom)
    return segements_final

def etape4(height, width, segements, carre):
    """
        etape 4 : on clippe dans le carré
    """
    # on créé une nouvelle image qui contient uniquement les segements qu'on va triée
    nom1 = "etape41.svg"
    start(height, width, nom1)
    segemnt_filtre = supprimer_seg(segements, carre)
    # line(288, 256, 372, 21, nom1)
    for segement in segemnt_filtre:
        point1 = segement[0]
        point2 = segement[1]
        line(point1[0], point1[1], point2[0], point2[1], nom1)
    close(nom1)
    return segemnt_filtre
def etape5(height, width, segments, point, nom):
    """
        l'étape de 8 duplication
    """
    start(height, width ,nom)
    segments_dup = duplications(segments, point)
    for segement in segments_dup:
        point1 = segement[0]
        point2 = segement[1]
        line(point1[0], point1[1], point2[0], point2[1], nom)
    close(nom)

def etape6(height, width, segments):
    """
        l'estape de la supression de degré 1
    """
    nom6 = "etape6.svg"
    start(height, width, nom6)
    segments_sup = sup_deg(segments)
    for seg in segments_sup:
        point11, point12 = seg.coordonnees()[0]
        point21, point22 = seg.coordonnees()[1]
        line(point11, point12, point21, point22, nom6)
    close(nom6)
    segs = []
    for seg in segments_sup:
        segs.append(seg.coordonnees())
    return segs

def main():
    """
        le programme principal
    """
    width, height = int(sys.argv[1]), int(sys.argv[2])
    start(height, width, nom)
    axe_vertical = width/2
    segments = etape1(height, width)
    segments_symetrique = etape2(segments, axe_vertical)
    seg = segments + segments_symetrique
    centre = [width / 2, height / 2]
    segements_final = etape3(seg, centre)
    # les coordonné de carré qu'on va choisir
    facteur = height//6
    point1 = [centre[0] - facteur, centre[1] - facteur]
    point2 = [centre[0] + facteur, centre[1] - facteur]
    point3 = [centre[0] + facteur, centre[1] + facteur]
    point4 = [centre[0] - facteur, centre[1] + facteur]
    carre = [point1, point2, point3, point4]
    # étape de clip dans le carré
    close(nom)
    segement_filtre = etape4(height, width, segements_final, carre)
    nom5 = "etape5.svg"
    etape5(height, width, segement_filtre, point1, nom5)
    segments7 = etape6(height, width, segement_filtre)
    nom7 = "etape7.svg"
    etape5(height, width, segments7, point1, nom7)

main()
