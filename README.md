# 📌 Teste do Lema do Bombeamento

Este projeto é um script em Python que permite testar se determinadas cadeias violam ou não o **Lema do Bombeamento** para linguagens regulares.

## 🔍 O que é o Lema do Bombeamento?

O lema do bombeamento é uma técnica usada para **provar que uma linguagem não é regular**. Ele afirma que para toda linguagem regular existe um inteiro p (constante de bombeamento), tal que qualquer cadeia w da linguagem com comprimento maior ou igual a p pode ser dividida em três partes: **x, y e z**, obedecendo algumas condições. 

Este script testa essas divisões e verifica se ao repetir a parte y, a nova cadeia ainda pertence à linguagem.

## ⚙️ Como funciona

O usuário escolhe uma linguagem, define um valor de p e fornece uma cadeia w. O programa testa automaticamente várias divisões possíveis de w e verifica se alguma violação ao lema ocorre.

Se violar o lema, a linguagem **não é regular**.  
Se nenhuma violação for encontrada, **não significa que é regular**, apenas que não foi possível provar o contrário com os testes realizados.

## ✏️ Linguagens suportadas

1. **L = { aⁿ | n ≥ 0 }**  
   Cadeias compostas apenas por letras "a".

2. **L = { aⁿbⁿ | n ≥ 1 }**  
   Mesma quantidade de "a"s seguidos por mesma quantidade de "b"s.

3. **L = { (ab)ⁿ | n ≥ 0 }**  
   Cadeias compostas por repetições do padrão "ab".

## ▶️ Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/LuKsKT/lema-bombeamento.git
   cd lema-bombeamento
