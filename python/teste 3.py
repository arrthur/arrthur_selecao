import re
def verificartestes(qntteste):
    if qntteste>=1 and qntteste<=100:
        return True
    else:
        return False 
num_entrada = input("Informe a quantidade de usu�rios: ")
if verificartestes(num_entrada):
    for i in range(num_entrada):
        usuarios = input("Informe o usu�rio")
        if re.match("^[_|\.]\d+[a-zA-Z]*_?$", usuarios):
            print "VALIDO"
        else:
            print "INVALIDO"
else:
    print "Informe a quantidade de usu�rios corretamente"
