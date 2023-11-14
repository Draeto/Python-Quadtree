import os
import sys

from src import QuadTree

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))


def test_sample():
    filename = "files/quadtree.txt"
    q = QuadTree.fromfile(filename)
    assert q.depth == 4


def test_single():
    filename = "files/quadtree_easy.txt"
    q = QuadTree.fromfile(filename)
    assert q.depth == 1
