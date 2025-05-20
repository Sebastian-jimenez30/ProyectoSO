from threading import Condition

class RendezvousDEchange:
    def __init__(self):
        self.condition = Condition()
        self.slot = None
        self.has_value = False

    def echanger(self, value):
        with self.condition:
            if not self.has_value:
                self.slot = value
                self.has_value = True
                self.condition.wait()
                received = self.slot
                self.slot = None
                self.has_value = False
                self.condition.notify()
                return received
            else:
                received = self.slot
                self.slot = value
                self.condition.notify()
                return received
