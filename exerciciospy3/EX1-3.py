
contador = 0
while n != 0:
    n = int(input("Informe um numero: "))
    if n % 2 == 0:
        contador += n
print(f'A soma dos números pares é {contador}')
