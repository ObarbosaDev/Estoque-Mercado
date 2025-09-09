# Cada produto será armazenado como uma tupla:
# (codigo, nome, quantidade, preco)

estoque = []

def cadastrar_produto(codigo, nome, quantidade, preco):
    # Verifica se o código já existe
    for prod in estoque:
        if prod[0] == codigo:
            print(f"Produto com código {codigo} já cadastrado.")
            return
    produto = (codigo, nome, quantidade, preco)
    estoque.append(produto)
    print(f"Produto {nome} cadastrado com sucesso.")

def listar_produtos():
    if not estoque:
        print("Estoque vazio.")
        return
    print("Código | Nome               | Quantidade | Preço")
    print("-----------------------------------------------")
    for prod in estoque:
        print(f"{prod[0]:6} | {prod[1]:18} | {prod[2]:9} | R$ {prod[3]:.2f}")

def buscar_produto(codigo):
    for prod in estoque:
        if prod[0] == codigo:
            return prod
    return None

def atualizar_estoque(codigo, quantidade):
    # Atualiza a quantidade do produto
    for i, prod in enumerate(estoque):
        if prod[0] == codigo:
            nova_quantidade = prod[2] + quantidade
            if nova_quantidade < 0:
                print("Erro: quantidade insuficiente no estoque.")
                return
            # Atualiza a tupla (tuplas são imutáveis, então cria uma nova)
            estoque[i] = (prod[0], prod[1], nova_quantidade, prod[3])
            print(f"Estoque atualizado. Novo saldo: {nova_quantidade}")
            return
    print("Produto não encontrado.")

def remover_produto(codigo):
    for i, prod in enumerate(estoque):
        if prod[0] == codigo:
            estoque.pop(i)
            print(f"Produto {prod[1]} removido do estoque.")
            return
    print("Produto não encontrado.")

def resumo_estoque():
    total_itens = sum(prod[2] for prod in estoque)
    valor_total = sum(prod[2] * prod[3] for prod in estoque)
    print(f"Total de itens no estoque: {total_itens}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

def menu():
    while True:
        print("\n--- Sistema de Estoque do Mercado ---")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar estoque")
        print("5 - Remover produto")
        print("6 - Resumo do estoque")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                codigo = int(input("Código do produto: "))
                nome = input("Nome do produto: ")
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço unitário: "))
                cadastrar_produto(codigo, nome, quantidade, preco)
            except ValueError:
                print("Entrada inválida. Tente novamente.")
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            try:
                codigo = int(input("Código do produto para buscar: "))
                prod = buscar_produto(codigo)
                if prod:
                    print(f"Produto encontrado: Código: {prod[0]}, Nome: {prod[1]}, Quantidade: {prod[2]}, Preço: R$ {prod[3]:.2f}")
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Código inválido.")
        elif opcao == '4':
            try:
                codigo = int(input("Código do produto para atualizar: "))
                quantidade = int(input("Quantidade (use negativo para saída): "))
                atualizar_estoque(codigo, quantidade)
            except ValueError:
                print("Entrada inválida.")
        elif opcao == '5':
            try:
                codigo = int(input("Código do produto para remover: "))
                remover_produto(codigo)
            except ValueError:
                print("Código inválido.")
        elif opcao == '6':
            resumo_estoque()
        elif opcao == '0':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
