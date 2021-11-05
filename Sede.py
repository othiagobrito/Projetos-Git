agua = 100
tempo = 0
garrafa = 20
carteira = 100
comprar_agua = 2.5
compras = 0

while True:

    log = f"Tempo: {tempo}s - Nível de água: {agua} - Saldo: R${carteira:.2f}"
    print(log)

    tempo += 1
    agua -= 1

    if agua <= 50 and garrafa > 0:
        print("Fulano está com sede")
        garrafa -= 5
        agua += 5
        print(f"Fulano tomou água e recuperou seu nível de água (nível: {agua})")
    elif agua <= 50 and garrafa < 1:
        print("Fulano está com sede, mas não tem água para beber.")
    
    if agua == 0:
        final_log = f"Fulano sobreviveu por {tempo/2:.0f} minutos."
        print(f"\nFulano morreu de sede.\n{final_log}")
        break
    
    if garrafa == 0 and carteira >= comprar_agua:
        carteira = carteira - comprar_agua
        compras += 1
        garrafa += 20
        print(f"Fulano comprou água por R${comprar_agua} e seu saldo agora é de R${carteira:.2f}")
    else:
        print(f"Fulano não tem dinheiro para comprar água.")
