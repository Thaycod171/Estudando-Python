'''
O que são tipos primitivos?
Imagine que você vai guardar informações no computador. Essas informações podem ser de vários tipos: números, textos, verdadeiros ou falsos, etc.
Cada tipo de informação tem uma forma diferente de ser guardada na memória. Essas formas básicas são chamadas de tipos primitivos.

É como se fossem caixinhas que servem para guardar tipos diferentes de dados.



💬 Tipos primitivos em Python
1. int (número inteiro)
O que é: Guarda números sem parte decimal.

Exemplo: 1, 42, -5, 0

Uso comum: Quando você precisa contar, somar, fazer operações matemáticas com números inteiros.
📌 Dica: Não tem vírgula. Só números inteiros mesmo!


2. float (número com ponto flutuante)
O que é: Guarda números com casas decimais (em Python, usamos ponto e não vírgula).

Exemplo: 3.14, -2.5, 0.0, 10.75

Uso comum: Quando você precisa trabalhar com medidas, notas, porcentagens, valores que não são inteiros.
📌 Dica: "Float" vem de "flutuante", porque o ponto pode “flutuar” na posição (ex: 0.1, 100.55).


3. str (string - texto)
O que é: Guarda qualquer texto: palavras, frases, letras, números como texto.

Exemplo: "Olá", 'Python', "123" (sim, mesmo parecendo número, aqui é texto!)

Uso comum: Quando você quer mostrar uma mensagem, guardar nomes, endereços, etc.
📌 Dica: Sempre fica entre aspas (simples ou duplas).


4. bool (booleano - verdadeiro ou falso)
O que é: Guarda apenas dois valores possíveis: True (verdadeiro) ou False (falso).

Exemplo: True, False

Uso comum: Usado em decisões do programa, como em comparações: "Esse número é maior que 10?"
📌 Dica: Começa com letra maiúscula: True, False




🧪 Como saber o tipo de uma variável?
Você pode usar a função type() em Python para descobrir o tipo:
'''
x = 10
print(type(x))  # Vai mostrar <class 'int'>


'''
🧠 Resumo em forma de tabela:
Tipo	    Nome completo	       Exemplo	         Representa o quê?
int	        Inteiro	              5, -3, 0	       Números sem parte decimal
float	    Ponto flutuante	      3.14, 2.0	       Números com casas decimais
str	        String (texto)	        "Olá"	         Texto, letras, frases
bool	    Booleano	         True, False	      Verdadeiro ou Falso


🎓 Exemplo completo
'''
nome = "Thayane"     # tipo str
idade = 19           # tipo int
altura = 1.65        # tipo float
maior_idade = True   # tipo bool

print(type(nome))        # str
print(type(idade))       # int
print(type(altura))      # float
print(type(maior_idade)) # bool


