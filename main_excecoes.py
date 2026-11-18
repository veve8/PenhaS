#Nome do programa: main_excecoes.py
#Curso: informática
#Ano: 2° ano
#Turma: 2° B
#Disciplina: Programação Orientada a Objetos
#Integrantes: Áirica Soares Queroz, Arielle Kayla Xavier Almeida e Verônica Oliveira Sarmento
#Data: 16/11/2026
#Versão: 1.0

from objetos_excecoes import *

#Testando as classes com casos de exceção
#Classe Usuario

#Telefone com letras
try:
    usuario = Usuario("Fulana", "699999999ab", "12345678910")
except ValueError as erro:
    print(erro)

#Telefone com menos de 11 dígitos
try:
    usuario = Usuario("Fulana", "699999999", "12345678910")
except ValueError as erro:
    print(erro)

#Telefone com mais de 11 dígitos
try:
    usuario = Usuario("Fulana", "699999999999", "12345678910")
except ValueError as erro:
    print(erro)

#CPF com letras
try:
    usuario = Usuario("Fulana", "69999999999", "123456789ab")
except ValueError as erro:
    print(erro)

#CPF com menos de 11 dígitos
try:
    usuario = Usuario("Fulana", "69999999999", "123456789")
except ValueError as erro:
    print(erro)

#CPF com mais de 11 dígitos
try:
    usuario = Usuario("Fulana", "69999999999", "123456789101")
except ValueError as erro:
    print(erro)


#Classe PessoasDeConfianca

#Nome vazio
try:
    contato = PessoasDeConfianca("", "69999999999")
except ContatoInvalidoError as erro:
    print("Exceção capturada:", erro)

#Telefone vazio
try:
    contato = PessoasDeConfianca("Maria", "")
except TelefoneInvalidoError as erro:
    print("Exceção capturada:", erro)

#Telefone com letras
try:
    contato = PessoasDeConfianca("Maria", "699999999ab")
except TelefoneInvalidoError as erro:
    print("Exceção capturada:", erro)

#Telefone com menos de 11 dígitos
try:
    contato = PessoasDeConfianca("Maria", "699999999")
except TelefoneInvalidoError as erro:
    print("Exceção capturada:", erro)

#Telefone com mais de 11 dígitos
try:
    contato = PessoasDeConfianca("Maria", "699999999999")
except TelefoneInvalidoError as erro:
    print("Exceção capturada:", erro)


#Classe Relatos
#Relato vazio
try:
    relato = Relatos("Ana", "", "15:56", "04/01/2026")
except RelatoVazioError as erro:
    print("Exceção capturada:", erro)


#Classe RedeDeApoio
#Relato vazio
try:
    rede = RedeDeApoio("Maria", "", "15/11/2026", "documento.pdf")

    print("Nome de usuário:", rede.nomeDeUsuario)
    print("Textos:", rede.textos)
    print("Data:", rede.data)
    print("Arquivo:", rede.arquivo)

    rede.CompartilharRelatos("Maria", "", "19:37", "15/11/2026")

except RelatoVazioError as erro:
    print("Exceção capturada:", erro)


#Classe Questionario
#Pergunta vazia
try:
    perguntas = Questionario("", "Exemplo de resposta.")
    print("Perguntas:", perguntas.perguntas)
    print("Resposta:", perguntas.resposta)
    perguntas.ValidarResposta()

except ValueError as erro:
    print("Exceção capturada:", erro)

#Resposta vazia
try:
    resposta = Questionario("Exemplo de pergunta.", "")
    print("Perguntas:", resposta.perguntas)
    print("Resposta:", resposta.resposta)
    resposta.ValidarResposta()

except ValueError as erro:
    print("Exceção capturada:", erro)


#Classes com dados predefinidos
#Classe Usuario
usuario = Usuario("Fulana", "69999999999", "12345678910")

print("Nome:", usuario.nome)
print("Telefone:", usuario.telefone)
print("CPF:", usuario.cpf)

usuario.FazerCadastro("senha123")

print("Login correto:")
print(usuario.FazerLogin("senha123"))

print("Login incorreto:")
print(usuario.FazerLogin("senha456"))


#Objeto Questionario
#Criado primeiro para representar a dependência com Vitima
questionario = Questionario("Exemplo de pergunta.", "Exemplo de resposta.")

#Classe Vitima
vitima = Vitima("Ana", "69999999999", "12345678910", "senha123", "ana@email.com", "Porto Velho - RO")

print("Nome:", vitima.nome)
print("Telefone:", vitima.telefone)
print("CPF:", vitima.cpf)
print("E-mail:", vitima.email)
print("Localização:", vitima.localizacao)

#Testando FazerLogin
vitima.FazerLogin("")

vitima.FazerLogin("senhaerrada")

vitima.FazerLogin("senha123")

#Testando métodos
vitima.VerLocalizacao()
vitima.AcessarRedeDeApoio()
vitima.CompartilharLocalizacao()

#Testando dependência com Questionario
vitima.ResponderQuestionario(questionario)

#Testando composição com PessoasDeConfiança
vitima.CadastrarContatos("Maria", "69999999999")

#Testando PedirSocorro
vitima.PedirSocorro()

print("Quantidade de contatos:", len(vitima.pessoasDeConfianca))


#Classe PessoasDeConfianca 
contato = PessoasDeConfianca("Maria", "69999999999")

print("Nome:", contato.nomeDeUsuario)
print("Telefone:", contato.numeroDeTelefone)

contato.receberSMSlocalizacao()

#Classe BotaoDePanico
print("CLASSE BOTAO DE PANICO")

botao = BotaoDePanico("17/11/2026", "18:00", "Porto Velho - RO", "Preciso de ajuda! Minha localização é Porto Velho.", contato)

print("Data:", botao.data)
print("Hora:", botao.hora)
print("Localização:", botao.localizacao)
print("SMS:", botao.sms)

botao.EnviarSMSLocalizacao()


#Classe Relatos 
relato = Relatos("Ana", "Exemplo de texto.", "16:12", "04/01/2026")

print("Nome de usuário:", relato.nomeDeUsuario)
print("Relato:", relato.textos)
print("Horário:", relato.hora)
print("Data:", relato.data)

relato.RegistrarRelato()
relato.ReceberComentarios()


#Classe RedeDeApoio
rede = RedeDeApoio("Maria", "Exemplo de texto.", "15/11/2026", "documento.pdf")

print("Nome de usuário:", rede.nomeDeUsuario)
print("Textos:", rede.textos)
print("Data:", rede.data)
print("Arquivo:", rede.arquivo)

rede.AcessarServicosProtecao()

rede.CompartilharRelatos("Maria", "Exemplo de texto.", "19:37", "15/11/2026")

#Testando composição entre RedeDeApoio e Relatos
print("Quantidade de relatos compartilhados:", len(rede.relatos))
print("Texto do relato:", rede.relatos[0].textos)

#Classe Questionario 
print("Perguntas:", questionario.perguntas)
print("Resposta:", questionario.resposta)

questionario.Retornarmanual()
questionario.RetornarAvaliacao()
questionario.ValidarResposta()

#Classe AudioProva
audio = AudioProva("04/01/2026", "18:18", "00:45", "audio.mp3")

print("Data:", audio.data)
print("Horário:", audio.hora)
print("Duração:", audio.duracao)
print("Arquivo:", audio.arquivo)

audio.GuardarAudio()
audio.ArmazenarAudioNuvem()

#Testando dependência entre Vitima e AudioProva
vitima.GravarAudio(audio)

print("Quantidade de áudios gravados:", len(vitima.audios))
