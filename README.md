# Implementação didática de SHA-256 em Python

Este repositório contém uma implementação simples e **didática** do algoritmo de hash SHA-256 em Python, **sem uso de bibliotecas externas**. A ideia é mostrar, passo a passo, como o algoritmo funciona internamente, desde o padding da mensagem até o cálculo final do hash em hexadecimal.

## Funcionalidades

- Cálculo do hash SHA-256 de uma string de entrada
- Implementação manual de:
  - Padding da mensagem (até múltiplos de 512 bits)
  - Divisão em blocos de 512 bits
  - Expansão das palavras de mensagem (64 palavras de 32 bits)
  - 64 rodadas de compressão usando:
    - Constantes K fixas do SHA-256
    - Funções de rotação e deslocamento de bits
- Saída no formato de string hexadecimal de 64 caracteres

## Estrutura do Projeto

- `sha256.py`  
  Contém:
  - As constantes do SHA-256:
    - `HASH_INICIAL`: vetor com os 8 valores iniciais do hash
    - `CONSTANTES`: 64 constantes usadas em cada rodada do algoritmo
  - A função `rotacionar_direita(valor, bits)`, que faz a rotação de bits à direita em 32 bits
  - A função `preparar_mensagem(texto)`, que:
    - Converte o texto para binário
    - Aplica o bit `1` de término
    - Preenche com `0` até chegar em 448 bits (mod 512)
    - Adiciona o tamanho original da mensagem em 64 bits
    - Retorna a lista de blocos de 512 bits
  - A função `expandir(bloco)`, que:
    - Gera as 64 palavras de 32 bits a partir do bloco original
    - Usa rotações, deslocamentos e somas módulo 2³²
  - A função principal `calcular_sha256(texto)`, que:
    - Prepara a mensagem
    - Processa cada bloco com as 64 rodadas
    - Atualiza os 8 registradores do hash
    - Retorna o resultado final em hexadecimal
  - Um bloco `if __name__ == "__main__":` que:
    - Lê uma string do teclado
    - Exibe o hash SHA-256 correspondente

## Pré-requisitos

- Python 3.x instalado

Para verificar a versão:

```bash
python --version
# ou
python3 --version
```

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo-sha256.git
cd seu-repo-sha256
```

2. Execute o script pelo terminal:

```bash
python sha256.py
# ou
python3 sha256.py
```

3. Quando solicitado, digite a mensagem que deseja hashear:

```text
Digite a mensagem para gerar o SHA-256: teste
Hash SHA-256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

*(o hash acima é apenas um exemplo; confirir com uma implementação oficial para validar testes)*

## Como Usar em Outros Códigos

Você pode importar a função `calcular_sha256` em outros scripts Python:

```python
from sha256 import calcular_sha256

mensagem = "Hello, SHA-256!"
hash_resultado = calcular_sha256(mensagem)
print(hash_resultado)
```

## Objetivo do Projeto

Este projeto foi criado com foco em:

- Entender a lógica interna do SHA-256 sem depender de bibliotecas prontas
- Servir como material de estudo para manipulação de bits, operações lógicas e funções de hash criptográfico
