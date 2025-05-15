#PARTE 0: desenho
print('')
print('======Programa iniciado com sucesso======')

print('')
print('')
print('              I3')
print(' ┌────R2──────┬────V5───R4────┐')
print(' │            │               │')
print(' V1           V2              R5')
print(' │     I1     │        I2     │')
print(' R1           R3              V6')
print(' │            │               │')
print(' └───V3──V4───┴───R6──────────┘')



#PARTE 1: DADOS

#*O programa deve ter as seguintes características:
#*Solicitar ao usuário colocar os valores dos resistores e fontes do circuito.

print('')
print('Resistências:') #Solicita ao usuário colocar os valores dos resistores
R1 = float(input('* Digite o valor de R1: '))
R2 = float(input('* Digite o valor de R2: '))
R3 = float(input('* Digite o valor de R3: '))
R4 = float(input('* Digite o valor de R4: '))
R5 = float(input('* Digite o valor de R5: '))
R6 = float(input('* Digite o valor de R6: '))
print('')
print('Fontes:') #Solicita ao usuário colocar os valores das fontes
V1 = float(input('* Digite o valor de V1: '))
V2 = float(input('* Digite o valor de V2: '))
V3 = float(input('* Digite o valor de V3: '))
V4 = float(input('* Digite o valor de V4: '))
V5 = float(input('* Digite o valor de V5: '))
V6 = float(input('* Digite o valor de V6: '))
print('')


#PARTE 2: CÁLCULOS BÁSICOS

#*Realizar os devidos cálculos:

MAV= (V4-V3+V1-V2) # Soma de todas as fontes da malha Alfa
MAR= (R1+R2)       # Soma de todas as resistências da malha Alfa (menos R3)


MBV= (V6+V2-V5)    # Soma de todas as fontes da malha Beta
MBR= (R4+R5+R6)    # Soma de todas as resistências da malha Beta


#PARTE 3: MATRIZ E DETERMINANTE

# DIAGONAIS PRINCIPAIS:      #Diagonais D1 e D2 são iguais a 0
D3 = ((-1)*MAR*MBR)
 
# DIAGONAIS SECUNDARIAS:     #Diagonal C3 é igual a 0
C1 = (-1)*(MAR*(-R3))
C2 = ((-R3)*MBR)

# VALOR DO DETERMINANTE:
D = D3-C1+C2

# Dx                    
Dx1 = (-R3)*MBV
Dx2 = MAV*MBR
Dx3 = MAV*R3
Dx = Dx1-Dx2-Dx3
I1 = -Dx/D                  #Valor da Corrente I1

#Dy
Dy1 = MAV*R3
Dy2 = MAR*MBV
Dy3 = R3*MBV
Dy = Dy1+Dy2+Dy3
I2 = -Dy/D                  #Valor da Corrente I2

#Dz
Dz1 = MAV*MBR
Dz2 = MBV*MAR
Dz= -Dz1+Dz2
I3 = Dz/D                   #Valor da Corrente I3

print('')

print('==== RESULTADOS FINAIS ===============')

print('')
print('I1:')
print((I1*1000), 'miliAmperes')              #Valor de I1 em mA
print('ou')
print(I1, 'Amperes')                         #Valor de I1 em A
print('')

print('////////////////////////////////')    #Separação visual pra facilitar a leitura das respostas

print('')
print('I2:')
print((I2*1000), 'miliAmperes')              #Valor de I2 em mA
print('ou')
print(I2, 'Amperes')                         #Valor de I2 em A
print('')

print('////////////////////////////////')    #Separação visual pra facilitar a leitura das respostas

print('')
print('I3:')
print((I3*1000), 'miliAmperes')              #Valor de I3 em mA
print('ou')
print(I3, 'Amperes')                         #Valor de I3 em A

print('')
print('')
I0 = (I1+I2+I3)

A = int(1)

if {( I0 > float(0)) and (I0 < float(1/2))}:
  print('VALOR CORRETO, POIS A SOMA DAS CORRENTES É IGUAL A ZERO')
  
print('')
print('')

