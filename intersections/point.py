"""
des points du plans
"""

from math import sqrt
from random import uniform


class Point:
    """
    un point du plan
    """
    def __init__(self, abscisse, ordonnee):
        """
        creation d'un point a partir d'une abscisse et d'une ordonnee
        """
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def __str__(self):
        return str(self.abscisse) + "," + str(self.ordonnee)

    def distance_a(self, autre_point):
        """
        renvoie la distance entre deux points
        """
        difference_x = autre_point.abscisse - self.abscisse
        difference_y = autre_point.ordonnee - self.ordonnee
        return sqrt(difference_x*difference_x + difference_y*difference_y)


def point_aleatoire(largeur=800, hauteur=600):
    """
    renvoie un point aleatoire,
    x compris entre 0 et largeur
    et y entre 0 et hauteur
    """
    return Point(uniform(0, largeur), uniform(0, hauteur))
