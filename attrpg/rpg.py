#Classe Pessoa:

class Pessoa:
    """
    Classe base para representar uma pessoa no sistema, seja um mestre ou um personagem.
    """
    def __init__(self, nome, senha):
        self._nome = nome
        self._senha = senha

    def get_nome(self):
        """Retorna o nome da pessoa."""
        return self._nome

    def get_senha(self):
        """Retorna a senha da pessoa."""
        return self._senha

    def autenticar(self, senha):
        """Autentica a pessoa comparando a senha fornecida com a senha armazenada."""
        return self._senha == senha

#Classe Mestre:

class Mestre(Pessoa):
    """
    Classe para representar um mestre no sistema.
    Herda da classe Pessoa e fornece funcionalidades adicionais.
    """
    def __init__(self, nome, senha):
        super().__init__(nome, senha)

    def mostrar_pagina_mestre(self):
        """Mostra a página de administração do mestre."""
        return "Bem-vindo à página do Mestre! Aqui você pode gerenciar o jogo quando quiser."

#Classe Personagem:

class Personagem(Pessoa):
    """
    Classe base para representar um personagem no sistema.
    Herda da classe Pessoa e adiciona características adicionais.
    """
    def __init__(self, nome, senha, classe, nivel):
        super().__init__(nome, senha)
        self._classe = classe
        self._nivel = nivel

    def get_classe(self):
        """Retorna a classe do personagem."""
        return self._classe

    def get_nivel(self):
        """Retorna o nível do personagem."""
        return self._nivel

    def subir_nivel(self):
        """Incrementa o nível do personagem em 1."""
        self._nivel += 1

    def exibir_info(self):
        """Exibe as informações do personagem."""
        return f"Nome: {self.get_nome()}, Classe: {self._classe}, Nível: {self._nivel}"

#Classes dos Personagens:

class Guerreiro(Personagem):
    def __init__(self, nome, senha, nivel):
        super().__init__(nome, senha, "Guerreiro", nivel)

class Mago(Personagem):
    def __init__(self, nome, senha, nivel):
        super().__init__(nome, senha, "Mago", nivel)

class Arqueiro(Personagem):
    def __init__(self, nome, senha, nivel):
        super().__init__(nome, senha, "Arqueiro", nivel)

class Ladino(Personagem):
    def __init__(self, nome, senha, nivel):
        super().__init__(nome, senha, "Ladino", nivel)

#Classe Jogo:

