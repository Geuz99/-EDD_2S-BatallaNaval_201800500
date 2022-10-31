import hashlib


class NodoMerkle:
    def __init__(self, left, right, value: str, content) -> None:
        self.left: NodoMerkle = left
        self.right: NodoMerkle = right
        self.value = value
        self.content = content

    @staticmethod
    def hash(val: str) -> str:
        return hashlib.sha256(val.encode("utf-8")).hexdigest()

    def __str__(self):
        return (str(self.value))
