n1 = (input('Se você quiser descobrir espaço, digite: Espaço, Se você quiser descobrir Velocidade, digite: Velocidade, Se você quiser descobrir Tempo, digite: Tempo. Qual você escolheu?: '))
if (n1 == "Velocidade"):
    Velocidade1 = int(input('Qual o Tempo: '))
    Velocidade2 = int(input('Qual o Espaço: '))
    print (Velocidade2 / Velocidade1)
if (n1 == "Tempo"):
    Tempo1 = int(input('Qual a Velocidade: '))
    Tempo2 = int(input('Qual o Espaço: '))
    print (Tempo2 / Tempo1)
if (n1 == "Espaço"):
    Espaço1 = int(input('Qual a Velocidade: '))
    Espaço2 = int(input('Qual o Tempo: '))
    print (Espaço1 * Espaço2)
    
