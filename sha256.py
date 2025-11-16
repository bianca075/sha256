# SHA-256 básico: cálculo do hash de uma string

# Hash inicial (8 constantes fixas)
HASH_INICIAL = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

# Constantes K (64 constantes usadas nas rodadas)
CONSTANTES = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
    0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
    0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
    0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
    0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

# Rotação à direita
def rotacionar_direita(valor, bits):
    return ((valor >> bits) | (valor << (32 - bits))) & 0xFFFFFFFF

# Prepara a string (padding + divisão em blocos)
def preparar_mensagem(texto):
    binario = ''.join(f'{ord(c):08b}' for c in texto) + '1'
    while len(binario) % 512 != 448:
        binario += '0'
    binario += f'{len(texto) * 8:064b}'
    return [binario[i:i+512] for i in range(0, len(binario), 512)]

# Expansão de palavras
def expandir(bloco):
    w = [int(bloco[i:i+32], 2) for i in range(0, 512, 32)]
    for i in range(16, 64):
        s0 = rotacionar_direita(w[i-15], 7) ^ rotacionar_direita(w[i-15], 18) ^ (w[i-15] >> 3)
        s1 = rotacionar_direita(w[i-2], 17) ^ rotacionar_direita(w[i-2], 19) ^ (w[i-2] >> 10)
        w.append((w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF)
    return w

# Cálculo do SHA-256
def calcular_sha256(texto):
    blocos = preparar_mensagem(texto)
    h = HASH_INICIAL.copy()

    for bloco in blocos:
        w = expandir(bloco)
        a, b, c, d, e, f, g, h_temp = h

        for i in range(64):
            S1 = rotacionar_direita(e, 6) ^ rotacionar_direita(e, 11) ^ rotacionar_direita(e, 25)
            ch = (e & f) ^ (~e & g)
            temp1 = (h_temp + S1 + ch + CONSTANTES[i] + w[i]) & 0xFFFFFFFF

            S0 = rotacionar_direita(a, 2) ^ rotacionar_direita(a, 13) ^ rotacionar_direita(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h_temp, g, f, e, d, c, b, a = g, f, e, (d + temp1) & 0xFFFFFFFF, c, b, a, (temp1 + temp2) & 0xFFFFFFFF

        h = [(x + y) & 0xFFFFFFFF for x, y in zip(h, [a, b, c, d, e, f, g, h_temp])]

    return ''.join(f'{valor:08x}' for valor in h)


if __name__ == "__main__":
    texto = input("Digite a mensagem para gerar o SHA-256: ")
    print("Hash SHA-256:", calcular_sha256(texto))
