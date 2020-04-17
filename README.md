# Topologia
Os dois subprojetos aqui sao compostos de conteiners com docker e estao dispostos da seguinte forma:

 ### brprev_cli
 - ##### **brprev_cli**
   conteiner onde sera rodado o comando de busca
 - ##### **brprec_cli_worker**
   worker responsavel por disparar uma request para *brprev_bot*

 ### brprev_bot
 - ##### **brprev_bot**
   Aplicação Flask que recebe chamada de *brpre_worker*
 - ##### **brprev_bot_worker**
   worker que envia as mensagens repassadas pelo *brprev_bot* e pelo *brprev_bot_beat*
 - ##### **brprev_bot_beat**
   Envia a tarefa de buscar novas mensagens no telegram

 # Ferramentas Usadas:
 
- Python (Obviamente)
 - Flask
 - Celery
 - SqlAlchemy
 - MongoDB
 - Docker
 - Redis (Broker)
 - Poetry
 - Gunicorn
 - pyTelegramBotAPI


 # Notas de Desenvolvimento:
 - Escolhi usar um celery-beat ao inves de fazer polling continuamente na aplicação, entao o *brprev_bot_beat* envia a cada 10 segundos para o *brprev_bot_worker*
 - Optei por usar celery para dar uma resposta mais rapida pro usuário da CLI enquanto as resquests sao enviadas ao chat do telegram e também pelo item anterior
- Este projeto foi feito com a ajuda de um cookiecutter de minha autoria: o
[flask-rest-cookiecutter](https://github.com/jedi-vim/flask-rest-cookiecutter)
- Nao Consegui resolver a questaõ de criação do banco de dados do *brprev_bot*, tentei usar um comando no poetry e click e sem sucesso (resolvo futuramente), o *brprev_bot_worker* vai ficar quebrando quando o bot receber uma mensagem e o worker nao conseguir salvar por que o BD nao tem tabelas
- Desenvolvi um decorator (brprev_bot.decorators) para que as tasks do celery possam ter um contexto pushado do flask mas aparentemente nao funcionou, no envio da msg mesmo com 9 chats cadastrados nao era enviada msg nenhum para mim no telegram
 
 # Observações
 - Tive problemas durante o desenvolvimento que me atrasaram, mas nao me fizeram desistir do desenho que eu tinha imaginado, mas me fizeram perder tempo que poderiam ser usados para escrever testes para esse projeto

 # Como Rodar o projeto
Sugiro usar o [**Terminator**](https://terminator-gtk3.readthedocs.io/en/latest/) para assim poderes visualizar em casa janela/projeto o que vai acontecendo

 ```sh
 # Essa rede é por onde o brprev_cli_worker enxerga brprev_bot
 $ docker network create brprev_network

 # Rodando cada projeto individualmente
 $ cd brprev_cli
 $ make build
 $ make run

 $ cd brprev_bot
 $ make build
 $ make run

 # Depois para executar a busca no stackoverflow
 $ cd brprev_cli
 $ make prompt
 $ $HOME/.poetry/bin/poetry run ask_for "Sua Pergunta"
```


