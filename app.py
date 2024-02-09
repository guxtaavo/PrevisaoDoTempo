from models.busca_cep import Cep

def main():
    cep = str(input('Digite seu cep: '))
    resolve = Cep.busca_cep(cep)
    print(resolve)

if __name__ == '__main__':
    main()