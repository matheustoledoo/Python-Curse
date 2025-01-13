import unittest #biblioteca de teste
import main #importando main que esta na pasta

class TestMain(unittest,TestCase):
    def testDoStuff(self):
        testParam = 10
        result = main.doStuff(testParam)
        self.assertEqual(result, 15)

unittest.main()