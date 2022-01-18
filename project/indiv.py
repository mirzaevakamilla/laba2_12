#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def start_sum(start=0):
    def wrapper(func):
        def wrapped(args):
            return_sum = func(args)
            return return_sum + start
        return wrapped
    return wrapper


@start_sum(start=5)
def str_summary(string):
    a = [int(s) for s in string.split()]
    summary = sum(elem for elem in a)
    return summary


if __name__ == "__main__":
    string_inp = input("Введите строку цеых чисел: ")
    print(f"Сумма: {str_summary(string_inp)}")
