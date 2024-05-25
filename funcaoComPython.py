#função para realizar calculo de dois numeros de acordo com o operador
def calculadora(num1,num2,operador):
    if(operador == "+"):
        return num1 + num2;
    elif(operador == "-"):
        return num1 - num2;
    elif(operador == "/"):
        return num1 / num2;
    else:
        return num1 * num2;
        
    
#chamada do método
print(calculadora(1,2,"*"))