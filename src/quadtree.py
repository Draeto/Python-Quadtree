from __future__ import annotations


class QuadTree:
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return self.getdepth()

    def getdepth(self, actualdepth: int = 1):

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
        """ Open a given file, containing a textual representation of a list"""
        return QuadTree.fromlist(eval(open(filename, 'r').read()))

    @staticmethod
    def fromlist(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        properties = []
        for element in data:
            if isinstance(element, int):
                properties.append(element)
            else:
                properties.append(QuadTree.fromlist(element))
        return QuadTree(properties[0], properties[1], properties[2], properties[3])


class PyQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass
