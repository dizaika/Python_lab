#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class StringFormatter:
    def __init__(self, string):
        self._string = string
    
    def DeleteWordsShortestThat(self, LetterCount):
        self._string = ' '.join(list(filter(lambda x: len(x) >= LetterCount, list(self._string.split()))))
        return self._string
    
    def MaskDecimal(self):
        def MaskDecimal(ch):
            if ch.isdecimal():
                return '*'
            else:
                return ch
                
        self._string = ''.join(list(map(MaskDecimal, self._string)))
        return self._string
    
    def InsertWhiteSpace(self):
        self._string = ' '.join(list(self._string))
        return self._string
    
    def SortWordBySize(self):
        self._string = ' '.join(sorted(list(self._string.split()), key=len))
        return self._string
    
    def SortLexycographic(self):
        self._string = ' '.join(sorted(list(self._string.split())))
        return self._string
        
if __name__ == "__main__":
    stringFmt = StringFormatter("6t66 6g7gv 7V&D &^DDF^ &VDTSvd 7df 76d f76d76qf 766 6d 8d tgq87wg d8gd 78 gtd87w dg87g d79w dgd87ygw d8")
    
    print(stringFmt.DeleteWordsShortestThat(6))
    print(stringFmt.MaskDecimal())
    print(stringFmt.InsertWhiteSpace())
    print(stringFmt.SortWordBySize())
    print(stringFmt.SortLexycographic())
    