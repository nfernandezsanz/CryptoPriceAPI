from nltk.book   import *
from nltk        import re


moby = text1.tokens

moby_tokens = [word.lower() for word in moby if re.search("\w", word)]

mb_to   = len(moby_tokens)
mb_ty   = len(set(moby_tokens))
mb_tyto = round(mb_ty / mb_to,3)

print("Tokens de Moby Dick:", mb_to)
print("Types  de Moby Dick:", mb_ty)
print("Moby dick type-token ratio", mb_tyto)


WSJ = text7.tokens
wsj_tokens = [word.lower() for word in WSJ if re.search("\w", word)]
wsj_to   = len(wsj_tokens)
wsj_ty   = len(set(wsj_tokens))
wsj_tyto = round(wsj_ty / wsj_to,3)

print("Tokens de Wall Street Jorunal:", wsj_to)
print("Types  de Wall Street Jorunal:", wsj_ty)
print("Wall Street Jorunal type-token ratio", wsj_tyto)

if(wsj_tyto > mb_tyto):
    print("Wall Street Journal tiene mas diversidad lexica..")
else:
    print("Moby dick tiene mas diversidad lexica..")


mb_whale  = moby_tokens.count('whale')
wsj_whale = wsj_tokens.count("whale")

print(f"MLE de 'whale' en Moby Dick es de {round(mb_whale * 100 / mb_to,2)}% ")
print(f"MLE de 'whale' en Wall Streer Journal es de {round(wsj_whale * 100 / wsj_to,2)}%",)