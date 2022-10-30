def InverteFrase(frase):
    text= frase[::-1]
    return text

frase = input("Digite uma frase: ")
result = InverteFrase(frase)
print(result)