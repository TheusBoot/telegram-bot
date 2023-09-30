# Telegram BOT 1.0

##Instalando as bibliotecas necessárias!
```python3
pip install telethon
```
***

## Aplicando os Imports Necessários

```python3
from telethon import TelegramClient, sync, events
from time import sleep
import requests
import asyncio
```
***
## Inicializando o projeto
```python3
projec = Projeto(api_hash = "1212121",
	api_id = 222011,
	sessao = 'Nova',
	id_canal_copiado = 102010201,
	id_canal_recepetor = 1921012)

projec.comercial(mensagem='OLÁ PESSOAL!')
projec.comercial(mensagem='tudo bem com todos ?')

projec.inicializador()
```
