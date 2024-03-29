import requests

class Cep:

    def _solicita_cep(self) -> str:
        cep = str(input('Porfavor, digite o seu cep: '))
        return cep

    def _valida_cep(self, cep) -> bool:
        if not (len(cep) == 8):
            return False
        else:
            return True

    @staticmethod
    def busca_cep():
        cep_instancia = Cep()
        cep = cep_instancia._solicita_cep()
        
        if not cep_instancia._valida_cep(cep):
            return 'Cep inválido'
        
        url = f'https://viacep.com.br/ws/{cep}/json/'
        try:
            r = requests.get(url)
            if r.status_code == 200:
                return(r.json())
            else:
                return f'Erro na requisição'
        except Exception as e:
            return f'Erro na requisição: {e}'