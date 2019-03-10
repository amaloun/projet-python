#!/usr/bin/env python3
"""
test de la class Point
"""
from point import point_aleatoire
import svg


def main():
    """
    creation d'un nuage de points aleatoires
    """
    svg.entete(800, 600)

    for _ in range(500):
        point = point_aleatoire()
        svg.disque((point.abscisse, point.ordonnee))

    svg.pied()

main()
