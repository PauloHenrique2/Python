votaram = {}

votaram["Tom"] = True 

def verifica_eleitor(nome):
 if votaram.get(nome):
  print ("Vaza meu fi")
 else:
  votaram[nome] = True
  print ("Pode votar")

print (verifica_eleitor("Tom"))