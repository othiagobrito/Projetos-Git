import random

def atacar():
    efetividade = random.randint(1, 100)
    dano_base = 20
    dano = dano_base * (efetividade/100)

    return efetividade, dano

def defender():
    efetividade = random.randint(1, 100)
    defesa_base = 15
    defesa = defesa_base * (efetividade/100)

    return efetividade, defesa

movimentos = ["atacar", "defender"]
turno = 1

players = {"Lutador A": 100, "Lutador B": 100}

while True:

    txt_turno = f"Turno {turno}"
    separador = "="
    
    if players["Lutador A"] <= 0 or players["Lutador B"] <= 0:
        print("\nLuta encerrada!\n")
        print("Relatório Final:")

        vida_A = players["Lutador A"]
        vida_B = players["Lutador B"]

        print(f"Vida do Lutador A: {vida_A:.2f}")
        print(f"Vida do Lutador B: {vida_B:.2f}")

        if vida_A > 0 and vida_B <= 0:
            print(f"\nLutador A é o vencedor!")
        elif vida_B > 0 and vida_A <= 0:
            print(f"\nLutador B é o vencedor!")
        elif vida_A <= 0 and vida_B <= 0:
            print(f"\nEmpate!")
        break
    else:
        vida_A = players["Lutador A"]
        vida_B = players["Lutador B"]

        print(f"Vida do Lutador A: {vida_A:.2f}")
        print(f"Vida do Lutador B: {vida_B:.2f}")

    print(f"\n{separador*len(txt_turno)}\n{txt_turno}\n{separador*len(txt_turno)}")

    lutador_a = random.choice(movimentos)
    if lutador_a == "atacar":
        movimento_a = atacar().__getitem__(1)
        efetividade_a = atacar().__getitem__(0)
        txt_A = f"{movimento_a:.2f} de dano causado, a efetividade do ataque é de {efetividade_a:.2f}%"
    else:
        movimento_a = defender().__getitem__(1)
        efetividade_a = defender().__getitem__(0)
        txt_A = f"{movimento_a:.2f} de defesa, a efetividade da defesa é de {efetividade_a:.2f}%"

    lutador_b = random.choice(movimentos)
    if lutador_b == "atacar":
        movimento_b = atacar().__getitem__(1)
        efetividade_b = atacar().__getitem__(0)
        txt_B = f"{movimento_b:.2f} de dano causado, a efetividade do ataque é de {efetividade_b:.2f}%"
    else:
        movimento_b = defender().__getitem__(1)
        efetividade_b = defender().__getitem__(0)
        txt_B = f"{movimento_b:.2f} de defesa, a efetividade da defesa é de {efetividade_b:.2f}%"
    
    if lutador_a == "atacar" and lutador_b == "atacar":
        print(f"Lutador A ataca: {txt_A}")
        players["Lutador A"] -= movimento_b
        print(f"Lutador B ataca: {txt_B}\n")
        players["Lutador B"] -= movimento_a

    elif lutador_a == "atacar" and lutador_b == "defender":
        print(f"Lutador A ataca: {txt_A}")
        dmg = movimento_a - movimento_b
        players["Lutador B"] -= dmg
        print(f"Lutador B defende: {txt_B}")
        print(f"Dano sofrido: {dmg:.2f}\n")

    elif lutador_a == "defender" and lutador_b == "atacar":
        print(f"Lutador B ataca: {txt_B}")
        dmg = movimento_b - movimento_a
        players["Lutador A"] -= dmg
        print(f"Lutador A defende: {txt_A}")
        print(f"Dano sofrido: {dmg:.2f}\n")

    else:
        print(f"Lutador A defende: {txt_A}")
        print(f"Lutador B defende: {txt_B}\n")
    
    turno += 1
