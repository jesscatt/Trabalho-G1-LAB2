# Imagine que estamos no auge dos anos 2000 e somos chamados para desenvolvermos um
# software para uma locadora de filmes. A locadora já possui um sistema que armazena o inventário de
# suas cópias de filmes, porém não consegue administrar quais dos seus filmes estão locados e quais
# estão disponíveis para locação. O atual sistema disponibiliza a lista de filmes na seguinte estrutura:

def menu():
    print("##################")
    print("Q")



def login():
    user = input("Digite o nome de usuário: ")
    password = int(input("Digite a senha:"))
    if user == "admin@locadora.com.br" and password == "_security_password":
        menu()
    else:
        print("")

def main():
    dict = {
        "movies": [
            {
            "name": "MIB - Homens de Preto",
            "year": 1997,
            "amount": 3,
            "age_group": 12,
            "located": [
                {}
            ]
            }
        ],
        "username": "admin@locadora.com.br",
        "password": "a_security_password"
    }

    print("1 - Entrar como adm")
    print("2 - Entrar como visitante")
    opc = int(input("Qual a sua opção? "))
    if opc == 2:
        checkmovies():
    if opc == 1:
        login()







main()
