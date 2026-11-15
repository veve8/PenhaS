

from objetos import *

print("CLASSE USUARIO")
#Criando objeto usuario
usuario = Usuario("Fulana", "69999999999", "12345678910")

#Atributos
print("Nome: ", usuario.nome)
print("Telefone: ", usuario.telefone)
print("CPF: ", usuario.cpf)

#Método de cadastro ("inventar" a senha)
usuario.FazerCadastro("senha123")

#Método de login
print("Login correto: ")
print(usuario.FazerLogin("senha123"))

print("Login incorreto: ")
print(usuario.FazerLogin("senha456"))

print("___________________________________________")

questionario = Questionario("Exemplo de pergunta", "Exemplo de resposta")

print("CLASSE VITIMA")
#Criando objeto vitima
vitima = Vitima("Fulana", "69999999999", "12345678910", "senha123", "@fulana@gmail.com", "Porto Velho")

#Atributos herdados
print("Nome: ", vitima.nome)
print("Telefone: ", vitima.telefone)
print("CPF: ", vitima.cpf)
print("Senha: ", vitima.senha)

#Atributos próprios
print("Email: ", vitima.email)
print("Localização: ", vitima.localizacao)

#Método herdado (login)
print("Login correto: ")
print(vitima.FazerLogin("senha123"))

print("Login incorreto: ")
print(vitima.FazerLogin("senha456"))

#Cadastro de pessoas de confiança
vitima.CadastrarContatos("Sicrana", "69998888888")

#Método de gravar áudio
audio = AudioProva("01/01/2026", "15:23", "01:24", "audio.mp3")
vitima.GravarAudio(audio)

#Demais métodos
vitima.PedirSocorro()
vitima.VerLocalizacao()
vitima.AcessarRedeDeApoio()
vitima.CompartilharLocalizacao()
vitima.ResponderQuestionario(questionario)
vitima.CompartilharRelatos()
print("___________________________________________")

print("CLASSE PESSOASDECONFIANCA")
#Criando objeto contato
contato = PessoasDeConfianca("Sicrana", "69988888888")

print("Nome: ", contato.nomeDeUsuario)
print("Telefone: ", contato.numeroDeTelefone)

contato.receberSMSlocalizacao()
print("___________________________________________")

#Testando composição (pessoas de confiança e vítima)
print("TESTE DE RELAÇÃO (COMPOSIÇÃO)")
vitima.CadastrarContatos("Sicrana", "69988888888")

print("Quantidade de contatos cadastrados: ", len(vitima.pessoasDeConfianca))
print("___________________________________________")

print("CLASSE BOTAODEPANICO")

#Criando objeto botao
botao = BotaoDePanico("01/01/2026", "15:58", "Porto Velho", "Pedido de socorro!")

print("Data: ", botao.data)
print("Horário: ", botao.hora)
print("Localização: ", botao.localizacao)
print("SMS: ", botao.sms)
print("___________________________________________")

print("CLASSE RELATOS")
#Criando objeto relato
relato = Relatos("Beltrana", "Relato da Beltrana", "16:23", "02/01/2026")

print("Nome de Usuário: ", relato.nomeDeUsuario)
print("Relato: ", relato.textos)
print("Horário: ", relato.hora)
print("Data: ", relato.data)

relato.RegistrarRelato()
relato.ReceberComentarios()
print("___________________________________________")

print("CLASSE REDEDEAPOIO")
#Criando objeto rede
rede = RedeDeApoio("Beltrana", "Relato da Beltrana", "02/01/2026", "relato.pdf")

print("Nome de Usuário: ", rede.nomeDeUsuario)
print("Relato: ", rede.textos)
print("Data: ", rede.data)
print("Arquivo: ", rede.arquivo)

rede.AcessarServicosProtecao()
print("___________________________________________")
#Testando composição (relatos e rede de apoio)
rede.CompartilharRelatos("Maria", "Teste de relato.", "16:53", "03/01/2026")

print("Quantidade de relatos compartilhados: ", len(rede.relatos))
print("Texto do relato: ", rede.relatos[0].textos)
print("___________________________________________")

print("CLASSE QUESTIONARIO")

print("Perguntas: ", questionario.perguntas)
print("Resposta: ", questionario.resposta)

questionario.Retornarmanual()
questionario.RetornarAvaliacao()
print("___________________________________________")

print("CLASSE AUDIOPROVA")
#Criando o objeto audio
audio = AudioProva("04/01/2026", "18:18", "00:45", "audio.mp3")

print("Data: ", audio.data)
print("Horário: ", audio.hora)
print("Duração: ", audio.duracao)
print("Arquivo: ", audio.arquivo)

audio.GuardarAudio()
audio.ArmazenarAudioNuvem()

#Testando dependência (vítima e AudioProva)
vitima.GravarAudio(audio)

print("Quantidade de áudios gravados: ", len(vitima.audios))
print("___________________________________________")
