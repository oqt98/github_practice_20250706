# calculator.pyの作成

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b




def check_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"



# 1つのファイルに複数の関数を設定するcalculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b
