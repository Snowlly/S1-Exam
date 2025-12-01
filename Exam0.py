print("Donné une chaine de caractères : ")
s = input()
print("Le dernier mot est " + s.split()[-1] + " et sa longueur est " + str(len(s.split()[-1])))