from banco import cursor, conexao

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    cursor.execute(
        "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
        (nome, quantidade, preco)
    )

    conexao.commit()

    print("Produto cadastrado com sucesso!")


def listar_produtos():
    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(produto)


def atualizar_estoque():
    id_produto = int(input("Digite o ID do produto: "))
    nova_quantidade = int(input("Digite a nova quantidade: "))

    cursor.execute(
        "UPDATE produtos SET quantidade = ? WHERE id = ?",
        (nova_quantidade, id_produto)
    )

    conexao.commit()

    print("Estoque atualizado com sucesso!")


while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        atualizar_estoque()

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")