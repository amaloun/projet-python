#!/usr/bin/env python3
# ceci contient le modulr svg
"""
    ce fichier contien toutes les fonctions qui permet
    la manipulations des module svg
"""
def start(height, width):
    """
        dessiner le plan de travail
    """
    print('<svg width="{}" height="{}">'.format(width, height))
    print('<rect width="{}" height="{}" style="fill:rgb(255,255,255)" />'\
    .format(width, height))

def line(x1, y1 ,x2, y2):
    """
        tracer un segement de x1,y1 à x2,y2
    """
    print('<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:rgb(255,0,0);stroke-width:2" />'\
    .format(x1,y1, x2, y2))
def close():
    """
        fermer la balise svg
    """
    print('</svg>')
