# -*- coding: utf-8 -*-
'''
Created on 2017年4月13日

@author: xiechuanjun
'''



class Triangle:
    def IsTriangle(self, a,b,c):
        if isinstance(a,int) and a > 0 and isinstance(b,int) and b > 0 and isinstance(c,int) and c > 0:
            
            m = max(a,b,c)
            if (a + b + c > 2 * m):
                if a == b and b == c:
                    print "equilateral triangle.a = %s, b = %s, c = %s\n"%(a,b,c)      
                elif a == b or b == c or a == c:
                    print "isosceles triangle.a = %s, b = %s, c = %s\n"%(a,b,c)                
                else:
                    print "scalene triangle.a = %s, b = %s, c = %s\n"%(a,b,c)     
            else:
                print "Not a triangle.a = %s, b = %s, c = %s\n"%(a,b,c)         
        else:
            print "please check input data. a = %s, b = %s, c = %s\n"%(a,b,c)
