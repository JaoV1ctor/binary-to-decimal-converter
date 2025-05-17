def bin_to_decimal(binary_str):
    decimal = 0
    length = len(binary_str)

    for i in range(length):
        # Obtém o dígito atual (começando da esquerda para a direita)
        current_bit = binary_str[i]

        # Converte o caractere '0' ou '1' para inteiro
        bit_value = int(current_bit)

        # Calcula o peso do bit: 2^(posição), onde a posição é (tamanho - 1 - i)
        # Exemplo: "1011" (i=0 => posição = 3; i=1 => posição = 2; ...)
        position = length - 1 - i
        weight = pow(2, position)

        # Acumula o valor decimal
        decimal += bit_value * weight
    
    return decimal

# Entrada do Usuario
binary_str = input("Digite um numero binario (ate 8 digitos): ")

# Validação da entrada
if len(binary_str) > 8:
    print("Erro: Maximo de 8 digitos permitidos! Tente novamente.")
elif not all(bit in '01' for bit in binary_str) :
    print("Erro: Apenas 0s e 1s sao permitidos!")
else:
    decimal_output = bin_to_decimal(binary_str)
    print(f"O valor decimal de {binary_str} é: {decimal_output}")