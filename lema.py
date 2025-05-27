# Função que testa o lema do bombeamento para uma linguagem dada, valor p e cadeia w
def testar_lema_bombeamento(linguagem, p, w, max_repeticoes=3):
    n = len(w)
    
    # Se o comprimento de w for menor que p, o lema não se aplica
    if n < p:
        return f"A cadeia w='{w}' é menor que o valor de bombeamento p={p}. O lema não se aplica."

    encontrou_violacao = False

    # Geração de todas as divisões possíveis de w em x, y, z com |xy| ≤ p e |y| > 0
    for i in range(p + 1):
        for j in range(1, p - i + 1):
            k = n - i - j
            if i + j + k != n:
                continue  # Garante que x + y + z = w

            x = w[:i]
            y = w[i:i + j]
            z = w[i + j:]

            print(f"\nDivisão: x='{x}', y='{y}', z='{z}'")

            # Testa repetições de y (bombeamento) de 0 até max_repeticoes
            for repeticoes in range(max_repeticoes + 1):
                nova_cadeia = x + (y * repeticoes) + z
                pertence = linguagem(nova_cadeia)

                print(f"  {repeticoes} repetições de y: '{nova_cadeia}' -> {'PERTENCE' if pertence else 'NÃO PERTENCE'}")

                # Se alguma repetição gerar uma cadeia fora da linguagem, há violação do lema
                if not pertence:
                    print(f"\n⚠️ Violação: repetindo y='{y}' {repeticoes} vezes gerou '{nova_cadeia}', que não pertence à linguagem.")
                    encontrou_violacao = True
                    return f"\n✅ O lema foi violado para a divisão x='{x}', y='{y}', z='{z}'. A linguagem não é regular."

    # Se nenhuma repetição gerou cadeia fora da linguagem, o lema não foi violado
    if not encontrou_violacao:
        return "\n✅ Para todas as divisões e repetições testadas, a cadeia permaneceu na linguagem. Nenhuma violação encontrada."

# Linguagem 1: somente letras 'a' (ex: '', 'a', 'aa', 'aaa', ...)
def linguagem_somente_a(s):
    return all(c == 'a' for c in s)

# Linguagem 2: número de 'a's igual ao número de 'b's e 'a's vêm antes dos 'b's (ex: 'ab', 'aabb', 'aaabbb')
def linguagem_an_bn(s):
    n_a, n_b = 0, 0
    estado = 0
    for char in s:
        if estado == 0:
            if char == 'a':
                n_a += 1
            elif char == 'b':
                estado = 1
                n_b += 1
            else:
                return False  # caractere inválido
        elif estado == 1:
            if char == 'b':
                n_b += 1
            else:
                return False  # encontrou um 'a' depois dos 'b's
    return n_a == n_b and n_a > 0

# Linguagem 3: cadeia composta por repetições de 'ab' (ex: '', 'ab', 'abab', 'ababab')
def linguagem_ab_n(s):
    if len(s) % 2 != 0:
        return False  # deve ter número par de caracteres
    for i in range(0, len(s), 2):
        if s[i:i+2] != 'ab':
            return False  # encontrou algo diferente de 'ab'
    return True

def menu():
    print("\n=== Teste do Lema do Bombeamento ===")
    print("Escolha a linguagem:")
    print("1 - L = { aⁿ | n ≥ 0 }")
    print("2 - L = { aⁿbⁿ | n ≥ 1 }")
    print("3 - L = { (ab)ⁿ | n ≥ 0 }")

    opcao = input("Digite o número da linguagem: ")

    # Seleciona a função da linguagem com base na opção
    if opcao == '1':
        linguagem = linguagem_somente_a
    elif opcao == '2':
        linguagem = linguagem_an_bn
    elif opcao == '3':
        linguagem = linguagem_ab_n
    else:
        print("Opção inválida.")
        return

    try:
        valor_p = int(input("Digite o valor de bombeamento p: "))
    except ValueError:
        print("Valor de p inválido. Digite um número inteiro.")
        return

    cadeia_w = input("Digite a cadeia w (use apenas 'a' e 'b') com comprimento ≥ p: ")

    if len(cadeia_w) < valor_p:
        print("A cadeia w é menor que p. O lema não se aplica.")
    else:
        resultado = testar_lema_bombeamento(linguagem, valor_p, cadeia_w)
        print("\nResultado final:")
        print(resultado)
        

# Executa o menu apenas se o arquivo for rodado diretamente1
if __name__ == "__main__":
    menu()