print('escreva 1 para ver o passo a passo dos cálculos:')
A = int(input(''))

    
if A == 1:
    print('')
    print('')
    print('##################################################')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('CÁLCULOS BÁSICOS')
    print('')
    print('')
    print('')
    print('Somar as tensões da malha Alfa:')  
    print('')
    print('MAV = Soma de todas as tensões de Alfa')
    print('MAV = (V1 - V2 - V3 + V4)')
    print('MAV =', '(', V1, '-', V2, '-', V3, '+', V4, ')')
    print('MAV =', (V1-V2-V3+V4))
    
    print('')
    
    print('Somar as resistências da malha Alfa (menos R3):')
    print('MAR = (R1 + R2)')
    print('MAR =', R1, '+', R2, ')')
    print('MAR =', (R1+R2))

    print('')

    print('Somar todas as fontes da malha Beta:')
    print('MBV = (V6 + V2 - V5)')
    print('MBV = (', V6, '+', V2, '-', V5, ')')
    print('MBV =', (V6+V2-V5))
    print('')
    print('Somar todas as resistências da malha Beta')
    print('MBR= (R4 + R5 + R6)')
    print('MBR=', '(', R4, '+', R5, '+', R6)
    print('MBR= (R4+R5+R6)')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('=======================================================')
    print('')
    print('')

    print('MATRIZ E DETERMINANTE')
    print('')
    print('MATRIZ')
    print('--> Diagonais Principais:')
    print('')
    print('D1 = 1*0*(-R3)')
    print('D2 = (-1)*R3*0')

    print('')
    print('////////////////////////////////////////////////////////')
    print('')

    print('*As diagonais D1 e D2 são iguais a 0, então eles não são')
    print('utilizados nos cálculos.')
    print('')
    print('D3 = ((-1)*MAR*MBR)')
    print('D3 = ((-1)*', MAR, '*', MBR, ')')
    print('D3 =', ((-1)*MAR*MBR))

    print('')
    print('=======================================================')
    print('')

    print('')
    print('--> Diagonais Secundárias:')
    print('')
    print('C1 = (-1) * (MAR * (-R3)')
    print('C1 = (-1) * (', MAR, '*(', (-R3), ')', ')')
    print('C1 =', (-1)*(MAR*(-R3)))
    print('C2 = ((-R3) * MBR)')
    print('C2 = ((', (-R3), ')', '*', MBR, ')')
    print('C2 =', ((-R3)*MBR))
    print('*Diagonal C3 é igual a 0:')
    print('C3 = (-1) * 0 * 0')
    print('Portanto, não a utilizamos nos cálculos também')
    print('')
    print('   (i)   Mas por que é zero?')
    print('')
    print('          isso se dá porque assumimos os valores')
    print('          desconhecidos (I1, I2 e I3) como 0.')

    print('')
    print('')
    print('')
    print('=======================================================')
    print('')
    print('')
    print('')
    
    print('VALOR DO DETERMINANTE:')
    print('D = D3 - C1 + C2')
    print('D =', D3, '-', C1, '+', C2)
    print('D =', D3-C1+C2)

    print('')
    
    print('Dx')
    
    print('')
    print('Dx1 = (-R3) * MBV')
    print('Dx1 = (', (-R3), ') *', MBV)
    print('Dx1 =', (-R3)*MBV)
    print('')
    print('Dx2 = MAV * MBR')
    print('Dx2 =', MAV, '*', MBR)
    print('Dx2 =', MAV * MBR)
    print('')
    print('Dx3 = MAV * R3')
    print('Dx3 =', MAV, '*', R3)
    print('Dx3 =', MAV*R3)
    
    print('')
    print('')
    
    print('Dx = Dx1 - Dx2 - Dx3')
    print('Dx =', Dx1, '-', Dx2, '-', Dx3)
    print('Dx =', Dx1-Dx2-Dx3)

    print('')
    print('')
    print('=======================================================')
    print('')
    print('')
    print('')
    
    print('Dy')
    
    print('')
    print('Dy1 = MAV * R3')
    print('Dy1 =', MAV, '*', R3)
    print('Dy1 =', MAV*R3)
    print('')
    print('Dy2 = MAR * MBV')
    print('Dy2 =', MAR, '*', MBV)
    print('Dy2 =', MAR*MBV)
    print('')
    print('Dy3 = R3 * MBV')
    print('Dy3 =', R3, '*', MBV)
    print('Dy3 =', R3*MBV)
    
    print('')
    print('')
    
    print('Dy = Dy1 + Dy2 + Dy3')
    print('Dy =', Dy1, '+', Dy2, '+', Dy3)
    print('Dy =', Dy1+Dy2+Dy3)
    
    print('')
    print('')
    print('=======================================================')
    print('')
    print('')
    print('')
    
    print('Dz')
    
    print('')
    print('Dz1 = MAV * MBR')
    print('Dz1 =', MAV, '*', MBR)
    print('Dz1 =', MAV*MBR)
    print('')
    print('Dz2 = MBV * MAR')
    print('Dz2 =', MBV, '*', MAR)
    print('Dz2 =', MBV*MAR)
    
    print('')
    print('')
    
    print('Dz= -Dz1 + Dz2')
    print('Dz=', -Dz1, '+', Dz2)
    print('Dz=', -Dz1+Dz2)
    
    print('')
    print('')
    print('=======================================================')
    print('')
    print('')


                
    print('')
    print('')
    print('')
    print('VALORES DAS CORRENTES')
    print('')
    print('Valor da Corrente I1:')
    print('I1 = -Dx / D')
    print('I1 =', -Dx, '/', D)
    print('I1 =', -Dx/D)
    print('')
    print('////////////////////////////////////////////////////////')
    print('')
    print('Valor da Corrente I2:')
    print('I2 = -Dy / D')
    print('I2 =', -Dy, '/', D)
    print('I2 =', -Dy / D)

    print('')
    print('////////////////////////////////////////////////////////')
    print('')
    print('Valor da Corrente I3:')
    print('')
    
    print('I3 = Dz / D')
    print('I3 =', Dz, '/', D)
    print('I3 =', Dz / D)
    
    print('')
    print('')
    print('')
    print('')
    
    print('Para passar a corrente de Amperes para miliAmaperes')
    print('precisamos multiplicar cada corrente por 1000:')
    print('')
    print('I1 = I1 * 1000')
    print('I1 =', I1, '* 1000')
    print('I1 =', I1 * 1000, 'mA')
    print('')
    print('I2 = I2 * 1000')
    print('I2 =', I2, '* 1000')
    print('I2 =', I2 * 1000, 'mA')
    print('')
    print('I3 = I3 * 1000')
    print('I3 =', I3, ' * 1000')
    print('I3 =', I3 * 1000, 'mA')
    
    print('')
else:
    print('')
    print('Tudo bem! :D')
