"""
Module principal pour l'étude de la suite de Syracuse.
Contient les fonctions de calcul et d'affichage.
"""


# imports
from plotly.graph_objects import Scatter, Figure  # pylint: disable=import-error

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Affiche la suite de Syracuse sous forme de graphique avec Plotly."""
    title = f"Syracuse (n = {lsyr[0]})"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html(
    #     'fig.html',
    #     include_plotlyjs='cdn'
    # )
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # Le temps de vol est le nombre d'étapes avant d'atteindre 1
    # (longueur de la suite - 1)
    return len(l) - 1
def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # Temps de vol en altitude : nombre d'étapes consécutives
    # où la valeur reste strictement supérieure à la source, à partir du début
    source = l[0]
    n = 0
    for x in l[1:]:
        if x > source:
            n += 1
        else:
            break
    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # Altitude maximale : valeur maximale de la suite
    return max(l)
#### Fonction principale

def main():

    """Fonction principale pour tester les fonctions secondaires sur la suite de Syracuse."""
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
