from models.busca_cep import Cep
from models.weather import Clima
import os

class Menu:
    
    def _mostrar_mensagem_inicial(self) -> None:
        os.system('cls')
        print('----Olá, seja bem-vindx!!----')
        msg = 'ＢｉｔＴｅｍｐｏ'
        print(msg.center(20))

    def _valida_a_opcao(self, opcao):
        while True:
            if opcao in [1, 2]:
                if opcao == 1:
                    return True
                else:
                    os.system('cls')
                    print('Saindo...')
                    break
            else:
                opcao = int(input('Você digitou um número inválido, tente novamente: '))

    def _mostrar_opcoes(self):
        print('\n1. Prosseguir ')
        print('2. Sair ')
        try:
            opcao = int(input('Digite a opção escolhida: '))
            retorno = self._valida_a_opcao(opcao)
            if retorno:
                dados_cep = Cep.busca_cep()
                print(dados_cep.get('cep', 'Erro na requisição'))
                localidade = dados_cep['localidade']
                Clima.buscar_o_clima(localidade)
        except Exception as e:
            print(f'Erro: {e}.')

    @staticmethod
    def exibir_menu():
        menu = Menu()
        menu._mostrar_mensagem_inicial()
        menu._mostrar_opcoes()