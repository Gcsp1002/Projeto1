# Guilherme da Costa Sampaio Pinto
# TIA: 32011059
# Aula 09: While
'''
Em um campeonato de futebol existem cinco times	e cada um possui onze jogadores.
Faça um algoritmo que receba a idade (de 14 a 35), o peso (de 60.0 a 100.0) e
a altura (de 1.60 a 2.00) de cada um dos jogadores, calcule e mostre:
a) a quantidade	de jogadores menores de	idade (idade inferior a	18 anos);
b) a média das idades dos jogadores de cada time;
c) a  média das	alturas	de todos os jogadores do campeonato;	
d) a porcentagem de jogadores com mais de 80Kg entre todos os jogadores do
campeonato.
'''
jogador = 1
time = 1
menor = 0
pesados = 0
totalAltura = 0
totalIdade = 0

while time < 6:
      print('-'*20, 'Time ', time, '-'*20)
      while jogador < 12:
        print('{}º Jogador' .format(jogador))

        idade = int(input('Qual a idade do {}º Jogador? ' .format(jogador)))
        while idade < 14 or idade > 35:
            idade = int(input('Idade inválida. Insira a idade do {}º Jogador novamente: ' .format(jogador)))
        if idade < 18:
            menor += 1
        totalIdade = totalIdade + idade
        mediaIdade = totalIdade/11

        altura = float(input('Qual a altura do {}º Jogador? ' .format(jogador)))
        while altura < 1.6 or altura > 2.0:
            altura = float(input('Altura inválida. Insira a altura do {}º Jogador novamente: ' .format(jogador)))
        totalAltura = totalAltura + altura

        peso = float(input('Qual o peso do {}º Jogador? ' .format(jogador)))
        while peso < 60 or peso > 100:
            peso = float(input('Peso inválido. Insira o peso do {}º Jogador novamente: ' .format(jogador)))
        if peso > 80:
            pesados += 1
        print('-'*20)
        jogador += 1
      print('A média da idade do {}º time é {}.' .format(time, mediaIdade))
      print()
      time += 1
      totalIdade = 0
      jogador = 1

mediaAltura = totalAltura / 55
porcentPesados = (pesados / 55)*100
print('A quantidade de jogadores com idade inferior a 18 anos é ', menor)
print('A média de altura de todos os jogadores do campeonato é ', mediaAltura)
print('A porcentagem de jogadores com peso acima dos 80kg é ', porcentPesados)
            
      
