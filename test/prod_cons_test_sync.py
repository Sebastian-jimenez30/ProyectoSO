import os
import unittest
from threading import Thread
import importlib

expected_module = 'PRODCONSMODULE'
default_module = 'pysyn'

if expected_module in os.environ:
    prod_cons_mdl = os.environ[expected_module]
else:
    prod_cons_mdl = 'pysync'

prod_cons_imprt = importlib.__import__(prod_cons_mdl, globals(), locals(), [], 0)

def basic_producer(prod_cons, times, output):
    for i in range(times):
        prod_cons.put(i)
        output.append(i)

def basic_consumer(prod_cons, times, output):
    for _ in range(times):
        value = prod_cons.get()
        output.append(value)

# 🧪 Clase de test
class TestProdConsTestSync(unittest.TestCase):
    def test_prod_cons_all(self):
        prod_cons = prod_cons_imprt.GenProdCons()
        produced = []
        consumed = []

        prod_thr = Thread(target=basic_producer, args=(prod_cons, 100, produced))
        cons_thr = Thread(target=basic_consumer, args=(prod_cons, 100, consumed))

        prod_thr.start()
        cons_thr.start()
        prod_thr.join()
        cons_thr.join()

        self.assertEqual(produced, consumed) 
