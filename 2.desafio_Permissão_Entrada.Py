def main():
    # Entrada de dados do usuário
    has_permission = input().lower() == "true"
    age = int(input())

    # Verificação das condições de acesso
    if has_permission and age >= 18:
        print("Acesso permitido")
    elif not has_permission:
        print("Acesso negado")
    else:
        print("Idade insuficiente")

if __name__ == "__main__":
    main()