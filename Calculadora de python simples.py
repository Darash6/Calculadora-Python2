def main():
    while True:
        try:
            a = int(input("Digite o primeiro número: "))

            b = int(input("Digite o segundo número: "))

            c = input("Escolha a operação (+, -, *, /): ")

            if c == '+':
                print(f"Resultado: {a + b}")

            elif c == '-':
                print(f"Resultado: {a - b}")

            elif c == '*':
                print(f"Resultado: {a * b}")

            elif c == '/':
                if b != 0:
                    print(f"Resultado: {a / b}")

                else:

                    print("Erro: Divisão por zero não é permitida.")
            else:

                print("Operação inválida. Escolha entre +, -, *, ou /.")

            reiniciar = input("Deseja recomeçar? (s/n): ")

            if reiniciar.lower() != 's':
                break
        except ValueError:
            print("Erro: Insira números inteiros válidos.")


if __name__ == "__main__":
    main()
