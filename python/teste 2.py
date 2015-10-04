def qnt_brinquedos(n, k):
    if n>=1 and n<=10**5:
        return True
        
    else:
        print ("Informe a quantidade de brinquedos corretamente")
    if k>=1 and k<=10**9:
        return True
        
    else:
        print ("Informe a quantidade de dinheiro corretamente")
    

        
n, k = map(int, raw_input("Informe a quantidade de brinquedos e o seu dinheiro, respectivamente: ").split())
if qnt_brinquedos(n, k):
    precos = raw_input("Informe os preços: ")
    numeros = map(int, precos.split())
    qnt = 0
    novo_valor = 0
    if len(numeros) == n:
        for i in numeros:
            if (i>=1 and i<=10**9) and numeros.count(i)<2:
                if i<k:
                    novo_valor = novo_valor+i
                    if novo_valor<k:
                        qnt = qnt+1
            else:
                print ("Informe o preço corretamente")
                break
        print qnt
    else:
         print ("Informe a quantidade certa de brinquedos")
    
        
        
    


