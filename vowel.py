a=input()
yy="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
xx="AEIOUaeiou"
if a in xx:
  print("Vowel")
elif a in yy:
  print("Consonant")
else:
  print("invalid")     
