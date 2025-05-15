frutas = ["uva", "kiwi", "maca", "caqui"]
print(frutas[2])
frutas[2] = "laranja"
print(frutas)

variavel_do_valor_removido = frutas.pop(1)
print(frutas)

del frutas[0]
print(frutas)

frutas[1] = "banana"