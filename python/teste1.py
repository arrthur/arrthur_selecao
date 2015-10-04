def verificartestes(qntteste):
    if qntteste>=1 and qntteste<=10:
        return True
    else:
        return False
    
def verificarnumeros(qntnumero):
    if qntnumero>=1 and qntnumero<=10**5:
        return True
    else:
        return False

t = input("Informe a quantidade de testes a serem realizados: ")

if verificartestes(t):
    for i in range(t):
        a = input("Informe a quantidade de elementos do vetor")
        if verificarnumeros(a):
            n = raw_input("informe os números")
            numeros = map(int, n.split())
            for ind, val in enumerate(numeros):
                if (val>=1 and val<=a):
                    esq = sum(numeros[:ind])
                    dire = sum(numeros[ind+1:])         
                    if esq==dire:
                        imp = True
                        break
                    else:
                        imp = False
                else:
                    print "Número menor que 0 ou maior que a quantidade do vetor"

            if imp:
                print ("SIM")
            else:
                print ("NÂO")
        else:
            print "Informe a quantidade certa de numeros"
                
                
      
else:
    print "Número de testes inválidos"
    

    
    


