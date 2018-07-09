
def decrypt(word):
  result = [0] * len(word)
  temp  = 1
  for i in range(len(word)):
    result[i] = ord(word[i]) - temp
    while (result[i] < 97):
       result[i] = result[i] + 26
    temp = result[i] + temp
    result[i] = chr(result[i])
   
  return ''.join(result)



word = "dnotq"
print(decrypt(word))

word = "flgxswdliefy"
print(decrypt(word))
#time o(n)
#space o(n)


       
