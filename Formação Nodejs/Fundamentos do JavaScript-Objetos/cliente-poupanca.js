function Cliente(nome,cpf,email,saldo){
    this.nome = nome
    this.cpf = cpf
    this.email = email
    this.saldo = saldo
    this.depositar = function(valor){
        this.saldo+=valor
    }
}

function ClientePoupanca (nome,cpf,email,saldo,saldoPoup){
    Cliente.call(this,nome,cpf,email,saldo)
    this.saldoPoup =  saldoPoup

}

const murilo = new ClientePoupanca("Murilo","235464325645","user@user.com",1000,200)

console.log(murilo)

ClientePoupanca.prototype.depositarPoup = function(valor){
    this.saldoPoup +=valor
}

murilo.depositarPoup(123)
console.log(murilo.saldoPoup)
