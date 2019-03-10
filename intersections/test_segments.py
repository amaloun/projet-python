#!/usr/bin/env python3
"""
test d'une intersection de segments
"""
from segment import Segment
from point import Point
import svg

def main():
    """
    on intersecte deux segments particuliers.
    """
    svg.entete(800, 600)
    segment1 = Segment([Point(0, 200), Point(500, 200)])
    segment2 = Segment([Point(300, 0), Point(300, 600)])
    svg.segment(*segment1.coordonnees())
    svg.segment(*segment2.coordonnees())
    intersection = segment1.intersection_avec(segment2)
    svg.disque((intersection.abscisse, intersection.ordonnee))
    svg.pied()

main()
