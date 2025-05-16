def calculadora(operacao, a, b):
    
    def soma(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b
    
    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b
    
    
    match operacao:
        case "+":
            return soma(a, b)
        
        case "-":
            return subtracao(a, b)  
        
        case "*":
            return multiplicacao(a, b)
        
        case "/":
            if b == 0:
                return "Erro: Divisão por zero não é permitida."
            return divisao(a, b)
        
        
        
        
op = calculadora("+", 10, 5)
print(op)
op = calculadora("-", 10, 5)
print(op)
op = calculadora("*", 10, 5)
print(op)
op = calculadora("/", 10, 5)
print(op)
op = calculadora("/", 10, 0)
print(op)

