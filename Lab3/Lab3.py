#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Fraction(object):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()
        
    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)
    
    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g
        
    def __neg__(self):
        return Fraction(-self.__num, self.__den)
        
    def __invert__(self):
        return Fraction(self.__den, self.__num)
        
    def __pow__(self, other):
        return Fraction(self.__num**other, self.__den**other)
        
    def __float__(self):
        return self.__num / self.__den
    
    def __int__(self):
        return int(self.__num/self.__den)
        
    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)
        
frac = Fraction(7, 2)
print(-frac)
print(~frac)
print(frac**2)
print(float(frac))
print(int(frac))