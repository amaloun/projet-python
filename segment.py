"""
segments dans le plan
"""
from point import point_aleatoire, Point

class Segment:
    """
    un segment du plan.
    """
    def __init__(self, points):
        """
        construit un segment a partir d'un vecteur de deux points
        """
        self.points = points

    def coordonnees(self):
        """
        renvoie le vecteur de couples de coordonnees des points.
        """
        return [[p.abscisse, p.ordonnee] for p in self.points]

    def longueur(self):
        """
        renvoie la longueur du segment.
        """
        return self.points[0].distance_a(self.points[1])

    def contient(self, point):
        """
        est-ce que l'on contient (a peu pres) le point donne ?
        """
        return abs(
            self.longueur()
            - sum(p.distance_a(point) for p in self.points)
        ) <= 0.0000001
    def symetrie(self, axe):
        """
            renvoie un nouvelle segment symetrique à
            l' axe
        """
        for point in self.points:
            point.symetrie(axe)
        return self


    def intersection_avec(self, autre):
        """
        intersection entre deux segments.
        renvoie None si aucun point n'est trouve.
        garantie: si on renvoie un point i alors i est contenu dans self et
        i est contenu dans autre.
        """
        # pylint: disable=invalid-name
        # le code est plutot complexe ici et d'ailleurs pylint nous le dit.
        # il merite donc au moins un petit commentaire pour guider le lecteur.
        # (xv, yv) est le vecteur directeur du premier segment (p0, p1)
        # (xw, yw) est le vecteur directeur du second segment (p2, p3)
        # on resout i = p0 + alpha*(xv, yv)
        # et i = p1 + beta*(xw, yw)
        # et on obtient alors les equations ci dessous.

        (x0, y0), (x1, y1) = self.coordonnees()
        (x2, y2), (x3, y3) = autre.coordonnees()
        xv = x1 - x0
        yv = y1 - y0
        xw = x3 - x2
        yw = y3 - y2
        denominateur = (xv*yw) - (yv*xw)
        if denominateur == 0:
            return None
        alpha = ((y0-y2)*xw - (x0-x2)*yw) / denominateur
        intersection = Point(
            x0 + alpha*xv,
            y0 + alpha*yv
        )
        if self.contient(intersection) and autre.contient(intersection):
            return intersection
        return None


def segment_aleatoire(largeur=800, hauteur=600):
    """
    renvoie un segment aleatoire tel que
    0 <= x <= largeur et
    0 <= y <= hauteur
    """
    return Segment(
        [
            point_aleatoire(largeur, hauteur),
            point_aleatoire(largeur, hauteur)
        ]
    )
