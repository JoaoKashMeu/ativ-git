import json

arquivo_json = "agenda.json"

def carregar_contatos():
    try:
        with open(arquivo_json, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar os contatos. O arquivo pode estar corrompido.")
        return []

def salvar_contatos():
    try:
        with open(arquivo_json, "w") as arquivo:
            json.dump(agenda, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao salvar os contatos: {e}")

agenda = carregar_contatos()

def adicionar_contato(nome, telefone, favorito):
    try:
        contato = {"Nome": nome, "Telefone": telefone, "Favorito": favorito}
        agenda.append(contato)
        salvar_contatos()
        print(f"Contato '{nome}' adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar o contato: {e}")

def listar_contatos():
    try:
        print("\nLista de Contatos:")
        for contato in sorted(agenda, key=lambda x: x["Nome"]):
            print(contato)
    except Exception as e:
        print(f"Erro ao listar os contatos: {e}")

def buscar_contato(nome):
    try:
        for contato in agenda:
            if contato["Nome"].lower() == nome.lower():
                print(f"\nContato encontrado: {contato}")
                return contato
        print(f"\nNenhum contato encontrado com o nome '{nome}'.")
        return None
    except Exception as e:
        print(f"Erro ao buscar o contato: {e}")

def atualizar_contato(nome_antigo, nome_novo, telefone_novo, favorito_novo):
    try:
        contato = buscar_contato(nome_antigo)
        if contato:
            contato.update({"Nome": nome_novo, "Telefone": telefone_novo, "Favorito": favorito_novo})
            salvar_contatos()
            print(f"Contato '{nome_antigo}' atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar o contato: {e}")

def remover_contato(nome):
    try:
        contato = buscar_contato(nome)
        if contato:
            agenda.remove(contato)
            salvar_contatos()
            print(f"Contato '{nome}' removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover o contato: {e}")

def favoritar_desfavoritar_contato(nome):
    try:
        contato = buscar_contato(nome)
        if contato:
            contato["Favorito"] = not contato["Favorito"]
            salvar_contatos()
            status = "favoritado" if contato["Favorito"] else "desfavoritado"
            print(f"Contato '{nome}' foi {status} com sucesso.")
    except Exception as e:
        print(f"Erro ao alterar o status de favorito: {e}")

def listar_favoritos():
    try:
        print("\nLista de Contatos Favoritos:")
        favoritos = [c for c in agenda if c["Favorito"]]
        for contato in sorted(favoritos, key=lambda x: x["Nome"]):
            print(contato)
    except Exception as e:
        print(f"Erro ao listar os favoritos: {e}")

def menu():
    while True:
        try:
            print("\nAGENDA DE CONTATOS")
            print("1. Adicionar contato")
            print("2. Listar contatos")
            print("3. Buscar contato")
            print("4. Atualizar contato")
            print("5. Remover contato")
            print("6. Favoritar/Desfavoritar contato")
            print("7. Listar contatos favoritos")
            print("8. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                favorito = input("Favorito (True/False): ").lower() == "true"
                adicionar_contato(nome, telefone, favorito)
            elif opcao == "2":
                listar_contatos()
            elif opcao == "3":
                nome = input("Digite o nome do contato: ")
                buscar_contato(nome)
            elif opcao == "4":
                nome_antigo = input("Nome atual: ")
                nome_novo = input("Novo nome: ")
                telefone_novo = input("Novo telefone: ")
                favorito_novo = input("Favorito (True/False): ").lower() == "true"
                atualizar_contato(nome_antigo, nome_novo, telefone_novo, favorito_novo)
            elif opcao == "5":
                nome = input("Nome do contato a ser removido: ")
                remover_contato(nome)
            elif opcao == "6":
                nome = input("Nome do contato: ")
                favoritar_desfavoritar_contato(nome)
            elif opcao == "7":
                listar_favoritos()
            elif opcao == "8":
                print("Saindo do programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro inesperado no menu: {e}")

menu()
