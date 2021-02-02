vPermitida = float(input("Qual a velocidade permitida? "))
vMotorista = float(input('Qual velocidade do motorista? '))

vPermitida20 = (vPermitida *0.2) + vPermitida

vPermitida50 = (vPermitida *0.5) + vPermitida

if vMotorista <= permitida:
    print("Tudo certo, nao precisa pagar multa ")
elife vMotorista > vPermitida and vMotorista <= vPermitida20:
    print("Voce cometeu infraçao media\nAssim ira pagar R$85.00 e receber 4 pontos na carteira")    
elife vMotorista > vPermitida20 and vMotorista <= vPermitida50:
    print("Voce cometeu infraçao grave\nAssim ira pagar R$127.00 e receber 5 pontos na carteira ")
elife vMotorista > vPermitida50:
    print("Voce cometeu infraçao gravissima\nAssim ira pagar R$547.00 alem de receber 7 pontos carteira\n ter carteira apreendida e \nTer o direito de dirigir suspeito")