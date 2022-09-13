# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 00:06:18 2022

@author: KYLE
"""

import  math  
class Fraction(object):
    """
 User-defined ojbect to represent numeric fractions
 The top value, known as the numerator, can be any integer.
 The bottom value, called the denominator, can be any integer
greater than 0
    """

    def __init__(self,x,y):
        self.denominator=y        #分母
        self.numerator=x          #分子
    
        if self.denominator<0:    #如果分母小於零，正負號更和位置
            self.denominator= -self.denominator  
            self.numerator=   -self.numerator
        
         
        
        
        

    def __add__(self,other):     #加法自定義           
        denominator_N=self.denominator*other.denominator  #通分
        numerator_N  =self.denominator*other.numerator + other.denominator*self.numerator#通分後分子相加
        g=math.gcd(denominator_N,numerator_N)  #取最大公因數
        return Fraction(numerator_N//g,denominator_N//g)#約分後回傳

    def __sub__(self,other):     #減法自定義
        denominator_N=self.denominator*other.denominator #分母成分母_通分
        numerator_N  =-self.denominator*other.numerator + other.denominator*self.numerator #通分後分子相減
        g=math.gcd(denominator_N,numerator_N) #取最大公因數
        return Fraction(numerator_N//g,denominator_N//g)#約分後回傳

    def __mul__(self,other):     #乘法自定義
        denominator_N=self.denominator*other.denominator #分母乘以分母
        numerator_N =self.numerator *other.numerator  #分子乘以分子
        g=math.gcd(denominator_N,numerator_N) #取最大公因數
        return Fraction(numerator_N//g,denominator_N//g)#約分後回傳

    def __truediv__(self,other): #除法自定義
        denominator_N=self.denominator*other.numerator #分母乘以分子
        numerator_N =self.numerator *other.denominator #分子乘以分母
        g=math.gcd(denominator_N,numerator_N) #取最大公因數
        return Fraction(numerator_N//g,denominator_N//g)#約分後回傳

    def __eq__(self,other):     #等於自定義
        g=math.gcd(self.denominator,self.numerator) #取最大公因數(分數一)
        o=math.gcd(other.denominator,other.numerator) #取最大公因數(分數二)
        if self.numerator//g == other.numerator//o and self.denominator//g == other.denominator//o: #判斷約分後是否相等
            return True
        else:
            return False
    def __ne__(self,other):     #不等於自定義
        g=math.gcd(self.denominator,self.numerator)  #取最大公因數(分數一)
        o=math.gcd(other.denominator,other.numerator) #取最大公因數(分數二)
        if self.numerator//g == other.numerator//o and self.denominator//g == other.denominator//o: #判斷約分後是否相等
            return False
        else:
            return True    
     
    def __str__(self):         #STR自定義
        if self.numerator==self.denominator and self.denominator!=0:#分母分子相等=>結果為一
            return str('1')
        elif self.numerator==0 and self.denominator!=0:             #分子等於零且分母不等於玲且分母不等於零=>結果為零
            return (str(self.numerator))    
        elif self.denominator==0:           #分母等於零是錯誤的
            return str("Error") 
        else:
            return(str(self.numerator)+'/'+str(self.denominator))#回傳分數形式
