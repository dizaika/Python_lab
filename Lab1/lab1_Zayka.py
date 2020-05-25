#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math

def ex1():
    try:    
        x = input('Введите вещественное число : ').replace(',', '.').split('.')
        if int(x[0]) < 0:
            raise ValueError    
        else:
            print(x[0], ' руб. ', int(float('0.'+x[1])*100), ' коп. ')
    except:
        print('Некорректный формат!')
        
def ex2():
    x = [1, 2, 3, 4, 5, 6]
    for a, b in zip(x[1::], x):
        if a < b:
            print('False')
            exit
    print('True')
    
def ex3():
    st = input('Введите номер дебетовой карты ')
    print(st[0:4:]+'*'*8 + st[-4::])
        
def ex4():
    text = input("Введите текст\n").split()
    
    print([i for i in text if len(i)>7])
    for i in text:
        if len(i) > 7:
            print(i)
    for i in text:
        if (len(i) >= 4) and (len(i) <= 7):
            print(i)
    for i in text:
        if len(i) < 4:
            print(i)
            
            
def ex5():
    st = input("Введите строку :\n")
    res = ""
    for i in range(len(st)):
        res += st[i]
        if (i > 0) and (res[i-1].isupper()):
            res = res[0:i:] + res[i].upper()
            
    print(res)
    
def ex6():
    st = input("Введите текст :\n")
    res = [c for c in set(st) if st.count(c) == 1]
    print(res)        
    
def ex7():
    strings = ["www.google.com", "www.vk.com", "www.ok.ru", "www.proghub"]
    tmp = ["http://"+st for st in strings if st.startswith("www")]
    res = [st if st.endswith(".com") else st+".com" for st in tmp]
    print(res)
    
def ex8():
    n = random.randint(1, 10000)
    res = [random.randint(0, 9) for x in range(n)]
    res.extend([0 for _ in range(2**(int(math.log2(n))+1)-n)])
    print(res)
    print(n, len(res))
    
def ex9():
    moneys = {1000:10, 100:6, 50:10, 10:20}
    print(moneys)
    summa = int(input("Введите сумму :\n"))
    
    thousands = summa // 1000
    summa -= thousands * 1000
    
    hundreds = summa // 100
    summa -= hundreds * 100
    
    fifth = summa // 50
    summa -= fifth * 50
    
    tens = summa // 10
    summa -= tens * 10
    
    if (thousands <= moneys[1000]) and (hundreds <= moneys[100]) and (fifth <= moneys[50]) and (tens <= moneys[10]):
        print("%d*1000 + %d*100 + %d*50 + %d*10" % (thousands, hundreds, fifth, tens))
    else:
        print("Операция не может быть выполнена")
        
def ex10():    
    st = input("Введите пароль\n")
    
    summ = 0
    for a, b in zip(st, st[1::]):
        summ += abs(ord(b)-ord(a))
      
    mid = summ // len(st)
    
    if  mid > 20:
        print("Хороший")
    elif mid > 10:
        print("Средний")
    elif mid > 8:
        print("Пойдёт")
    else:
        print("Плохой")  
        
def ex11():
    def frange(first, last, step):
        first *= 10**10
        last *= 10**10
        step *= 10**10
        
        while first <= last:
            yield first/10**10
            first += step
        
    for x in frange(1, 5, 0.1):
        print(x)
    
def ex12():
    def get_frames(signal, size, overlap):
        step = int(size*overlap)
        pos = 0
        end = len(signal)-size
        while pos <= end:
            yield signal[pos:pos+size:]
            pos += step
    
    signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    for frame in get_frames(signal, size=4, overlap=0.5):
        print(frame)
            
def ex13():
    def extra_enumerate(x):
        temp = 0
        for elem in x:
            temp += elem
            yield elem, temp, temp/sum(x)  
            
        
    x = [1, 3, 4, 2]
    
    for elem, cum, frac in extra_enumerate(x):
        print(elem, cum, frac)
        
def ex14():
    
    def non_empty(func):
        def _wrapper():
            return [e for e in func() if ((e != "None") and (e != ""))]
        return _wrapper
    
    @non_empty
    def get_pages():
        return ['chapter1', '', 'contents', '', 'line1']
    
    print(get_pages())
    
def ex15():
    def pre_process(a=0.97):
        def decorator(func):
            def _wrapper(*args, **kwargs):
                
                lst = args[0]
                for i in range(len(lst)):
                    if i > 0:
                        lst[i] -= a*lst[i-1]
                    
                return func(*args)
            return _wrapper
        return decorator
    
    @pre_process(0.93)
    def plot_signal(s):
        for sample in s:
            print(sample)
    
    signal = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plot_signal(signal)
    
def ex16():
    import random
    import datetime
    import itertools
    
    teams = ['Россия', 'Испания', 'Италия', 'Франция', 
             'Англия', 'Германия', 'Швеция', 'Дания',
             'Греция', 'Бельгия', 'Китай', 'Бразилия', 
             'Аргентина', 'Урлай', 'Турция', 'Португалия']
    
    random.shuffle(teams)
    teams = [teams[i*4:i*4+4] for i in range(0, 4)]
    groups = [group for group in itertools.combinations(teams, 4)]
    for i in range(0, 4):
        print('Группа №', i+1, groups[0][i])
    
    now = datetime.datetime.now()
    start = datetime.datetime(now.year, 9, 14, 22, 45)
    for i in range(1, 16):
        print('Игра №', i, start.strftime('%d/%m/%Y %H:%M'))
        start += datetime.timedelta(days=14)
    
if __name__ == "__main__":
    ex6()