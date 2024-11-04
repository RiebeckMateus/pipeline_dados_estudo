from processamento_dados import Dados

path_csv = 'data_raw/dados_empresaB.csv'
path_json = 'data_raw/dados_empresaA.json' 

# Extract

dados_empresa_a = Dados.leitura_dados(path_json, 'json')
print(dados_empresa_a.colunas)
print(dados_empresa_a.qtd_linhas)

dados_empresa_b = Dados.leitura_dados(path_csv, 'csv')
print(dados_empresa_b.colunas)
print(dados_empresa_b.qtd_linhas)

# Transform

key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresa_b.rename_columns(key_mapping)
print(dados_empresa_b.colunas)

dados_fusao = Dados.join(dados_empresa_a, dados_empresa_b)
print(dados_fusao.colunas)
print(dados_fusao.qtd_linhas)

# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'

dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)