def loja_de_queijos(tipo, *argumentos, **argumentos_nomeados):
    print("-- Você tem algum", tipo, "?")
    print("-- Lamento, acabou o", tipo)
    for arg in argumentos:
        print(arg)
    print("-" * 40)
    for kw in argumentos_nomeados:
        print(kw, ":", argumentos_nomeados[kw])

loja_de_queijos("Limburger", "Está muito mole, senhor",
           "Está realmente muito, MUITO mole, senhor.",
           vendedor="Michael Palin",
           cliente="John Cleese",
           sketch="Sketch da Loja de Queijos")