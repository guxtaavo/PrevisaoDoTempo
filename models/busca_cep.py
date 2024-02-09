import requests

class Cep:

    def _valida_cep(cep):
        if not (len(cep) == 8):
            return False
        else:
            return True

    @staticmethod
    def busca_cep(cep):
        if not Cep._valida_cep(cep):
            return 'Cep inválido'
        
        url = f'https://viacep.com.br/ws/{cep}/json/'
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return r.json()
            else:
                return f'Erro na requisição'
        except Exception as e:
            return f'Erro na requisição: {e}'
        
        