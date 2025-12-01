print ("Donné une chaine de caractères : ")
s = input()
for i in range(len(s)):
    if s[i-1] == s[i+1]:
        pal = s[i-1:i+2]
        break
    

print("dans cette chaine de caractères, le palindrome est : " + pal)