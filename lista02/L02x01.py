
a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))


if a + b > c and a + c > b and b + c > a:
    print("Os valores podem formar um triângulo!")
    
    
    if a == b == c:
        print("Tipo: Equilátero (todos os lados iguais)")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles (dois lados iguais)")
    else:
        print("Tipo: Escaleno (todos os lados diferentes)")
else:
    print("Os valores NÃO podem formar um triângulo.")
