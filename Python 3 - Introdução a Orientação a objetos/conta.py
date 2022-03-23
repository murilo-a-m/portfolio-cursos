
#Define a classe conta (bancária)
class Conta:
    def __init__(self, numero, titular, saldo, limite): #Construtor da classe conta
        print("Construindo Conta...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self): #Método para retornar o extrato de uma conta
        print('Saldo de {} do titular {}.'.format(self.__saldo, self.__titular))

    def depositar(self,valor): #Método para depositar na conta
        self.__saldo += valor

    def sacar(self,valor): #Método para sacar da conta
        if(self.__pode_sacar()):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, valor, destino): #Método para tranferencia de valores entre duas contas
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self): #Método para consultar o saldo da conta
        return self.__saldo

    @property
    def titular(self): #Método para consultar o titular da conta
        return self.__titular

    @property
    def limite(self): #Método para consultar o limite da conta
        return self.__limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    @limite.setter
    def limite(self, limite): #Método para configurar um novo limite para a conta
        self.__limite = limite

    def __pode_sacar(self,valor): #Método que retorna se é possivel realizar o saque
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel


