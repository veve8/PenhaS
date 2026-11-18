#Nome do programa: objetos_excecoes.py
#Curso: informática
#Ano: 2° ano
#Turma: 2° B
#Disciplina: Programação Orientada a Objetos
#Integrantes: Áirica Soares Queroz, Arielle Kayla Xavier Almeida e Verônica Oliveira Sarmento
#Data: 17/11/2026
#Versão: 3.0

#VOLTAR AQUI APÓS SEÇÃO DE TESTE VERÔNICA NÃO ESQUECE LIXOSA

#Deixando as Exceções personalizadas prontas
class SenhaInvalidaError(Exception):
    pass

class ContatoInvalidoError(Exception):
    pass

class TelefoneInvalidoError(Exception):
    pass

class RelatoVazioError(Exception):
    pass


# Classe Usuario com tratamento de exceção
class Usuario:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = self.validar_telefone(telefone)
        self.cpf = self.validar_cpf(cpf)
        self.senha = ""

    def validar_telefone(self, telefone):
        try:
            if not telefone.isdigit():
                raise ValueError("O telefone não pode conter letras ou símbolos.")

            if len(telefone) != 11:
                raise ValueError("O telefone deve ter exatamente 11 dígitos.")

            return telefone

        except ValueError as erro:
            print("Erro no telefone:", erro)
            raise

    def validar_cpf(self, cpf):
        try:
            if not cpf.isdigit():
                raise ValueError("O CPF não pode conter letras ou símbolos.")

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

        self.senha = senha
        self.email = email
        self.localizacao = localizacao

#A vítima possui pessoas de confiança
        self.pessoasDeConfianca = []

#A vítima utiliza a classe AudioProva
        self.audios = []

    def FazerLogin(self, senha_tentada):
        try:
            if not senha_tentada or len(senha_tentada.strip()) == 0:
                raise SenhaInvalidaError("A senha não pode estar vazia.")

            if self.senha != senha_tentada:
                raise SenhaInvalidaError("Senha incorreta.")

            print("Login realizado com sucesso.")
            return True

        except SenhaInvalidaError as erro:
            print("Erro no login:", erro)
            return False

#Cria e armazena uma pessoa de confiança
    def CadastrarContatos(self, nomeDeUsuario, numeroDeTelefone):
        contato = PessoasDeConfianca(nomeDeUsuario, numeroDeTelefone)
        self.pessoasDeConfianca.append(contato)
        print("Contatos cadastrados.")

#A vítima utiliza a classe AudioProva
    def GravarAudio(self, audio):
        self.audios.append(audio)
        audio.GuardarAudio()
        print("Áudio gravado pela vítima.")

    def PedirSocorro(self):
        try:
            if len(self.pessoasDeConfianca) == 0:
                raise IndexError("Nenhuma pessoa de confiança cadastrada.")

            print("Pedido de socorro enviado.")

        except IndexError as erro:
            print("Erro de envio:", erro)
            raise

    def VerLocalizacao(self):
        print("Localização:", self.localizacao)

    def AcessarRedeDeApoio(self):
        print("Rede de apoio acessada.")

    def CompartilharLocalizacao(self):
        print("Localização compartilhada.")

#A vítima utiliza a classe Questionario
    def ResponderQuestionario(self, questionario):
        questionario.Retornarmanual()
        questionario.RetornarAvaliacao()
        questionario.ValidarResposta()

    def CompartilharRelatos(self, textoRelato):
        try:
            if not textoRelato or len(textoRelato.strip()) == 0:
                raise RelatoVazioError("O relato está vazio.")

            print("Relato compartilhado.")

        except RelatoVazioError as erro:
            print("Erro no envio:", erro)
            raise


#Classe PessoasDeConfianca com tratamento de exceção
class PessoasDeConfianca:
    def __init__(self, nomeDeUsuario, numeroDeTelefone):
        try:
# Validação do nome
            if not nomeDeUsuario or len(nomeDeUsuario.strip()) == 0:
                raise ContatoInvalidoError("O nome de usuário não pode estar vazio.")

# Validação do telefone
            if not numeroDeTelefone or len(numeroDeTelefone.strip()) == 0:
                raise TelefoneInvalidoError("O número de telefone não pode estar vazio.")

