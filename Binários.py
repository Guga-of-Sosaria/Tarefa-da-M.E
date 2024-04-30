import emoji

print(emoji.emojize(":rosto_de_nerd: CONVERSOR DE BINÁRIOS :rosto_de_nerd:", language='pt'), end="\n\n")
num = str
while True:
    flag_letra = False
    num = input("Digite um número: ")
    for i in range(0, len(num) - 1):
        if not num[i].isnumeric():
            flag_letra = True
    if flag_letra:
        print(emoji.emojize("EU DISSE NÚMEROS E NÃO LETRAS SEU IMBECIL! :rosto_furioso:", language='pt'))
    else:
        break
num_bin = str(bin(int(num)))
print(f"{num} em binário é {num_bin}")
print(emoji.emojize("Obrigado por usar o programa! :rosto_sorridente:", language='pt'))
