cache = {}
dadosBD = "SELECT idUsuario, senha FROM Usuarios"

def pega_dados_do_servidor():
 return dadosBD

def pega_pagina(url):
 if cache.get(url):
  return cache[url]
 else:
  dados = pega_dados_do_servidor(url)
  cache[url] = dados
  return dados