# ----------------------------------------------
# Teste do Lema do Bombeamento para Linguagens Formais
# Autor: [Seu Nome Aqui]
# Linguagem: Python
# ----------------------------------------------

def testar_lema_bombeamento(linguagem, p, w, max_divisoes_exibidas=3):
    n = len(w)
    if n < p:
        return "❗ A cadeia w é menor que o valor de bombeamento p. O lema não se aplica."

    violacoes = []
    divisoes_exibidas = 0
    resultado_final = []

    for i in range(p + 1):
        for j in range(1, p - i + 1):
            if divisoes_exibidas >= max_divisoes_exibidas:
                continue  # Ainda testa, mas não imprime mais divisões

            x = w[:i]
            y = w[i:i + j]
            z = w[i + j:]

            divisao_resultado = [f"\nDivisão: x='{x}', y='{y}', z='{z}'"]
            violacao_ocorreu = False

            for repeticoes in range(5):  # i = 0 a 4
                nova_cadeia = x + (y * repeticoes) + z
                pertence = linguagem(nova_cadeia)
                status = "PERTENCE" if pertence else "NÃO pertence"
                divisao_resultado.append(f"  i = {repeticoes} → '{nova_cadeia}' → {status} à linguagem.")

                if not pertence and not violacao_ocorreu:
                    violacao_ocorreu = True
                    violacoes.append({
                        "x": x, "y": y, "z": z,
                        "i": repeticoes,
                        "cadeia": nova_cadeia
                    })

            resultado_final.extend(divisao_resultado)
            divisoes_exibidas += 1

    if violacoes:
        resultado_final.append("\n🛑 Conclusão: A linguagem testada **NÃO é regular**, pois houve violação do Lema do Bombeamento.")
        for v in violacoes:
            resultado_final.append(
                f"\n⚠️ Violação: x='{v['x']}', y='{v['y']}', z='{v['z']}'\n"
                f"   Com i = {v['i']}, gerou '{v['cadeia']}' que NÃO pertence à linguagem."
            )
    else:
        resultado_final.append("\n✅ Nenhuma violação foi encontrada. O lema do bombeamento **não foi violado** com essa cadeia.")
        resultado_final.append("⚠️ Isso **não prova** que a linguagem é regular — apenas que essa cadeia específica não violou o lema.")

    return "\n".join(resultado_final)


# -----------------------------
# Definição da linguagem L = { aⁿbⁿ | n ≥ 1 }
# -----------------------------
def linguagem_an_bn(s):
    n_a = 0
    n_b = 0
    estado = 0
    for char in s:
        if estado == 0:
            if char == 'a':
                n_a += 1
            elif char == 'b':
                if n_a == 0:
                    return False
                estado = 1
                n_b += 1
            else:
                return False
        elif estado == 1:
            if char == 'b':
                n_b += 1
            elif char == 'a':
                return False
            else:
                return False
    return n_a == n_b and n_a > 0

def linguagem_so_a(s):
    return all(char == 'a' for char in s)


# Teste com cadeia que violará
p = 3
w = "aaaaaa"
resultado = testar_lema_bombeamento(linguagem_so_a, p, w)
print(resultado)
print('nota 10')