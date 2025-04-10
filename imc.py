p = float(input('Peso = '))
a = float(input('Altura = '))
imc = float(p/(a*a))

def classificacao():
    if imc <= 18.5:
        print('MAGREZA')
    elif imc < 25:
        print('NORMAL')
    elif imc < 30:
        print('SOBREPESO')
    elif imc < 40:
        print('OBESIDADE')
    elif imc > 40:
        print('OBESIDADE GRAVE')

print('')

print('      IMC	     CLASSIFICAÇÃO     OBESIDADE')
print('')
print('MENOR QUE  18,5	      MAGREZA	           0')
print('ENTRE 18,5 E 24,9     NORMAL               0')
print('ENTRE 25,0 E 29,9     SOBREPESO            I')
print('ENTRE 30,0 E 39,9     SOBESIDADE	   II')
print('MAIOR QUE 40,0	      OBESIDADE GRAVE      III')
print('')
print('')
print('Seu IMC é', imc, )
print('')
print('SUA CLASSIFICAÇÃO É:')
classificacao()
