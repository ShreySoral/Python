import unittest
import unittest
import main

class testmain(unittest.TestCase):
    def test_do_stuff(self):
        num=10
        result=main.do_stuff(num)
        self.assertEqual(result,15)

    def test_do_stuff1(self):
        param='ssss'
        result=main.do_stuff(param)
        self.assertIsInstance(result,ValueError)

    def test_do_stuff2(self):
        testp=None
        r=main.do_stuff(testp)
        self.assertEqual(r,'please enter a number')
    def test_do_stuff3(self):
        tp=''
        r1=main.do_stuff(tp)
        self.assertEqual(r1,'please enter a number')

    # def test_do_stuff(self):
    #     parameter=0
    #     res=main.do_stuff(parameter)
    #     self.assertIsNone(res,ValueError)
    # def test_do_stuff(self):
    #     p={'zvi':999}
    #     resultis=main.do_stuff(p)
    #     self.assertNotEqual(resultis)
if __name__=='__main__':
    unittest.main()