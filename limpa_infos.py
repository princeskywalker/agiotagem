# Abra o arquivo original para leitura
with open('com_valor', 'r') as f:
    # Crie uma lista para armazenar as linhas processadas
    linhas_processadas = []

    # Para cada linha no arquivo
    for linha in f:
        # Encontre o índice do " - " e corte até essa posição
        nova_linha = linha.split(" - ")[0]
        # Adicione a linha processada à lista
        linhas_processadas.append(nova_linha)

# Abra um novo arquivo para escrever as linhas limpas
with open('arquivo_limpo.txt', 'w') as f:
    for linha in linhas_processadas:
        # Escreva cada linha no novo arquivo
        f.write(linha + '\n')

print("Arquivo limpo gerado com sucesso!")
