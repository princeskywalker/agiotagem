from datetime import datetime, timedelta

class Cliente:
    def __init__(self, nome, valor, juros, data=None):
        """
        Cria um novo cliente.
        - Se `data` for None, usa a data atual.
        - Se `data` for fornecida, aceita como data retroativa.
        """
        self.nome = nome
        self.juros = juros  # Juros mensais em %
        if data:
            # Aceitar data retroativa
            self.data_vencimento = datetime.strptime(data, "%d/%m/%Y")
        else:
            # Usar a data atual
            self.data_vencimento = datetime.now()

        self.saldo_devedor = valor
        self.juros_no_mes = 0  # Juros ainda não aplicados

    def calcular_juros(self):
        """
        Aplica os juros ao saldo devedor no vencimento.
        """
        hoje = datetime.now()
        if hoje.date() >= self.data_vencimento.date():
            self.juros_no_mes = self.saldo_devedor * (self.juros / 100)
            self.saldo_devedor += self.juros_no_mes
            self.data_vencimento += timedelta(days=30)

    def registrar_pagamento(self, valor):
        """
        Registra o pagamento:
        - Subtrai o valor do saldo devedor.
        """
        self.saldo_devedor -= valor
        if self.saldo_devedor < 0:
            print(f"Pagamento excedente de R$ {abs(self.saldo_devedor):.2f}. Ajustando o saldo.")
            self.saldo_devedor = 0

        print(f"Pagamento de R$ {valor:.2f} registrado. Novo saldo devedor: R$ {self.saldo_devedor:.2f}.")

    def adicionar_emprestimo(self, valor):
        """
        Adiciona um novo valor ao saldo devedor existente.
        """
        self.saldo_devedor += valor
        print(f"Novo empréstimo de R$ {valor:.2f} adicionado. Saldo devedor atualizado: R$ {self.saldo_devedor:.2f}.")

    def exibir_dados(self):
        """Exibe os dados do cliente."""
        self.calcular_juros()

        if self.saldo_devedor > 0:
            return (
                f"Cliente: {self.nome}\n"
                f"Saldo devedor: R$ {self.saldo_devedor:.2f}\n"
                f"Próximo vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n"
                f"Juros do mês atual: R$ {self.juros_no_mes:.2f}\n"
            )
        else:
            return f"Cliente: {self.nome}\nDívida quitada!\n"
# https://www.pichau.com.br/monitor-gamer-pichau-nexus-wide-34-34-pol-va-ultrawide-curvo-2k-1ms-165hz-freesync-hdmi-dp-pg-nxsw34-bl01
#
# https://www.pichau.com.br/ssd-corsair-mp700-pro-2tb-m-2-2280-pcie-nvme-leitura-12400mb-s-gravacao-11800mb-s-cssd-f2000gbmp700phx