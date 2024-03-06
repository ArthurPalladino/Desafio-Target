#5) Escreva um programa que inverta os caracteres de um string.

string= 'Target Sistemas!'
cont=len(string)
contrario=str()
while cont>0:
    aux=string[cont-1]
    cont-=1
    contrario=contrario+aux
print(contrario)
