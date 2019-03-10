#!/usr/bin/env python3
"""
exemple du cours: intersection de segments.
"""
from itertools import combinations
from segment import segment_aleatoire
import svg

def main():
    """
    genere un svg de 50 segments aleatoires, avec leurs intersections
    et l'affiche sur la sortie standard.
    """

    segments = [segment_aleatoire() for _ in range(50)]
    svg.entete(800, 600)
    for segment in segments:
        svg.segment(*segment.coordonnees())

    intersections = filter(
        None,
        (s1.intersection_avec(s2) for s1, s2 in combinations(segments, r=2)))

    for intersection in intersections:
        svg.disque((intersection.abscisse, intersection.ordonnee))

    svg.pied()


main()