class Jogo:
    """
    Classe para gerenciar o estado do jogo, incluindo personagens e mestres.
    """
    def __init__(self):
        self._personagens = []
        self._mestres = []

    def adicionar_personagem(self, personagem):
        """Adiciona um personagem à lista de personagens."""
        self._personagens.append(personagem)

    def remover_personagem(self, nome):
        """Remove um personagem da lista pelo nome."""
        self._personagens = [p for p in self._personagens if p.get_nome() != nome]

    def adicionar_mestre(self, mestre):
        """Adiciona um mestre à lista de mestres."""
        self._mestres.append(mestre)

    def autenticar_usuario(self, nome, senha):
        """Autentica um usuário, seja mestre ou personagem, pelo nome e senha."""
        for mestre in self._mestres:
            if mestre.get_nome() == nome and mestre.autenticar(senha):
                return mestre
        for personagem in self._personagens:
            if personagem.get_nome() == nome and personagem.autenticar(senha):
                return personagem
        return None

    def listar_personagens(self):
        """Lista todos os personagens registrados."""
        for personagem in self._personagens:
            print(personagem.exibir_info())

    def listar_mestres(self):
        """Lista todos os mestres registrados."""
        for mestre in self._mestres:
            print(mestre.get_nome())

    def salvar_dados(self, filename):
        """Salva os dados dos personagens e mestres em um arquivo texto."""
        with open(filename, 'w') as file:
            file.write("Personagens:\n")
            for personagem in self._personagens:
                file.write(f"{personagem.get_nome()},{personagem.get_senha()},{personagem.get_classe()},{personagem.get_nivel()}\n")
            file.write("Mestres:\n")
            for mestre in self._mestres:
                file.write(f"{mestre.get_nome()},{mestre.get_senha()}\n")

    def carregar_dados(self, filename):
        """Carrega os dados dos personagens e mestres de um arquivo texto."""
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                modo = None
                for line in lines:
                    line = line.strip()
                    if line == "Personagens:":
                        modo = "personagens"
                    elif line == "Mestres:":
                        modo = "mestres"
                    elif modo == "personagens":
                        nome, senha, classe, nivel = line.split(',')
                        nivel = int(nivel)
                        if classe == "Guerreiro":
                            personagem = Guerreiro(nome, senha, nivel)
                        elif classe == "Mago":
                            personagem = Mago(nome, senha, nivel)
                        elif classe == "Arqueiro":
                            personagem = Arqueiro(nome, senha, nivel)
                        elif classe == "Ladino":
                            personagem = Ladino(nome, senha, nivel)
                        else:
                            continue
                        self.adicionar_personagem(personagem)
                    elif modo == "mestres":
                        nome, senha = line.split(',')
                        mestre = Mestre(nome, senha)
                        self.adicionar_mestre(mestre)
        except FileNotFoundError:
            print("Arquivo não encontrado. Nenhum dado carregado.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

#Interface do Terminal:

def menu():
    jogo = Jogo()
    jogo.carregar_dados('dados_jogo.txt')

    while True:
        print("\nSistema de Gerenciamento do Jogo")
        print("1. Adicionar Personagem")
        print("2. Remover Personagem")
        print("3. Adicionar Mestre")
        print("4. Listar Personagens")
        print("5. Listar Mestres")
        print("6. Autenticar Usuário")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Personagem: ")
            senha = input("Senha do Personagem: ")
            classe = input("Classe do Personagem (Guerreiro, Mago, Arqueiro, Ladino): ")
            try:
                nivel = int(input("Nível do Personagem: "))
                if nivel < 1:
                    raise ValueError("O nível deve ser um número positivo.")
            except ValueError as e:
                print(f"Erro: {e}")
                continue
            
            if classe == "Guerreiro":
                personagem = Guerreiro(nome, senha, nivel)
            elif classe == "Mago":
                personagem = Mago(nome, senha, nivel)
            elif classe == "Arqueiro":
                personagem = Arqueiro(nome, senha, nivel)
            elif classe == "Ladino":
                personagem = Ladino(nome, senha, nivel)
            else:
                print("Classe inválida.")
                continue
            
            jogo.adicionar_personagem(personagem)
            print("Personagem adicionado com sucesso.")

        elif escolha == "2":
            nome = input("Nome do Personagem a remover: ")
            jogo.remover_personagem(nome)
            print("Personagem removido com sucesso.")

        elif escolha == "3":
            nome = input("Nome do Mestre: ")
            senha = input("Senha do Mestre: ")
            mestre = Mestre(nome, senha)
            jogo.adicionar_mestre(mestre)
            print("Mestre adicionado com sucesso.")

        elif escolha == "4":
            jogo.listar_personagens()

        elif escolha == "5":
            jogo.listar_mestres()

        elif escolha == "6":
            nome = input("Nome do Usuário: ")
            senha = input("Senha do Usuário: ")
            usuario = jogo.autenticar_usuario(nome, senha)
            if usuario:
                if isinstance(usuario, Mestre):
                    print(usuario.mostrar_pagina_mestre())
                else:
                    print(f"Autenticação bem-sucedida para o personagem {usuario.get_nome()}.")
            else:
                print("Autenticação falhou.")

        elif escolha == "7":
            jogo.salvar_dados('dados salvos')
            print("Dados salvos.")
            break

        else:
            print("Opção inválida :( Tente novamente!")

if __name__ == "__main__":
    menu()
