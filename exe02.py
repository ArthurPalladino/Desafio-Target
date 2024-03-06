#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
#informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

numero=int(input("Digite um número inteiro para saber se faz parte da sequência de Fibonacci: "))
fibonacci=0
soma=1

while fibonacci<numero:
    fibonacciantes=fibonacci
    fibonacci=fibonacci+soma
    soma=fibonacciantes
if fibonacci==numero:
        print("Esse número pertence a sequência!")
else:
        print("Esse número não pertence a sequência!")