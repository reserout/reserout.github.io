# кальколятор 2.0
import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()

print(Back.CYAN)
print(Fore.WHITE)

expr = input("Введите математическую операцию:")

result = numexpr.evaluate(expr)
## старый калькулятор:
#a = float(input("Введите первое число: "))
#b = float(input("Введите второе число: "))

#operation = input("Что сделать? (+,-,*,/):")
#result = 0

#if operation == "+":
#    result = a + b
#elif operation == "-":
#    result = a - b
#elif operation == "*":
#    result = a * b
#elif operation == "/":
#    result = a / b
    
print(f"Результат: {result}")
input()