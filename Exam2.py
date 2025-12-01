print("Donné une chaine de caractères : ")
s = input()
t = 0
for i in range(len(s) - 1):
    t += abs(ord(s[i]) - ord(s[i + 1]))
print(t)
