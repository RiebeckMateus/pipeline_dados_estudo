import json, csv

class Dados:
    def __init__(self, dados):
        self.dados = dados
        self.colunas = self._get_columns()
        self.qtd_linhas = self._size_data()
    
    def __str__(self) -> str:
        return f'Path: {self.path}\nTipo dado: {self._tipo_dados}'
    
    def _leitura_json(path):
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def _leitura_csv(path):
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        dados = []
        if tipo_dados == 'csv':
            dados = cls._leitura_csv(path)
        elif tipo_dados == 'json':
            dados = cls._leitura_json(path)
        
        return cls(dados)
     
    def _get_columns(self):
        return list(self.dados[-1].keys())

    def rename_columns(self, key_mapping):
        new_dados = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados]
        self.dados = new_dados
        self.colunas = self._get_columns()
        
    def _size_data(self):
        return len(self.dados)

    def join(dados_a, dados_b):
        combined_list = []
        combined_list.extend(dados_a.dados)
        combined_list.extend(dados_b.dados)
        
        return Dados(combined_list)

    def _transformando_dados_tabela(self):
        dados_combinados_tabela =  [self.colunas] + [[row.get(coluna, 'Indisponivel') for coluna in self.colunas] for row in self.dados]
        
        return dados_combinados_tabela

    def salvando_dados(self, path):
        
        dados_combinados_tabela = self._transformando_dados_tabela()
        
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
