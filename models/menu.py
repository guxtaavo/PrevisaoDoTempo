from models.busca_cep import Cep
import os

class Menu:
    
    def _mostrar_mensagem_inicial():
        os.system('cls')
        print('----Olá, seja bem-vindx!!----')
        msg = 'ＢｉｔＴｅｍｐｏ'
        msg = msg.center(20)
        print(msg)

    def _valida_a_opcao(opcao):
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

    def _mostrar_opcoes():
        print('\n1. Prosseguir ')
        print('2. Sair ')
        try:
            opcao = int(input('Digite a opção escolhida: '))
            retorno = Menu._valida_a_opcao(opcao)
            if retorno:
                cep = Cep.busca_cep()
                print(cep.get('cep', 'Erro na requisição'))
        except Exception as e:
            print(f'Erro: {e}.')

    @staticmethod
    def exibir_menu():
        Menu._mostrar_mensagem_inicial()
        Menu._mostrar_opcoes()