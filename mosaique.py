#!/usr/bin/env python3
import sys
from random import randint
from math import pi
from svg import *
from operations import *
nom = "etape1.svg"
def etape1(height, width):
    """
        création des segements aléatoire
    """
    # nom = "etape1.svg"
    # première étape : traçage des segements aléatoires
    nombre_de_segments = randint(15, 25)
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
    for segement in seg:
        for coef in range(8):
            alpha = coef*(45)*pi/180
            segement1 = rotation(segement, centre, alpha)
            absc1, ord1 = segement1[0]
            absc2, ord2 = segement1[1]
            line(absc1, ord1, absc2, ord2, nom)
def etape4(largeur_rect, width, height, point1, point2, point4):
    """
        etape 4 : on clippe dans le carré
    """
    # rectangle1
    absc, ord = [0, 0]
    rect(absc, ord, width, point1[1], nom)
    # resctangle 2
    absc2, ord2 = [0, point1[1]]
    height2 = height - point1[1]
    rect(absc2, ord2, point1[0], height2, nom)
    # rectangle 3
    width3 = width - point2[0]
    height3 = height - point2[1]
    rect(point2[0], point2[1], width3, height3, nom)
    # rectangle 4
    height4 = height - point4[1]
    rect(point4[0], point4[1], largeur_rect, height4, nom)


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
    etape3(seg, centre)
    largeur_rect = width // 2
    point1 = [centre[0] - largeur_rect/2, centre[1] - largeur_rect / 2]
    point2 = [centre[0] + largeur_rect/2, centre[1] - largeur_rect / 2]
    point4 = [centre[0] - largeur_rect/2, centre[1] + largeur_rect / 2]
    etape4(largeur_rect, width, height, point1, point2, point4)
    close(nom)
main()
