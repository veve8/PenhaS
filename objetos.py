#Nome do programa: objetos.py
#Curso: informática
#Ano: 2° ano
#Turma: 2° B
#Disciplina: Programação Orientada a Objetos
#Integrantes: Áirica Soares Queroz, Arielle Kayla Xavier Almeida e Verônica Oliveira Sarmento
#Data: 14/11/2026
#Versão: 5.0
        
#Criando a classe Usuario
class Usuario:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.senha = ""
        
#Criando a função para fazer cadastro
    def FazerCadastro(self, senha):
        self.senha = senha
        print("Cadastro realizado com sucesso.")
        
#Criando a função de fazer login     
    def FazerLogin(self, senha):
        return self.senha == senha

#Criando a classe Vitima, que herda de Usuario (Herança)
class Vitima(Usuario):
    def init(self, nome, telefone, cpf, senha, email, localizacao):
        super().init(nome, telefone, cpf)
        
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
        
    def CadastrarContatos(self, nomeDeUsuario, numeroDeTelefone):
#Criando objeto pessoasDeConfianca
        contato = PessoasDeConfianca(nomeDeUsuario, numeroDeTelefone)
        
        self.pessoasDeConfianca.append(contato)
        
        print("Contatos cadastrados.")

#Criando a função para gravar áudios
    def GravarAudio(self, audio):
        self.audios.append(audio)
        print("Áudio gravado.")

#Criando a função para pedir socorro (enviar mensagem para pessoas de confiança)
    def PedirSocorro(self):
        print("Pedido de socorro enviado.")

#Criando a função para ver a localização
    def VerLocalizacao(self):
        print("Localização:", self.localizacao)

#Criando a função para acessar a rede de apoio
    def AcessarRedeDeApoio(self):
        print("Rede de apoio acessada.")

#Criando a função para compartilhar a localização com pessoas de confiança
    def CompartilharLocalizacao(self):
        print("Localização compartilhada.")

#Criando a função para a vítima responder o questionário
    def ResponderQuestionario(self):
        print("Questionário respondido.")

#Criando a função para a vítima compartilhar relatos na rede de apoio
    def CompartilharRelatos(self):
        print("Relato compartilhado.")

#Criando a classe PessoasDeConfianca, cadastradas pela vítima (Composição)
class PessoasDeConfianca:
    def __init__(self, nomeDeUsuario, numeroDeTelefone):
        self.nomeDeUsuario = nomeDeUsuario
        self.numeroDeTelefone = numeroDeTelefone

#Criando a função para receber a localização da vítima
    def receberSMSlocalizacao(self):
        print("SMS de localização recebido.")

#Criando a classe BotaoDePanico, dependente da vítima (Dependência)
class BotaoDePanico:
    def __init__(self, data, hora, localizacao, sms):
        self.data = data
        self.hora = hora
        self.localizacao = localizacao
        self.sms = sms

  #Criando a função para enviar a localização da vítima via SMS para as pessoas de confiança
    def EnviarSMSLocalizacao(self, contato):
        print("SMS de localização enviado:")
        print(self.sms)
        
        contato.receberSMSlocalizacao()

#Criando a classe Relatos
class Relatos:
    def __init__(self, nomeDeUsuario, textos, hora, data):
        self.nomeDeUsuario = nomeDeUsuario
        self.textos = textos
        self.hora = hora
        self.data = data

  #Criando a função para registrar relatos
    def RegistrarRelato(self):
        print("Relato registrado.")

    def ReceberComentarios(self):
        print("Comentários recebidos.")

#Criando a classe RedeDeApoio, composta por relatos (Composição)
class RedeDeApoio:
    def __init__(self, nomeDeUsuario, textos, data, arquivo):
        self.nomeDeUsuario = nomeDeUsuario
        self.textos = textos
        self.data = data
        self.arquivo = arquivo
        
#A rede de apoio possui CompartilharRelatos
        self.relatos = []
        
    def AcessarServicosProtecao(self):
        print("Serviços de proteção acessados.")
        
    def CompartilharRelatos(self, nomeDeUsuario, textos, hora, data):
        
#Criando objeto relatos     
        relato = Relatos(nomeDeUsuario, textos, hora, data)
        
        self.relatos.append(relato)
        
        print("Relato compartilhado na rede de apoio.")

#Criando a classe Questionario, dependente da vítima (Dependência)
class Questionario:
    def __init__(self, perguntas, resposta):
        self.perguntas = perguntas
        self.resposta = resposta

#Criando a função para retornar o manual de fuga
    def Retornarmanual(self):
        print("Manual disponível.")

#Criando a função para retornar a avaliação da situação
    def RetornarAvaliacao(self):
        print("Avaliação disponível.")

#Criando a classe AudioProva, dependente da vítima (Dependência)
class AudioProva:
    def __init__(self, data, hora, duracao, arquivo):
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.arquivo = arquivo

#Criando a função para a vítima guardar o áudio gravado
    def GuardaAudio(self):
        print("Áudio guardado.")

#Criando a função para a vítima armazenar o áudio na nuvem
    def ArmazenarAudioNuvem(self):
        print("Novo áudio armazenado.")