# Verifica se o telefone contém somente números
            if not numeroDeTelefone.isdigit():
                raise TelefoneInvalidoError("O número de telefone não pode conter letras ou símbolos.")

# Verifica a quantidade de dígitos
            if len(numeroDeTelefone) != 11:
                raise TelefoneInvalidoError("O número de telefone deve ter exatamente 11 dígitos.")

            self.nomeDeUsuario = nomeDeUsuario
            self.numeroDeTelefone = numeroDeTelefone

        except ContatoInvalidoError as erro:
            print("Erro no cadastro:", erro)
            raise

        except TelefoneInvalidoError as erro:
            print("Erro no cadastro:", erro)
            raise

    def receberSMSlocalizacao(self):
        print("SMS de localização recebido.")


#Classe BotaoDePanico com tratamento de exceção
class BotaoDePanico:
    def __init__(self, data, hora, localizacao, sms, contato_cadastrado):
        self.data = data
        self.hora = hora
        self.localizacao = localizacao
        self.sms = sms
        self.contato_cadastrado = contato_cadastrado

#Utiliza um objeto da classe PessoasDeConfianca
    def EnviarSMSLocalizacao(self):
        try:
            if not self.sms or len(self.sms.strip()) == 0:
                raise ValueError("A mensagem SMS não pode estar vazia.")

            if not self.localizacao or len(self.localizacao.strip()) == 0:
                raise ValueError("A localização não foi informada.")

            if not self.contato_cadastrado:
                raise ValueError("Não existe ninguém cadastrado para receber o SMS.")

            print("SMS de localização enviado:", self.sms)
            print("Localização:", self.localizacao)

            self.contato_cadastrado.receberSMSlocalizacao()

        except ValueError as erro:
            print("Erro:", erro)
            raise


#Classe Relatos com tratamento de exceção
class Relatos:
    def __init__(self, nomeDeUsuario, textos, hora, data):
        try:
            if not textos or len(textos.strip()) == 0:
                raise RelatoVazioError("O relato não pode estar vazio.")

            self.nomeDeUsuario = nomeDeUsuario
            self.textos = textos
            self.hora = hora
            self.data = data

        except RelatoVazioError as erro:
            print("Erro ao criar relato:", erro)
            raise

    def RegistrarRelato(self):
        try:
            if not self.textos or len(self.textos.strip()) == 0:
                raise RelatoVazioError("Não é possível registrar um relato vazio.")

            print("Relato registrado.")

        except RelatoVazioError as erro:
            print("Erro ao registrar relato:", erro)
            raise

    def ReceberComentarios(self):
        print("Comentários recebidos.")


#Classe RedeDeApoio com tratamento de exceção
class RedeDeApoio:
    def __init__(self, nomeDeUsuario, textos, data, arquivo):
        self.nomeDeUsuario = nomeDeUsuario
        self.textos = textos
        self.data = data
        self.arquivo = arquivo

#A rede de apoio possui relatos
        self.relatos = []

    def AcessarServicosProtecao(self):
        print("Serviços de proteção acessados.")
#Cria e armazena objetos da classe Relatos
    def CompartilharRelatos(self, nomeDeUsuario, textos, hora, data):
        try:
            if not textos or len(textos.strip()) == 0:
                raise RelatoVazioError("O relato está vazio.")

            relato = Relatos(nomeDeUsuario, textos, hora, data)
            self.relatos.append(relato)

            print("Relato compartilhado na rede de apoio.")

        except RelatoVazioError as erro:
            print("Erro ao compartilhar relatos na rede de apoio:", erro)
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
            if not self.perguntas or len(self.perguntas.strip()) == 0:
                raise ValueError("A pergunta não pode estar vazia.")

            if not self.resposta or len(self.resposta.strip()) == 0:
                raise ValueError("A resposta não pode estar vazia.")

            print("Questionário respondido com sucesso.")

        except ValueError as erro:
            print("Erro no questionário:", erro)
            raise


#Classe AudioProva
#Não foram identificados casos de exceção
class AudioProva:
    def __init__(self, data, hora, duracao, arquivo):
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.arquivo = arquivo

    def GuardarAudio(self):
        print("Áudio guardado.")

    def ArmazenarAudioNuvem(self):
        print("Novo áudio armazenado.")
