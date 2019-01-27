#!/usr/bin/env python3
from svg import *
from random import randint
import sys
def main():
    """
        le programme principal
    """
    width, height = int(sys.argv[1]), int(sys.argv[2])
    start(height, width)
    # première étape : traçage des segements aléatoires
    nombre_de_segments = randint(15,25)
    segements = []
    for _ in range(nombre_de_segments):
        point1 = [randint(0, width), randint(0, height)]
        point2 = [randint(0, width), randint(0, height)]
        segements += [[point1, point2]]
        line(point1[0], point1[1], point2[0], point2[1])
    close()
main()
