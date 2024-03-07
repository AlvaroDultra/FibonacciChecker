a=0
c=1
numero =int(input("Digite um numero "))
if numero==a:
    print("seu numero esta na sequencia de Fibonacci")
elif numero<a:
    print("seu numero não esta na sequencia de Fibonacci")
while numero>a:
    soma=a+c
    
    a=c
    c=soma 
    if a==numero:
        print("seu numero está na sequencia de Fibonacci")
        break
    elif a>numero:
        print("seu numero não esta na sequencia de Fibonacci")
        break

