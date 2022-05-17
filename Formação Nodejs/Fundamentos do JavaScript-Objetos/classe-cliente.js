class Cliente{
    constructor(nome,email,cpf,saldo){
        this.nome = nome
        this.email=email
        this.cpf = cpf
        this.saldo=saldo
    }

    depositar(valor) {
        this.saldo+=valor
    }

    exibirSaldo(){
        console.log(this.saldo)
    }
}

class ClientePoupanca extends Cliente{
    constructor(nome,email,cpf,saldo,saldoPoup){
        super(nome,email,cpf,saldo)
        this.saldoPoup = saldoPoup
    }

    depositarPoup(valor){
        this.saldoPoup += valor
    }

    exibirSaldoPoup(){
        console.log(this.saldoPoup)
    }
}


const murilo = new ClientePoupanca("Murilo","user@user.com","2345345",123,321)

murilo.depositar(1)
murilo.depositarPoup(1)
murilo.exibirSaldo()
murilo.exibirSaldoPoup()