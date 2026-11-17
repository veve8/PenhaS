#Nome do programa: objetos_excecoes.py
#Curso: informática
#Ano: 2° ano
#Turma: 2° B
#Disciplina: Programação Orientada a Objetos
#Integrantes: Áirica Soares Queroz, Arielle Kayla Xavier Almeida e Verônica Oliveira Sarmento
#Data: 16/11/2026
#Versão: 1.0

#Classe Usuario com tratamento de exceção
class Usuario:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = self.validar_telefone(telefone)
        self.cpf = self.validar_cpf(cpf)
        self.senha = ""

    def validar_telefone(self, telefone):
        try:
            if not telefone.isdigit():
                raise ValueError("O telefone não pode conter letras.")

            if len(telefone) != 11:
                raise ValueError("O telefone deve ter exatamente 11 dígitos.")

            return telefone

        except ValueError as erro:
            print("Erro no telefone:", erro)
            raise

    def validar_cpf(self, cpf):
        try:
            if not cpf.isdigit():
                raise ValueError("O CPF não pode conter letras.")

            if len(cpf) != 11:
                raise ValueError("O CPF deve ter exatamente 11 dígitos.")

            return cpf

        except ValueError as erro:
            print("Erro no CPF:", erro)
            raise

    def FazerCadastro(self, senha):
        self.senha = senha
        print("Cadastro realizado com sucesso.")

    def FazerLogin(self, senha):
        return self.senha == senha

#Classe Vitima com tratamento de exceção
#A classe vitima herda da classe Usuario
class Vitima(Usuario):
    def __init__(self, nome, telefone, cpf, senha, email, localizacao):
        super().__init__(nome, telefone, cpf)
        
#A vítima já possui uma conta cadastrada, então precisa de uma senha definitiva
        self.senha = senha

        self.email = email
        self.localizacao = localizacao
        
#A vítima possui pessoas de confiança
        self.pessoasDeConfianca = []
        
#A vítima utiliza a classe Questionario
        self.questionario = None
        
#A vítima grava audios provas
        self.audios = []

#Diferente de cadastro, login mantem uma senha definitiva, pois a conta já está criada
#Validando a senha
def FazerLogin(self, senha_tentada):
    try:
        if not senha_tentada or len(senha_tentada.strip()) == 0:
            raise SenhaInvalidaError("Senha incorreta.")
        print("Login realizado com sucesso.")
        return True
    except SenhaInvalidaError as erro:
        print("Erro no login: ", erro)
        return False

#Impedindo o usuário de cadastrar nada

#Classe Questionario com tratamento de exceção
class Questionario:
    def __init__(self, perguntas, resposta):
        self.perguntas = perguntas
        self.resposta = resposta

    def Retornarmanual(self):
        print("Manual disponível.")

    def RetornarAvaliacao(self):
        print("Avaliação disponível.")

    def ValidarResposta(self):
        try:
            if not self.perguntas.strip():
                raise ValueError("A pergunta não pode estar vazia.")

            if not self.resposta.strip():
                raise ValueError("A resposta não pode estar vazia.")

            print("Questionário respondido com sucesso.")

        except ValueError as erro:
            print("Erro no questionário:", erro)
            raise

#Classe Questionario com tratamento de exceção
class Questionario:
    def __init__(self, perguntas, resposta):
        self.perguntas = perguntas
        self.resposta = resposta

    def Retornarmanual(self):
        print("Manual disponível.")

    def RetornarAvaliacao(self):
        print("Avaliação disponível.")

    def ValidarResposta(self):
        try:
            if not self.perguntas.strip():
                raise ValueError("A pergunta não pode estar vazia.")

            if not self.resposta.strip():
                raise ValueError("A resposta não pode estar vazia.")

            print("Questionário respondido com sucesso.")

        except ValueError as erro:
            print("Erro no questionário:", erro)
            raise
