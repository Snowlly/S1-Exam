print("Donné un chiffre romain : ")
s = input()
Ceuro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
t = 0
i = 0
while i < len(s):
    if i + 1 < len(s) and Ceuro[s[i]] < Ceuro[s[i + 1]]:
        t += Ceuro[s[i + 1]] - Ceuro[s[i]]
        i += 2
    else:
        t += Ceuro[s[i]]
        i += 1
print(str(t))
