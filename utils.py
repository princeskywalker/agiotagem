def projetar_saldo(cliente, meses):
    """
    Calcula o saldo devedor projetado após um número de meses, sem alterar o estado real.
    """
    saldo_projetado = cliente.saldo_devedor
    for _ in range(meses):
        juros = saldo_projetado * (cliente.juros / 100)
        saldo_projetado += juros
    return saldo_projetado
#html dinamico

