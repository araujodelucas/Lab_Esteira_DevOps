OBSERVAÇÕES:
- Enquanto o ambiente da API não está containerizado, recomendo utilizar o sistema operacional Ubuntu 18.04, através de uma VM no Virtual BOX com o Vagrant, um container com essa distro, ou caso seja o caso, na sua própria máquina.
- Caso o SO não tenha o git instalado, execute o seguinte comando, dentro do SO do Ubuntu: sudo apt-get install git-all

1 - Instalar o pip com o python3: sudo apt install python3-venv python3-pip
Referência: https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers

2 - Instalar o virtualenv: pip3 install virtualenv

3 - Criar o diretório api e entrar nele: mkdir api && cd api

4 - Criar o virtualenv: virtualenv .venv

5 - Ativar o virtualenv: source .test/bin/activate
OBS: Caso queria sair do virtualenv, execute o seguinte comando: deactivate

6 - Instalar o Flask: pip3 install flask

7 - Instalar o jsonify: pip3 install jsonify

8 - Instalar o request: pip3 install request

9 - Criar arquivo para instalar as dependências do Flask: touch requirements.txt

10 - Escolher o editor de texto de sua preferência e inserir o seguinte conteúdo dentro do arquivo requirements.txt: flask==x.x.x
Exemplo: flask==1.1.2
OBS: A versão do flask pode ser analisada no output do comando de instalação pip install flask

11 - Inserir um novo comentário: curl -X POST -H 'Content-Type: application/json' -d '{"comentario":"COMENTARIO","usuario":"USUARIO_QUE_COMENTOU"}' localhost:5000/comentar
Exemplo: curl -X POST -H 'Content-Type: application/json' -d '{"comentario":"Reportagem show de bola","usuario":"Lucas"}' http://127.0.0.1:5000/comentar

12 - Executar o seguinte comando no bash, para consultar os comentários: curl -X GET http://127.0.0.1:5000/consultar.
OBS: Como o GET e o http é o método e protocólo padrão, respectivamente, também podemos consultar os comentários da seguinte maneira: curl 127.0.0.1:5000/consultar. Caso o comando curl não esteja instalado, execute o seguinte comando para instalá-lo: apt install curl -y