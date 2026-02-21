from clientes import Cliente

# Cadastro com data atual
cliente1 = Cliente(nome="João", valor=1000, juros=10)
print(cliente1.exibir_dados())

# Cadastro com data retroativa
cliente2 = Cliente(nome="Maria", valor=1500, juros=8, data="10/01/2025")
print("\nCliente com data retroativa:")
print(cliente2.exibir_dados())

# Registrar pagamento para o cliente retroativo
cliente2.registrar_pagamento(500)
print("\nApós pagamento de R$ 500:")
print(cliente2.exibir_dados())

