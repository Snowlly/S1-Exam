print("Combien de chiffres voulez-vous mettre dans la liste ? ")
s = int(input())
l = []
for i in range(s):
    print("Entrez le chiffre numéro " + str(i + 1) + " : ")
    x = int(input())
    l.append(x)
l[-1] += 1

print(str(l))
