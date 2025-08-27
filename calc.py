# calc.py
import sys

def usage():
    print("Использование: python calc.py <a> <b>")
    print("Пример: python calc.py 2 5")
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
except ValueError:
    print("Ошибка: a и b должны быть числами")
    usage()

print(a + b)
