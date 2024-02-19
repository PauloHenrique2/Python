votaram = {}

votaram["Tom"] = True
votaram["Jerry"] = True

def verifica_eleitor(nome):
 if nome in votaram:
  return 0
 else:
  return 1

def insere_eleitor(nome):
 if verifica_eleitor(nome) != 1:
  print ("Eleitor já cadastrado!")
 else:
  votaram[nome] = True

insere_eleitor("Jerry")

print (votaram)
