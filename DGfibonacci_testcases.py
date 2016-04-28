from fibonacci_func_1 import fibogetnum, getfiboresp, getfibo_accuracy
import unittest

"""
Test cases to test backend Fibonacci service.
"""

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        """
        maxterm is largest term that can be returned by service without error
        maxterm is derived from findmaxtermfibo() in fibonacci_func_1
        """       
        self.maxterm = 604

    def test_DGFibonacci_BackEnd_valid(self):
        """test for correct fibonacci number for a valid term"""
        self.assertEqual(fibogetnum(10,'get'),55) 
      
    def test_DGFibonacci_BackEnd_nonintnumber(self):
        """test for error response for non integer"""  
        self.assertTrue('error' in getfiboresp(5.8,'get'))
        
    def test_DGFibonacci_BackEnd_maximum_valid(self):
        """test for getting a fibonacci number for maximum term"""  
        self.assertTrue('fibonacci' in getfiboresp(self.maxterm,'get'))
        
    def test_DGFibonacci_BackEnd_morethanmaximum(self):
        """test for error response for a term > maximum valid term"""   
        self.assertTrue('error' in getfiboresp(self.maxterm+1,'get'))
        
    def test_DGFibonacci_BackEnd_negative(self):
        """test for error response for a term > maximum valid term"""
        self.assertTrue('error' in getfiboresp(-50,'get'))
        
    def test_DGFibonacci_BackEnd_nonnumeric(self):
        """test for error response for a for non numeric term"""
        self.assertTrue('error' in getfiboresp('q','get'))

    def test_DGFibonacci_BackEnd_blank(self):
        """test for error response for an empty term"""
        self.assertTrue('error' in getfiboresp('','get'))

    def test_DGFibonacci_BackEnd_accuracy(self):
        """
        test if maximum valid term is an accurate fibonacci number
        accurate is defined as: term(n) = term(n-1) + term(n-2)
        """
        maxaccterm=getfibo_accuracy(self.maxterm)
        self.assertEqual(maxaccterm,self.maxterm,'largest accurate term is:%d'%maxaccterm)
        
    def test_DGFibonacci_BackEnd_PostAction(self):
        """test for error response for an invalid post verb"""
        self.assertTrue('error' in getfiboresp('10','post'))
        
    def test_DGFibonacci_BackEnd_PutAction(self):
        """test for error response for an invalid put verb"""
        self.assertTrue('error' in getfiboresp('10','put'))

    def test_DGFibonacci_BackEnd_DeleteAction(self):
        """test for error response for an invalid delete verb"""
        self.assertTrue('error' in getfiboresp('10','delete'))
        
    def test_DGFibonacci_BackEnd_InvalidAction(self):
        """test for error response for an invalid action verb"""
        self.assertTrue('error' in getfiboresp('10','got'))          

if __name__ == '__main__':
    unittest.main()

