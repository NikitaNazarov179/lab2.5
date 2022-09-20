#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Определить, является ли кортеж упорядоченным по возрастанию.
#В случае отрицательногоответа определить номер первого
#элемента, нарушающего такую упорядоченность.

if __name__ == '__main__':
    array = tuple(map(int, input().split()))
    result = None

    for n, i in enumerate(array):
        if (array[n]) > (array[n + 1]):
            result = array[n + 1]
            break

    if result is None:
        print('Последовательность упорядочена')
    else:
        print('Первое число, нарушающее упорядоченность: ', result)
