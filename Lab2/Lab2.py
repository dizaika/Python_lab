#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ex1():
    f = open('D:\sometext.txt', 'rt')
    
    symbCount = 0
    res = {}
    for line in f:
        for c in line:
            if c.isalpha():
                if res.get(c.upper()) is None:
                    res[c.upper()] = 0
                else:
                    res[c.upper()] += 1
                symbCount += 1    
                
    for i in res:
        res[i] = res[i] / symbCount * 100
    
    ItemsList = sorted(res.items(), key=(lambda x: -x[1]))
    for i in ItemsList:
        print(i[0], i[1])
        
def ex2(search_path):
    import os, glob, subprocess, hashlib
    print("Идёт поиск дублирующихся файлов в", search_path)
    result = {}
    
    def ParseDir(parse_path):
        files = glob.glob(parse_path+"/*")
        
        for f in files:
            if os.path.isdir(f):
                ParseDir(f)    
            else:
                with open(f, 'rb') as file:
                    data = file.read()
                    res = hashlib.md5(data).hexdigest()
                    if result.get(res) is None:
                        result[res] = [f]
                    else:
                        result[res].append(f)
            
    ParseDir(search_path)
    
    for i in result:
        files = result[i]
        if len(files) > 1:
            print(i)
            for _ in files:
                print("\t"+_)
                
def ex3(parse_path, playlist):
    import os, glob
    
    filelist = sorted([os.path.basename(i) for i in glob.glob(parse_path+"/*.mp3")])
    
    for music in open(playlist, 'rt'):
        music_parts = music.split(' ')
        music_num = music_parts[0]
        music_name = ' '.join(music_parts[1:-1])
        
        for filename in filelist:
            if ''.join(filename.split('.')[0:-1]) == music_name:
                Old_File_Name = parse_path + '/' + filename
                New_Name      = parse_path + '/' + music_num + filename
                os.rename(Old_File_Name, New_Name)
                print('rename ', Old_File_Name, 'to', New_Name)
                
def ex4(File_Name):
    import os,re
    
    if os.path.exists(File_Name):
        with open(File_Name) as f:
            for i,line in enumerate(f):
                res = re.findall("\d{2}\-\d{2}\-\d{4}", line)
                for g in res:
                    print("Строка %d позиция %d : найдено '%s'" % (i, line.index(g[0]), g[0]))
                        
def ex5():
    import re
    
    st = input("Введите текст\n")
    
    for word in st.split():
        res = re.findall("(^[A-Z]\D*\d{2}$)|(^[A-Z]\D*\d{4}$)", word)
        for i in res:
            print(i)
        
if __name__ == "__main__":
    #ex2('D:\Изображения')
    #ex3('D:\Музыка', 'D:\Музыка\playlist.txt')
    #ex4('D:\file.txt')
    ex5()