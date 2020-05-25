#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Book:
    
    __slots__ = ['_name', '_author', '_code']
    
    def __init__(self, author, name):
        self._name   = name
        self._author = author
        self._code   = 0
        
        if self._name == '':
            raise ValueError()

    def __str__(self):
        res = "[%d] %s %s" % (self._code, self._author, self._name)
        return res
    
    def SetCode(self, code):
        self._code = code
        
    def tag(self):
        return [i for i in self._name.split() if i[0].isupper()]

class Library:
    LastCode = 0
    __slots__ = ['_num', '_address', '_books', '_BookNum']
    
    def __init__(self, num, address):
        
        self._num = num
        self._address = address
        self._BookNum = 0
        self._books = []
    
    def __iadd__(self, other):
        
        if isinstance(other, Book):
            self.__class__.LastCode += 1
            other.SetCode(self.__class__.LastCode)
            self._books.append(other)
            
        else:
            raise ValueError()
        return self
            
    def __str__(self):
        
        res = "%d %s\n" % (self._num, self._address)
        for book in self._books:
            res += str(book) + "\n"
            
        return res
    
    def __iter__(self):
        self._BookNum = 0
        return self
    
    def __next__(self):
        if self._BookNum < len(self._books):
            book = self._books[self._BookNum]
            self._BookNum += 1
            return book
        else:
            raise StopIteration
            
if __name__ == "__main__":
    lib = Library(1, "51 Some str., NY")
    lib += Book("Leo Tolstoi", "War and Peace")
    lib += Book("Charles Dickens", "David Copperfield")
    
    for book in lib:
        print(book)
        print(book.tag())