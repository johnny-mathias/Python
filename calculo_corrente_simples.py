print('')
print('======Programa iniciado com sucesso======')

#O programa deve ter as seguintes características:

#Solicitar ao usuário colocar os valores dos resistores e fontes do circuito.
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


#Realizar os devidos cálculos:

MAV= (V4-V3+V1-V2) # -6
MAR= (R1+R2)       # 200  //  R3 =  100


MBV= (V6+V2-V5)    # 9
MBR= (R4+R5+R6)    # 900  // -R3 = -100

# DIAGONAIS PRINCIPAIS
D3 = ((-1)*MAR*MBR)   #   -180.000
 
# DIAGONAIS SECUNDARIAS
C1 = (-1)*(MAR*(-R3))   #  -20.000
C2 = ((-R3)*MBR)        #  -90.000

# VALOR DO DETERMINANTE
D = D3-C1+C2            # -290.000

# Dx
Dx1 = (-R3)*MBV
Dx2 = MAV*MBR
Dx3 = MAV*R3
Dx = Dx1-Dx2-Dx3
I1 = -Dx/D

#Dy
Dy1 = MAV*R3
Dy2 = MAR*MBV
Dy3 = R3*MBV
Dy = Dy1+Dy2+Dy3
I2 = -Dy/D

#Dz
Dz1 = MAV*MBR
Dz2 = MBV*MAR
Dz= -Dz1+Dz2
I3 = Dz/D

print('')

print('RESULTADOS FINAIS')
print('* Valor da corrente I1 =', I1, 'Amperes')   #Valor de I1 em A
print('ou', (I1*1000), 'miliAmperes')              #Valor de I1 em mA
print('* Valor da corrente I2 =', I2, 'Amperes')   #Valor de I2 em A
print('ou', (I2*1000), 'miliAmperes')              #Valor de I2 em mA
print('* Valor da corrente I3 =', I3, 'Amperes')   #Valor de I3 em A
print('ou', (I3*1000), 'miliAmperes')              #Valor de I3 em mA
