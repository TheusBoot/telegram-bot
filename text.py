#pip install teletom

from telethon import TelegramClient, sync, events
from time import sleep
import requests
import asyncio
#from  senhas import api_hash,api_id

#sessao = 'repassar mensagem'


def obter_chats():
	client = TelegramClient(sessao, api_id, api_hash)
	client.start()
	dialogs = client.get_dialogs()
	for dialog in dialogs:
		print('--------------------------------')
		if dialog.id < 0:
			print(f'Grupo: {dialog.title}')
			print(f'id: {dialog.id}')
		#else:
		#	print(f'Nome: {dialog.title}')
		#	print(f'id: {dialog.id}')

		print('--------------------------------')

	client.disconnect()

#obter_chats()

class Projeto:

	def __init__(self,api_hash,api_id,sessao,id_canal_copiado):
		
		self.api_hash = api_hash  #representação do HASH: "e4acdae0fs20aa3b9dff53f953absd61d3a14"
		self.api_id = api_id #representação do ID: 58721501
		self.sessao = sessao #representação do ID: secao nova
		self.id_canal_copiado = id_canal_copiado # id do canal copiado
		
		self.client = TelegramClient(self.sessao,self.api_id,self.api_hash)

	
	def main(self):
		print('chat 1') #identificando o chat
		@self.client.on(events.NewMessage(chats=[1001515706428])) # aqui vai o chat que o bot vai ficar pegando info
		async def enviar_mensagem(event):
			if event.message.video or (event.message.photo):
				await self.client.send_message(1001954230141,event.message)



	def chat_2(self):
		print('chat 2') #identificando o chat
		@self.client.on(events.NewMessage(chats=[1001538470927]))
		async def enviar_mensagem(event):

			if event.message.video or (event.message.photo):
				await self.client.send_message(1001954230141,event.message)


	def comercial(self):
		print('chat 3') #identificando o chat
		mensagem = """MENSAGEM DE COMERCIAL !"""

		@self.client.on(events.NewMessage)
		async def enviar_mensagem(event):
			await asyncio.sleep(50)
			await self.client.send_message(1001954230141,mensagem)
					

	def inicializador(self):
		self.main()
		self.chat_2()
		self.comercial()
		self.client.start()
		self.client.run_until_disconnected()
 






projec = Projeto()

projec.inicializador()








