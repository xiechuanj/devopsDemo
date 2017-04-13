# -*- coding: utf-8 -*-
'''
Created on 2017年4月13日

@author: xiechuanjun
'''

import unittest
from triangle import Triangle

class TestIsTriangleFunctions(unittest.TestCase):  
  
    def setUp(self):  
        pass
    
    def test_IsTriangle(self):
        Triangle().IsTriangle('a',2,3)
        Triangle().IsTriangle(2,-2,3)
        Triangle().IsTriangle(1,2,3)
        Triangle().IsTriangle(2,2,3)
        Triangle().IsTriangle(2,2,2)
        Triangle().IsTriangle(3,4,5)
    
    def tearDown(self):
        pass