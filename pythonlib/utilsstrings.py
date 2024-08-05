# utils/strings.py
def contar_vogais(texto):
    return sum(1 for char in texto if char.lower() in 'aeiou')

def inverter_texto(texto):
    return texto[::-1]

# utils/matematica.py
def soma(a, b):
    return a + b

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)