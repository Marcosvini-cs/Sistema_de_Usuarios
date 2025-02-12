from re import search
from stdiomask import getpass


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


def filtrar_usuarios(email, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.email == email]

    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    padrao = r"\@gmail.com"

    nome = input("Nome: ")
    email = input("Email: ")

    usuario = filtrar_usuarios(email, usuarios)
    testa_padrao = search(padrao, email)

    if not testa_padrao:
        print("\nEmail inválido!\n")

        return criar_usuario(usuarios)

    if usuario:
        print("\nJá existe usuário com esse email!\n")

        return criar_usuario(usuarios)

    senha = getpass(prompt="Senha: ", mask="*")

    if len(senha) < 7:
        print("\nSenha muito fraca!\n")

        return criar_usuario(usuarios)

    confirma_senha = getpass(prompt="Confirma senha: ", mask="*")

    if not senha == confirma_senha:
        print("\nAs senhas não são iguais!\n")

        return criar_usuario(usuarios)

    usuario = Usuario(nome, email, senha)

    usuarios.append(usuario)

    print("\nUsuário criado!")


def login(usuarios):
    email = input("Email: ")

    senha = getpass(prompt="senha: ", mask="*")

    usuario = filtrar_usuarios(email, usuarios)

    if senha != usuario.senha:
        print("\nEmail ou senha incorreto!\n")

        return login(usuarios)

    print(f"\nBem vindo! {usuario.nome.title()}.")


def menu():
    menu = """\n
=========MENU=========
[c]\tCriar conta
[l]\tLogin
[s]\tSair
======================
=> """

    return input(menu)


def main():
    usuarios = []

    while True:
        opcao = menu().strip()

        match opcao:
            case "c":
                criar_usuario(usuarios)

            case "l":
                login(usuarios)

            case "s":
                break

            case _:
                print(
                    "\nOperação inválida,"
                    "por favor selecione novamente a operação desejada."
                )


main()
