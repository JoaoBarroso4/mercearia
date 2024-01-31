from Models import *
from DAO import *
from datetime import datetime


class ControllerCategoria:
    def inserir(self, categoriaAdc):
        existe = False

        categorias = DaoCategoria.ler()
        for categoria in categorias:
            if categoria.categoria == categoriaAdc:
                existe = True
                break

        if not existe:
            DaoCategoria.salvar(categoriaAdc)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria já cadastrada.')

    def listar(self):
        categorias = DaoCategoria.ler()
        if len(categorias) > 0:
            print('Categorias cadastradas: ' + ', '.join([categoria.categoria for categoria in categorias]))
        else:
            print('Não há categorias cadastradas.')

    def remover(self, categoriaRemover):
        categorias = DaoCategoria.ler()

        existe = len(list(filter(lambda x: x.categoria == categoriaRemover, categorias))) > 0

        if existe:
            for i in range(len(categorias)):
                if categorias[i].categoria == categoriaRemover:
                    categorias.pop(i)
                    break
            print('Categoria removida com sucesso!')
        else:
            print('A categoria não existe.')

        with open('categoria.txt', 'w') as arq:
            for categoria in categorias:
                arq.write(categoria.categoria + '\n')

    def alterar(self, categoriaAlterar, categoriaNova):
        categorias = DaoCategoria.ler()

        existe = len(list(filter(lambda x: x.categoria == categoriaAlterar, categorias))) > 0

        if existe:
            for i in range(len(categorias)):
                # verifica se a categoria nova não é igual a uma existente usando array e filter
                if len(list(filter(lambda x: x.categoria == categoriaNova, categorias))) == 0:
                    # aplica a atualizacao usando map
                    categorias = list(map(lambda x: x.categoria if (x.categoria != categoriaAlterar) else categoriaNova,
                                          categorias))
                else:
                    print('A categoria já existe.')
                break
            print('Categoria alterada com sucesso!')
        else:
            print('A categoria não existe.')

        with open('categoria.txt', 'w') as arq:
            for categoria in categorias:
                arq.write(Categoria(categoria).categoria + '\n')


class ControllerEstoque:
    def inserir(self, nome, preco, categoria, qtd):
        produtos = DaoEstoque.ler()
        categorias = DaoCategoria.ler()

        # verifica se a categoria existe
        existeCat = len(list(filter(lambda x: x.categoria == categoria, categorias))) > 0

        # verifica se o produto existe
        existeProd = len(list(filter(lambda x: x.produto.nome == nome, produtos))) > 0

        if existeCat:
            if not existeProd:
                produto = Produtos(nome, preco, categoria)
                estoque = Estoque(produto, qtd)
                DaoEstoque.salvar(estoque)
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto já cadastrado.')
        else:
            print('Categoria inexistente.')

    def listar(self):
        estoque = DaoEstoque.ler()
        if len(estoque) > 0:
            print('==== Produtos em estoque ==== \n' + '\n'.join([f"Produto: {estoque[i].produto.nome} - "
                                                                  f"Categoria: {estoque[i].produto.categoria} -"
                                                                  f" Preço: R${estoque[i].produto.preco} -"
                                                                  f" Quantidade: ${estoque[i].qtd} un."
                                                                  for i in range(len(estoque))]))
        else:
            print('Não há produtos em estoque.')

    def remover(self, produto: Produtos):
        estoque = DaoEstoque.ler()

        # verifica se o produto existe
        existeProd = len(list(filter(lambda x: x.produto.nome == produto, estoque))) > 0

        if existeProd:
            for i in range(len(estoque)):
                if estoque[i].produto.nome == produto:
                    estoque.pop(i)
                    break
            print('Produto removido com sucesso!')
        else:
            print('Produto não cadastrado.')

        with open('estoque.txt', 'w') as arq:
            for etq in estoque:
                arq.write('|'.join([etq.produto.nome, str(etq.produto.preco), etq.produto.categoria,
                                    str(etq.qtd)]) + '\n')

    def alterar(self, produtoAlt: Produtos, produtoNovo: Produtos, qtd):
        produtos = DaoEstoque.ler()
        categorias = DaoCategoria.ler()

        # verifica se o produto existe
        existeProdAlt = len(list(filter(lambda x: x.produto.nome == produtoAlt.nome, produtos))) > 0

        if existeProdAlt:
            for i in range(len(produtos)):
                if produtos[i].produto.nome == produtoAlt.nome:

                    # verifica se a nova categoria existe
                    existeCat = len(list(filter(lambda x: x.categoria == produtoNovo.categoria, categorias))) > 0

                    if existeCat:
                        produtos[i].produto = produtoNovo
                        produtos[i].qtd = qtd
                        print('Produto alterado com sucesso!')
                        break
                    else:
                        print('Categoria inexistente.')
                        break
        else:
            print('Produto não cadastrado.')

        with open('estoque.txt', 'w') as arq:
            for etq in produtos:
                arq.write('|'.join([etq.produto.nome, str(etq.produto.preco), etq.produto.categoria,
                                    str(etq.qtd)]) + '\n')


class ControllerVenda:
    def inserir(self, produto, vendedor, comprador, qtdVendida):
        produtos = DaoEstoque.ler()
        valorCompra = 0

        # verifica se o produto existe
        existeProd = len(list(filter(lambda x: x.produto.nome == produto, produtos))) > 0

        if existeProd:
            for i in range(len(produtos)):
                if produtos[i].produto.nome == produto:
                    # verifica se a quantidade em estoque é suficiente
                    if produtos[i].qtd >= int(qtdVendida):
                        produtos[i].qtd -= int(qtdVendida)

                        venda = Venda(produtos[i].produto, vendedor, comprador, qtdVendida,
                                      datetime.now().strftime("%d/%m/%Y"))
                        DaoVenda.salvar(venda)

                        valorCompra = int(produtos[i].produto.preco) * int(qtdVendida)

                        print('Venda realizada com sucesso!')
                        break
                    else:
                        print('Quantidade em estoque insuficiente.')
                        break
        else:
            print('Produto não cadastrado.')

        with open('estoque.txt', 'w') as arq:
            for prd in produtos:
                arq.write('|'.join([prd.produto.nome, str(prd.produto.preco), prd.produto.categoria,
                                    str(prd.qtd)]) + '\n')
        return valorCompra

    def listar(self):
        vendas = DaoVenda.ler()
        produtos = []

        for venda in vendas:
            produto = venda.itensVendidos.nome
            qtdVend = venda.qtdVendida

            # verifica se há vendas do produto
            existeProdVend = len(list(filter(lambda x: x['produto'] == produto, produtos))) > 0

            if existeProdVend:
                produtos = list(map(lambda x: {'produto': produto, 'qtd': x['qtd'] + qtdVend} if (
                        x['produto'] == produto) else x, produtos))
            else:
                produtos.append({'produto': produto, 'qtd': qtdVend})

        ordenado = sorted(produtos, key=lambda x: x['qtd'], reverse=True)

        print("==== Produtos mais vendidos ====")
        for i in range(len(ordenado)):
            print(f"Produto: {ordenado[i]['produto']} - Quantidade: {ordenado[i]['qtd']} un.")
