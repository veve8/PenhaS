#Nome do programa: main_objetos.py
#Curso: informática
#Ano: 2° ano
#Turma: 2° B
#Disciplina: Programação Orientada a Objetos
#Integrantes: Áirica Soares Queroz, Arielle Kayla Xavier Almeida e Verônica Oliveira Sarmento
#Data: 16/11/2026
#Versão: 1.0

from objetos_excecoes import *

#Testando as classes com casos de erro
print("CLASSE USUARIO")

#Telefone com letras
try:
  usuario = Usuario("Fulana", "699999999ab", "12345678910")
  #Atributos
  print("Nome: ", usuario.nome)
  print("Telefone: ", usuario.telefone)
  print("CPF: ", usuario.cpf)
except ValueError as erro:
  print(erro)

#Telefone com menos de 11 dígitos
try:
  usuario = Usuario("Fulana", "699999999", "12345678910")
  #Atributos
  print("Nome: ", usuario.nome)
  print("Telefone: ", usuario.telefone)
  print("CPF: ", usuario.cpf)
except ValueError as erro:
  print(erro)

#Telefone com mais de 11 dígitos
try:
  usuario = Usuario("Fulana", "69999999999", "12345678910")
  #Atributos
  print("Nome: ", usuario.nome)
  print("Telefone: ", usuario.telefone)
  print("CPF: ", usuario.cpf)
except ValueError as erro:
  print(erro)

#CPF com letras
try:
  usuario = Usuario("Fulana", "69999999999", "123456789ab")
  print("Nome: ", usuario.nome)
  print("Telefone: ", usuario.telefone)
  print("CPF: ", usuario.cpf)
except ValueError as erro:
  print(erro)

#CPF com menos de 11 dígitos
try:
  usuario = Usuario("Fulana", "69999999999", "123456789")
  print("Nome: ", usuario.nome)
  print("Telefone: ", usuario.telefone)
  print("CPF: ", usuario.cpf)
except ValueError as erro:
  print(erro)

#CPF com mais de 11 dígitos
try:
  usuario = Usuario("Fulana", "69999999999", "123456789101")
  print("Nome: ", usuario.nome)
  print("Telefone: ", usuario.telefone)
  print("CPF: ", usuario.cpf)
except ValueError as erro:
  print(erro)

#Criando objeto com dados válidos
print("___________________________________________")
print("OBJETO DA CLASSE USUÁRIO COM DADOS VÁLIDOS")
usuario = Usuario("Fulana", "69999999999", "12345678910")
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

#Definindo objeto antes para poder utiliza-la para representar caso de dependência em Vitima
questionario = Questionario("Exemplo de pergunta", "Exemplo de resposta")

'''print("CLASSE VITIMA")
#Senha vazia
try:
  senha = Vitima("")
  senha.FazerLogin()
  print("Senha: ", senha.senha_tentada)
except SenhaInvalidaError as erro:
  print(erro)

#Senha errada
try:
  senha = Vitima("senha124")
  senha.FazerLogin()
  print("Senha: ", senha.senha_tentada)
except SenhaInvalidaError as erro:
  print(erro)''' 
print("CLASSE QUESTIONARIO")
#Pergunta vazia
try:
  perguntas_resposta = Questionario("", "Exemplo de resposta.")
  perguntas_resposta.ValidarResposta()
  print("Perguntas: ", questionario.perguntas)
  print("Resposta: ", questionario.resposta)
except ValueError as erro:
  print(erro)

#Resposta vazia
try:
  perguntas_resposta = Questionario("Exemplo de pergunta.", "")
  perguntas_resposta.ValidarResposta()
  print("Perguntas: ", questionario.perguntas)
  print("Resposta: ", questionario.resposta)
except ValueError as erro:
  print(erro)

#Criando objetos com dados válidos
print("___________________________________________")
print("OBJETO DA CLASSE QUESTIONARIO COM DADOS VÁLIDOS")
perguntas_resposta = Questionario("Exemplo de pergunta.", "Exemplo de resposta.")
print("Perguntas: ", questionario.perguntas)
print("Resposta: ", questionario.resposta)

questionario.Retornarmanual()
questionario.RetornarAvaliacao()
print("___________________________________________")

#A classe AudioProva não recebeu tratamento de exceção pois não foi necessário
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
