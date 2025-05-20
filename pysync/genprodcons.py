from threading import Condition
from collections import deque

class GenProdCons:
    def __init__(self, size=10):  # Cambiado de 100 a 10
        self.buffer = deque(maxlen=size)
        self.size = size
        self.condition = Condition()

    def put(self, e):
        with self.condition:
            while len(self.buffer) == self.size:
                self.condition.wait()
            self.buffer.append(e)
            self.condition.notify_all()

    def get(self):
        with self.condition:
            while len(self.buffer) == 0:
                self.condition.wait()
            e = self.buffer.popleft()
            self.condition.notify_all()
            return e

    def __len__(self):
        return len(self.buffer)
