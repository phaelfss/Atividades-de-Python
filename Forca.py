import random

def escolher_palavra():
    palavras = ['desenvolvimento', 'tecnologia', 'programacao', 'tendencias', 'codigo', 'aprendizado']
    return random.choice(palavras)

def exibir_forca(tentativas):
    forca = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
    print(forca[tentativas])
    
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra oculta. Boa sorte!")

    exibir_forca(tentativas)
    print(' '.join(palavra_oculta))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Voce ja tentou essa letra. Tente outra..")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1

        exibir_forca(tentativas)
        print(' '.join(palavra_oculta))

        if ''.join(palavra_oculta) == palavra:
            print("Parabens! Voce adivinhou a palavra correta:", palavra)
            break
        elif tentativas == 6:
            print("Voce perdeu! A palavra correta era:", palavra)
            break

    print("Obrigado por jogar!")

jogar()