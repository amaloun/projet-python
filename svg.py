#!/usr/bin/env python3
# ceci contient le modulr svg
"""
    ce fichier contien toutes les fonctions qui permet
    la manipulations des module svg
"""
def start(height, width, nom):
    """
        dessiner le plan de travail
    """
    with open(nom, "w") as fichier:
        fichier.write('<svg width="{}" height="{}">\n'.format(width, height))
        fichier.write('<rect width="{}" height="{}" style="fill:rgb(255,255,255)" />\n'\
        .format(width, height))

def line(x1, y1 ,x2, y2, nom):
    """
        tracer un segement de x1,y1 à x2,y2
    """
    with open(nom, "a") as fichier:
        fichier.write('<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:rgb(255,0,0);stroke-width:2" />\n'\
        .format(x1,y1, x2, y2))


def rect(absc, ord, width, height, nom):
    """
        dessiner un rectangle
    """
    with open(nom, "a") as fichier:
        fichier.write(' <rect x="{}" y="{}" width="{}" height="{}" style="fill:white" />'\
        .format(absc, ord, width, height))
def close(nom):
    """
        fermer la balise svg
    """
    with open(nom, "a") as fichier:
        fichier.write('</svg>\n')
