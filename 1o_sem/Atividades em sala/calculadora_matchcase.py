#entrada de dados


match op:
    case '+':
        result = num_a + num_b
    case '-':
         result = num_a - num_b
    case '*':
        result = num_a * num_b
    case '/':
        if num_b != 0:
           result = num_a / num_b
        else:
            print("impossível dividir por zero!")
    case '_':
        print("Operador inválido!")
