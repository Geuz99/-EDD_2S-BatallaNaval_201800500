class hash_table:
    def __init__(self):
        self.table = [[],] * 13

    def checkPrime(self, n):
        if n == 1 or n == 0:
            return 0
        for i in range(2, n // 2):
            if n % i == 0:
                return 0
        return 1

    def getPrime(self, n):
        if n % 2 == 0:
            n = n + 1
        while not self.checkPrime(n):
            n += 2
        return n

    def hashFunction(self, key):
        capacity = self.getPrime(10)
        return key % capacity

    def insertData(self, key, data):
        index = self.hashFunction(key)
        self.table[index] = [key, data]

    def removeData(self, key):
        index = self.hashFunction(key)
        self.table[index] = 0
