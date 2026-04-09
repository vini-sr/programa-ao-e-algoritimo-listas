peso = float(input("Digite o peso de peixes (kg): "))
limite = 50.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00
else:
    excesso = 0
    multa = 0

print(f"Excesso: {excesso:.2f} kg")
