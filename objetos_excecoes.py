#Nome do programa: objetos_excecoes.py
#Curso: informática
#Ano: 2° ano
#Turma: 2° B
#Disciplina: Programação Orientada a Objetos
#Integrantes: Áirica Soares Queroz, Arielle Kayla Xavier Almeida e Verônica Oliveira Sarmento
#Data: 17/11/2026
#Versão: 2.0

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
#A classe Vitima herda da classe Usuario
class Vitima(Usuario):
    def __init__(self, nome, telefone, cpf, senha, email, localizacao):
        super().__init__(nome, telefone, cpf)
        
        self.senha = "senha123"
        self.email = email
        self.localizacao = localizacao
        
#A vítima possui pessoas de confiança
        self.pessoasDeConfianca = []
        
#A vítima utiliza a classe Questionario
        self.questionario = None
        
#A vítima tem acesso aos audios provas
        self.audios = []

#Erro ao confirmar senha vazia
    def FazerLogin(self, senha_tentada):
        try:
           if not senha_tentada or len(senha_tentada.strip()) == 0:
              raise SenhaInvalidaError("A senha digitada não pode estar vazia.")
               
#No login, diferente do cadastro, a senha é definitiva
#Validando senha
           if self.senha != senha_tentada:
               raise SenhaInvalidaError("Senha incorreta.")

           print("Login realizado com sucesso.")
           return True

       except senhaInvalidaError as erro:
           print("Erro no login:", erro)
           return False

#Erro ao cadastrar ninguém
    def CadastrarContatos(self, nomeDeUsuario, numeroDeTelefone):
        try:
            if not nomeDeUsuario or len(nomeDeUsuario.strip()) == 0 or not nomeDeTelefone or len(numeroDeTelefone.strip()) == 0:
                raise ContatoInvalidoError("O nome e o telefone de contato não podem estar vazios.")
            
# Criando objeto PessoasDeConfianca
    contato = PessoasDeConfianca(nomeDeUsuario, numeroDeTelefone)
            
            self.pessoasDeConfianca.append(contato)
            print("Contatos cadastrados.")
            
        except ContatoInvalidoError as erro:
            print("Erro no cadastro de contato:", erro)
            raise
        
    def GravarAudio(self, audios):
        self.audios.append(audio)
        print("Áudio gravado.")

#Não há como enviar pedido de socorro se não houver alguém para recebê-la
    def PedirSocorro(self):
       try:
           if len(self.pessoasDeConfiança) == 0:
            raise IndexError("Nenhuma pessoa de confiança cadastrada.")
         print("Pedido de socorro enviado.")
            except IndexError as erro:
         print ("Erro de envio:", erro)
             raise

    def VerLocalizacao(self):
        print("Localização:", self.localizacao)

    def AcessarRedeDeApoio(self):
        print("Rede de apoio acessada.")

    def CompartilharLocalizacao(self):
        print("Localização compartilhada.")

    def ResponderQuestionario(self):
        print("Questionário respondido.")

#Não é possível compartilhar relato sem conteúdo algum
    def CompartilharRelatos(self, textoRelato):
       try:
           if not textoRelato or len (textoRelato.strip()) == 0:
            raise RelatoVazioError("O relato está vazio.")
        print("Relato compartilhado.")
              excepto RelatoVazioError as erro:
        print("Erro no envio:", erro)
            raise

#Classe PessoasDeConfiança com tratamento de exceção
class PessoasDeConfianca:
    def __init__(self, nomeDeUsuario, numeroDeTelefone):
        try:
#Validação do nome
           if not nomeDeUsuario or len(nomeDeUsuario.strip()) == 0:
             raise ContatoInvalidoError("O nome de usuário não pode estar vazio.")

           #Valida se o telefone foi preenchido
           if not número de telefone or len(número de telefone.strip()) == 0:
              raise Telefone inválido erro("O número de telefone não pode estar vazios.")

           #Verifica se há letras no número
           if any(c.isalpha() for c in número de telefone):
              raise Telefone inválido erro("O número de telefone não pode conter letras.")

          #Verifica se a quantidade de dígitos é diferente de 11
          if len(digitos_telefone) != 11:
             raise Telefone inválido erro("O número de telefone deve ter exatamente 11 dígitos.")

        self.nomeDeUsuario = nomeDeUsuario
        self.numeroDeTelefone = numeroDeTelefone
        
     except ContatoInvalidoError as erro:
         print("Erro no cadastro: ", erro)
         raise

    def receberSMSlocalizacao(self):
        print("SMS de localização recebido.")

#Classe BotaodePanico com tratamento de exceção
class BotaoDePanico:
    def __init__(self, data, hora, localizacao, sms, contato_cadastrado):
        self.data = data
        self.hora = hora
        self.localizacao = localizacao
        self.sms = sms
        self.contato_cadastrado = contato_cadastrado

    def EnviarSMSLocalizacao(self):
        try:
            if not self.sms.strip():
                raise ValueError("A mensagem SMS não pode estar vazia.")

            if not self.localizacao.strip():
                raise ValueError("A localização não foi informada.")

            if not self.contato_cadastrado:
                raise ValueError("Não existe ninguém cadastrado para receber o SMS.")

            print("SMS de localização enviado: ", self.sms)
            print("Localização:", self.localizacao)

        except ValueError as erro:
            print("Erro:", erro)
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

#Nessa classe não foram indentificados casos de exceção
class AudioProva:
    def __init__(self, data, hora, duracao, arquivo):
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.arquivo = arquivo

    def GuardaAudio(self):
        print("Áudio guardado.")

    def ArmazenarAudioNuvem(self):
        print("Novo áudio armazenado.")
