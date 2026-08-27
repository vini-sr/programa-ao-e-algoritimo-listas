x = 2
y = 5

if y > 8:
    y = y * 2
else:
    x = x * 2

print(x + y)





def calcular_resultado_parametrizado(x, y):
    if y > 8:
        y = y * 2
    else:
        x = x * 2

    return x + y

 
print(calcular_resultado_parametrizado(2, 5))
