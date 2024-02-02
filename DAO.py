from Models import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('BDs/categoria.txt', 'a') as arq:
            arq.writelines(categoria + '\n')

    @classmethod
    def ler(cls):
        with open('BDs/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        return [Categoria(c) for c in cls.categoria]


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        venda_info = '|'.join([
            venda.itensVendidos.nome,
            venda.itensVendidos.preco,
            venda.itensVendidos.categoria,
            venda.vendedor,
            venda.comprador,
            venda.qtdVendida,
            venda.data
        ])

        with open('BDs/venda.txt', 'a') as arq:
            arq.write(venda_info + '\n')

    @classmethod
    def ler(cls):
        with open('BDs/venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

            cls.venda = list(map(lambda x: x.replace('\n', '').split('|'), cls.venda))

        return [Venda(Produtos(v[0], v[1], v[2]), v[3], v[4], int(v[5]), v[6]) for v in cls.venda]


# simular venda
# a = Venda(Produtos('Coca', '5', 'Bebidas'), 'Joao', 'Maria', '2')
# DaoVenda.salvar(v)
# b = DaoVenda.ler()
# for i in b:
#     print(i.itensVendidos.nome)

class DaoProdutos:
    @classmethod
    def salvar(cls, produto: Produtos):
        produto_info = '|'.join([
            produto.nome,
            produto.preco,
            produto.categoria
        ])

        with open('produtos.txt', 'a') as arq:
            arq.write(produto_info + '\n')

    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            cls.produto = arq.readlines()

            cls.produto = list(map(lambda x: x.replace('\n', '').split('|'), cls.produto))

        return [Produtos(p[0], p[1], p[2]) for p in cls.produto]


class DaoEstoque:
    @classmethod
    def salvar(cls, estoque: Estoque):
        estoque_info = '|'.join([
            estoque.produto.nome,
            estoque.produto.preco,
            estoque.produto.categoria,
            estoque.qtd
        ])

        with open('BDs/estoque.txt', 'a') as arq:
            arq.write(estoque_info + '\n')

    @classmethod
    def ler(cls):
        with open('BDs/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

            cls.estoque = list(map(lambda x: x.replace('\n', '').split('|'), cls.estoque))

        return [Estoque(Produtos(e[0], e[1], e[2]), int(e[3])) for e in cls.estoque]


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        fornecedor_info = '|'.join([
            fornecedor.nome,
            fornecedor.cnpj,
            fornecedor.telefone,
            fornecedor.categoria
        ])

        with open('BDs/fornecedores.txt', 'a') as arq:
            arq.write(fornecedor_info + '\n')

    @classmethod
    def ler(cls):
        with open('BDs/fornecedores.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

            cls.fornecedor = list(map(lambda x: x.replace('\n', '').split('|'), cls.fornecedor))

        return [Fornecedor(f[0], f[1], f[2], f[3]) for f in cls.fornecedor]


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        pessoa_info = '|'.join([
            pessoa.nome,
            pessoa.cpf,
            pessoa.telefone,
            pessoa.endereco,
            pessoa.email
        ])

        with open('BDs/clientes.txt', 'a') as arq:
            arq.write(pessoa_info + '\n')

    @classmethod
    def ler(cls):
        with open('BDs/clientes.txt', 'r') as arq:
            cls.pessoa = arq.readlines()

            cls.pessoa = list(map(lambda x: x.replace('\n', '').split('|'), cls.pessoa))

        return [Pessoa(p[0], p[1], p[2], p[3], p[4]) for p in cls.pessoa]


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        funcionario_info = '|'.join([
            funcionario.clt,
            funcionario.nome,
            funcionario.cpf,
            funcionario.telefone,
            funcionario.endereco,
            funcionario.email
        ])

        with open('BDs/funcionarios.txt', 'a') as arq:
            arq.write(funcionario_info + '\n')

    @classmethod
    def ler(cls):
        with open('BDs/funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

            cls.funcionario = list(map(lambda x: x.replace('\n', '').split('|'), cls.funcionario))

        return [Funcionario(f[0], f[1], f[2], f[3], f[4], f[5]) for f in cls.funcionario]