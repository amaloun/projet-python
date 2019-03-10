"""
generation d'images svg sur la sortie standard.
"""


def pied():
    """
    affiche la fin du code svg sur la sortie standard
    """
    print("</svg>")


def entete(largeur, hauteur):
    """
    affiche le debut du code svg d'une image
    de largeur et hauteur donnees sur la sortie standard
    """
    print('<svg height="{}" width="{}">'.format(hauteur, largeur))


def segment(point1, point2, epaisseur_trait=2, couleur=(255, 0, 0)):
    """
    affiche un segment entre les deux points donnes.
    le style est changeable dans les arguments optionnels.
    """
    #pylint: disable=invalid-name
    x1, y1 = point1
    x2, y2 = point2
    print('<line x1="{}" y1="{}" x2="{}" y2="{}" \
style="stroke:rgb{};stroke-width:{}" />'.format(x1, y1, x2, y2,
                                                couleur, epaisseur_trait))


def disque(centre, rayon=5, couleur=(0, 255, 0)):
    """
    affiche un disque au point donne.
    le style est changeable dans les arguments optionnels.
    """
    x_centre, y_centre = centre
    print('<circle cx="{}" cy="{}" r="{}" fill="rgb{}" />'.format(x_centre,
                                                                  y_centre,
                                                                  rayon,
                                                                  couleur))
