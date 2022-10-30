def VerificaPrimo(n):
    mult = 0
    for count in range(2, n):
        if (n % count == 0):
            mult += 1
    if (mult == 0):
        return True
    else:
        return False


n = int(input("insira um numero de 1 a 100 para verificação: "))
if 0 < n <= 100:
    IsPrimo = VerificaPrimo(n)
    if IsPrimo:
        print("É primo")
    else:
        print("Não é primo")
else:
    print("numero fora do escopo")

