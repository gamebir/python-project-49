import prompt
from random import randint

"""приветствие"""
def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n ")
    print(f"Hello, {name}")
    return name


"""переворачиваем ответ"""
def rev(answer):
    return "no" if answer == "yes" else "yes"


"""Присваеваем символу математическую операцию"""
def math_action(number1, number2, oper):
    question = 0
    if oper == "+":
        question = number1 + number2
    elif oper == "-":
        question = number1 - number2
    elif oper == "*":
        question = number1 * number2
    return question


"""список делителей"""
def div(number):
    list_div = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_div.append(i)
    return list_div
 

"""поиск наибольшего общего делителя"""
def gr_com_div(list_div1, list_div2):
    return max(set(list_div1) & set(list_div2))

"""проверка на число"""
def is_digit(text):
	value = input(text)
	return int(value) if value.isdigit() else is_digit(text)

"""генерируем последовательность"""
def gen_prog(step=3):
	result = ""
	n = randint(0,100)
	for i in range(n,n+(step*10),step):
			result +=f"{i} "
	return result		
