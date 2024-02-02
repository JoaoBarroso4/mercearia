import Controller
import os.path
from Models import *


def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')


criarArquivos('DBs/categoria.txt', 'DBs/clientes.txt',
              'DBs/estoque.txt', 'DBs/fornecedores.txt',
              'DBs/funcionarios.txt', 'DBs/venda.txt')

if __name__ == '__main__':
    while True:
        local = int(input("Digite 1 para acessar Categorias\n"
                          "Digite 2 para acessar Estoque\n"
                          "Digite 3 para acessar Clientes\n"
                          "Digite 4 para acessar Fornecedores\n"
                          "Digite 5 para acessar Funcionários\n"
                          "Digite 6 para acessar Vendas\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"))

        if local == 1:
            contr = Controller.ControllerCategoria()
            while True:
                escolha = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para alterar uma categoria\n"
                                    "Digite 3 para excluir uma categoria\n"
                                    "Digite 4 para listar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))
                if escolha == 1:
                    categoria = input("Digite o nome da categoria que deseja cadastrar: ")
                    contr.inserir(categoria)
                elif escolha == 2:
                    categoriaAlterar = input("Digite o nome da categoria que deseja alterar: ")
                    categoriaNova = input("Digite o novo nome da categoria: ")
                    contr.alterar(categoriaAlterar, categoriaNova)
                elif escolha == 3:
                    categoria = input("Digite o nome da categoria que deseja excluir: ")
                    contr.remover(categoria)
                elif escolha == 4:
                    contr.listar()
                elif escolha == 5:
                    break

        elif local == 2:
            contr = Controller.ControllerEstoque()
            while True:
                escolha = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para alterar um produto\n"
                                    "Digite 3 para excluir um produto\n"
                                    "Digite 4 para listar os produtos cadastrados\n"
                                    "Digite 5 para sair\n"))
                if escolha == 1:
                    nome = input("Digite o nome do produto que deseja cadastrar: ")
                    valor = input("Digite o valor do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    quantidade = input("Digite a quantidade do produto: ")
                    contr.inserir(nome, valor, categoria, quantidade)
                elif escolha == 2:
                    nomeAlterar = input("Digite o nome do produto que deseja alterar: ")
                    nomeNovo = input("Digite o novo nome do produto: ")
                    valor = input("Digite o novo valor do produto: ")
                    categoria = input("Digite a nova categoria do produto: ")
                    quantidade = input("Digite a nova quantidade do produto: ")
                    contr.alterar(nomeAlterar, Produtos(nomeNovo, valor, categoria), quantidade)
                elif escolha == 3:
                    nome = input("Digite o nome do produto que deseja excluir: ")
                    contr.remover(nome)
                elif escolha == 4:
                    contr.listar()
                elif escolha == 5:
                    break

        elif local == 3:
            contr = Controller.ControllerCliente()
            while True:
                escolha = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para alterar um cliente\n"
                                    "Digite 3 para excluir um cliente\n"
                                    "Digite 4 para listar os clientes cadastrados\n"
                                    "Digite 5 para sair\n"))
                if escolha == 1:
                    nome = input("Digite o nome do cliente que deseja cadastrar: ")
                    cpf = input("Digite o CPF do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    endereco = input("Digite o endereço do cliente: ")
                    email = input("Digite o email do cliente: ")
                    contr.inserir(nome, cpf, telefone, endereco, email)
                elif escolha == 2:
                    clienteAlterar = input("Digite o CPF do cliente que deseja alterar: ")
                    nome = input("Digite o novo nome do cliente: ")
                    telefone = input("Digite o novo telefone do cliente: ")
                    cpf = input("Digite o novo CPF do cliente: ")
                    endereco = input("Digite o novo endereço do cliente: ")
                    email = input("Digite o novo email do cliente: ")
                    contr.alterar(clienteAlterar, nome, cpf, telefone, endereco, email)
                elif escolha == 3:
                    cpf = input("Digite o CPF do cliente que deseja excluir: ")
                    contr.remover(cpf)
                elif escolha == 4:
                    contr.listar()
                elif escolha == 5:
                    break

        elif local == 4:
            contr = Controller.ControllerFornecedor()
            while True:
                escolha = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para alterar um fornecedor\n"
                                    "Digite 3 para excluir um fornecedor\n"
                                    "Digite 4 para listar os fornecedores cadastrados\n"
                                    "Digite 5 para sair\n"))
                if escolha == 1:
                    nome = input("Digite o nome do fornecedor que deseja cadastrar: ")
                    cnpj = input("Digite o CNPJ do fornecedor: ")
                    telefone = input("Digite o telefone do fornecedor: ")
                    categoria = input("Digite a categoria dos produtos do fornecedor: ")
                    contr.inserir(nome, cnpj, telefone, categoria)
                elif escolha == 2:
                    fornecedorAlterar = input("Digite o CNPJ do fornecedor que deseja alterar: ")
                    nome = input("Digite o novo nome do fornecedor: ")
                    telefone = input("Digite o novo telefone do fornecedor: ")
                    categoria = input("Digite a nova categoria dos produtos do fornecedor: ")
                    cnpj = input("Digite o novo CNPJ do fornecedor: ")
                    contr.alterar(fornecedorAlterar, nome, telefone, categoria, cnpj)
                elif escolha == 3:
                    cnpj = input("Digite o CNPJ do fornecedor que deseja excluir: ")
                    contr.remover(cnpj)
                elif escolha == 4:
                    contr.listar()
                elif escolha == 5:
                    break

        elif local == 5:
            contr = Controller.ControllerFuncionario()
            while True:
                escolha = int(input("Digite 1 para cadastrar um funcionário\n"
                                    "Digite 2 para alterar um funcionário\n"
                                    "Digite 3 para excluir um funcionário\n"
                                    "Digite 4 para listar os funcionários cadastrados\n"
                                    "Digite 5 para sair\n"))
                if escolha == 1:
                    clt = input("Digite o número da carteira de trabalho do funcionário: ")
                    nome = input("Digite o nome do funcionário que deseja cadastrar: ")
                    cpf = input("Digite o CPF do funcionário: ")
                    telefone = input("Digite o telefone do funcionário: ")
                    endereco = input("Digite o endereço do funcionário: ")
                    email = input("Digite o email do funcionário: ")
                    contr.inserir(clt, nome, cpf, telefone, endereco, email)
                elif escolha == 2:
                    funcionarioAlterar = input("Digite o CPF do funcionário que deseja alterar: ")
                    clt = input("Digite o novo número da carteira de trabalho do funcionário: ")
                    nome = input("Digite o novo nome do funcionário: ")
                    telefone = input("Digite o novo telefone do funcionário: ")
                    cpf = input("Digite o novo CPF do funcionário: ")
                    endereco = input("Digite o novo endereço do funcionário: ")
                    email = input("Digite o novo email do funcionário: ")
                    contr.alterar(funcionarioAlterar, clt, nome, telefone, cpf, endereco, email)
                elif escolha == 3:
                    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
                    contr.remover(cpf)
                elif escolha == 4:
                    contr.listar()
                elif escolha == 5:
                    break

        elif local == 6:
            contr = Controller.ControllerVenda()
            while True:
                escolha = int(input("Digite 1 para cadastrar uma venda\n"
                                    "Digite 2 para pesquisar pelas vendas de um determinado período\n"
                                    "Digite 3 para sair\n"))
                if escolha == 1:
                    produto = input("Digite o nome do produto que foi vendido: ")
                    comprador = input("Digite o nome do cliente que realizou a compra: ")
                    vendedor = input("Digite o nome do funcionário que realizou a venda: ")
                    quantidade = input("Digite a quantidade do produto que foi vendido: ")
                    contr.inserir(produto, comprador, vendedor, quantidade)
                elif escolha == 2:
                    dataInicio = input("Digite a data de início do período que deseja pesquisar: ")
                    dataFim = input("Digite a data de fim do período que deseja pesquisar: ")
                    contr.pesquisar(dataInicio, dataFim)
                elif escolha == 3:
                    break

        elif local == 7:
            contr = Controller.ControllerVenda()
            contr.listar()

        elif local == 8:
            break