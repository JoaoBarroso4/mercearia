from datetime import datetime


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Estoque:
    def __init__(self, produto: Produtos, qtd):
        self.produto = produto
        self.qtd = qtd


class Venda:
    def __init__(self, itensVendidos: Produtos, vendedor, comprador, qtdVendida, data=datetime.now().strftime("%d/%m/%Y")):
        self.data = data
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.qtdVendida = qtdVendida


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria


class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email


class Funcionario(Pessoa):
    def __init__(self, clt, nome, cpf, telefone, endereco, email):
        super(Funcionario, self).__init__(nome, cpf, telefone, endereco, email)
        self.clt = clt
