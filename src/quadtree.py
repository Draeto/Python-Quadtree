from __future__ import annotations


class QuadTree:

    """ Classe principale qui contient toutes les méthodes du code """

    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        """ Constructeur de la classe Quadtree """
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """ Appel de la méthode getdepth pour retourner la profondeur du quadtree"""
        return self.getdepth()

    def getdepth(self, actualdepth: int = 1):
        """  Calcul la profondeur des 4 premières branches principales puis retourne la plus grande profondeur   """
        parameters = [self.hg, self.hd, self.bd, self.bg]
        depths = []
        for element in parameters:
            if isinstance(element, QuadTree):
                depths.append(element.getdepth(actualdepth + 1))
            else:
                depths.append(actualdepth)

        return max(depths)

    @staticmethod
    def fromfile(filename: str) -> QuadTree:
        """ Ouvre un fichier et transforme le texte en liste qui pourra être lue
         et retournée en Quadtree par la méthode fromlist"""
        return QuadTree.fromlist(eval(open(filename, 'r').read()))

    @staticmethod
    def fromlist(data: list) -> QuadTree:
        """ Génération d'un Quadtree depuis une liste """
        properties = []
        for element in data:
            if isinstance(element, int):
                properties.append(element)
            else:
                properties.append(QuadTree.fromlist(element))
        return QuadTree(properties[0], properties[1], properties[2], properties[3])