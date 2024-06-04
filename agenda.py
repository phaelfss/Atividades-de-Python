class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
        
        
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("Contato já existe.")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado com sucesso.")
            
            
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado.")
            
            
    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print("Contato não encontrado.")
            
            
    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")
                
                
def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\n1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome do contato que deseja pesquisar: ")
            agenda.pesquisar_contato(nome)
        elif escolha == '4':
            agenda.listar_contatos()
        elif escolha == '5':
            print("Fechando agenda telefônica.")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()