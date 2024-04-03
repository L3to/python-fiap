
pares = 0
n = int(input("Informe um numero: "))
while n != 0:
    if n % 2 == 0:
        pares += n
    n = int(input("Informe um numero: "))
print(f'A soma dos números pares é {pares}')
