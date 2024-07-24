# Elementos e funcionalidades do site
# -> Título do site (Hashzap)
#  -> Botão para iniciar o chat
#   -> Abrir popup para entrar no chat
#    -> Após entrar no chat:
#      -exibir mensagem que entrou no chat
#      -exibir campo e botão de enviar mensagem
#     -> Ao enviar uma mensagem:
#      -exibir Nome: texto da mensagem

import flet as ft

def main(pagina):
 titulo = ft.Text("PHsapp")
 #logo = ft.Image(src=f"logo.png", width=100, height=100)
 chat = ft.Column()

 nome_usuario = ft.TextField(label="Digite seu nome")

 def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

 
 def entrar_popup(evento):
  pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
  pagina.add(chat)
  popup.open = False
  #pagina.remove(logo)
  pagina.remove(titulo)
  pagina.remove(botao_iniciar)
  pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))
  pagina.update()


 popup = ft.AlertDialog(open=False, 
    modal=True,
    title=ft.Text("Bem vindo ao PHsapp. Fique a vontade para conversar!"),
    content=nome_usuario,
    actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)])

 def entrar_chat(evento):
   pagina.overlay.append(popup) 
   popup.open = True
   pagina.update()
  
 botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

 def enviar_mensagem(evento):
   pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
   campo_mensagem.value = ""
   pagina.update()

 campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
 botao_enviar_mensagem = ft.ElevatedButton("Enviar mensagem", on_click=enviar_mensagem)
  
 
 #pagina.add(logo)
 pagina.add(titulo)
 pagina.add(botao_iniciar)

 pagina.pubsub.subscribe(enviar_mensagem_tunel)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
# Deploy do site