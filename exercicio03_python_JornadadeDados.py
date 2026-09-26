'''Exercício 3 – Trabalhando com operadores

Considere:

pontos = 7
vitorias = 2
saldo_gols = 4

Crie expressões que respondam às seguintes perguntas:

A seleção possui mais de 5 pontos?
A seleção possui exatamente 3 vitórias?
O saldo de gols é maior ou igual a 0?
A seleção possui mais de 5 pontos e saldo de gols positivo?
A seleção possui 3 vitórias ou mais de 6 pontos?

Mostre o resultado de cada expressão.'''

pontos = 7
vitorias = 2
saldo_gols = 4

print("A seleção possui mais de 5 pontos?")
if pontos >=5:
    print(f'A seleção possui {pontos}')
else:
    print("A seleção não possui mais de 5 pontos")


print("A seleção possui exatamente 3 vitórias?")
if vitorias == 3:
    print('Sim a seleção possui exatamente 3 vitórias')
else:
    print(f'A seleção possui {vitorias}')


print("O saldo de gols é maior ou igual a 0?")
if saldo_gols >=0:
    print(f'Sim a seleção possui saldo de gols de {saldo_gols}')
else:
    print("Não possui saldo de gols negativo")


print("A seleção possui mais de 5 pontos e saldo de gols positivo?")
if pontos>=0 and saldo_gols >=0:
    print('Sim')
else:
    print("Não")

print("A seleção possui 3 vitórias ou mais de 6 pontos?")
if vitorias>=3 or pontos>6:
    print("Sim")
else:
    print("Não")