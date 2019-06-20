import unittest
import calc  
class UTest(unittest.TestCase):
    def test_add(self):
        print("Success")
        result=calc.add(20,5)
        self.assertEqual(result,25)
    def test_mul(self):
        print("Success")
        result=calc.multiply(20,5)
        self.assertEqual(result,100)

    def test_div(self):
        print("Success")
        result=calc.divide(20,5)
        self.assertEqual(result,4)

    def test_sub(self):
        print("Success")
        result=calc.subtract(20,5)
        self.assertEqual(result,15)
        
if __name__=='__main__':
    unittest.main()
