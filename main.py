from objetos import *

print("CLASSE USUARIO")

#Criando objeto usuario
usuario = Usuario("Fulana", "69999999999", "12345678910")

#Atributos
print("Nome: ", usuario.nome)
print("Telefone: ", usuario.telefone)
print("CPF: ", usuario.cpf)

#Função de cadastro ("inventar" a senha)
usuario.FazerCadastro("senha123")

#Função de login
print("Login correto: ")
print(usuario.FazerLogin("senha123"))

print("Login incorreto: ")
print(usuario.FazerLogin("senha456"))

print("___________________________________________")

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

#Funções herdadas
