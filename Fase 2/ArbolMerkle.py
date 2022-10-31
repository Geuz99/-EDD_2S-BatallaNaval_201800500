from typing import List
import typing
from NodoMerkle import NodoMerkle


class ArbolMerkle:
    def __init__(self, values: List[str]) -> None:
        self.__buildTree(values)

    def __buildTree(self, values: List[str]) -> None:
        leaves: List[NodoMerkle] = [NodoMerkle(None, None, NodoMerkle.hash(e), e) for e in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0])  # duplicate last elem if odd number of elements
            self.root: NodoMerkle = self.__buildTreeRec(leaves)

    def __buildTreeRec(self, nodes: List[NodoMerkle]) -> NodoMerkle:
        half: int = len(nodes) // 2
        if len(nodes) == 2:
            return NodoMerkle(nodes[0], nodes[1], NodoMerkle.hash(nodes[0].value + nodes[1].value),
                              nodes[0].content + "+" + nodes[1].content)
        left: NodoMerkle = self.__buildTreeRec(nodes[:half])
        right: NodoMerkle = self.__buildTreeRec(nodes[half:])
        value: str = NodoMerkle.hash(left.value + right.value)
        content: str = self.__buildTreeRec(nodes[:half]).content + "+" + self.__buildTreeRec(nodes[half:]).content
        return NodoMerkle(left, right, value, content)

    def printTree(self) -> None:
        self.__printTreeRec(self.root)

    def __printTreeRec(self, node) -> None:
        if node is not None:
            if node.left is not None:
                print("Left: " + str(node.left))
                print("Right: " + str(node.right))
            else:
                print("Input")

            print("Value: " + str(node.value))
            print("Content: " + str(node.content))
            print("")
            self.__printTreeRec(node.left)
            self.__printTreeRec(node.right)

    def getRootHash(self) -> str:
        return self.root.value