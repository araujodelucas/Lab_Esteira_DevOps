#Case DevOps Globo.com
- O planejamento inicial era utilizar o Vagrant para gerenciar uma VM Linux Ubuntu 18.04, executando em um Hypervisor Oracle VirtualBox, onde através do Vagrantfile, estaria setado os parâmetros para fazer a camada de provisionamento e gerenciamento de configuração do ambiente com o Puppet / Ansible e Shell Script. Porém, aconteceram alguns imprevistos e não consegui terminar a tempo.
- Nesse provisionamento, seria automatizado a instalação e e configuração do:
. Docker-CE: Para o Jenkins conectar no daemon do Docker Host e consiga fazer o build da imagem da API
. Docker-Compose: Para subir as ferramentas dessa stack DevOps
. Git: Para fazer o pull do repositório remoto no Github, e trabalhar localmente

- Subindo a Stack DevOps
1 - Dentro do repositório na máquina local, execute o seguinte comando: docker-compose -f api/docker-compose.yml up -d

- Configurando o job no Jenkins: 
1- No servidor do Jenkins, vamos criar um par de chaves para autenticar o Jenkins no GitHub, onde a chave privada deve ficar no servidor do Jenkins, e a chave pública deve ser setada no console do Github.
2- Dentro da opção de Credentials, vamos criar as nossas credenciais para que o Jenkins se autentique no Github (via ssh com chave provada) e no Dockerhub (através de usuário e senha).  
3- Em Manage Jenkins > Manage Plugins > Available > Na barra de pesquisa, digite docker > Selecione o checkbox do plugin Docker Plugin e clique no botão para instalar e reiniciar o Jenkins após a instalação
4- Clique em New Item para criar um job com o nome de api e o projeto do tipo Freestyle > Clique em OK
5- Na aba Source Code Management, selecone Git > Em Repositories, insira a URL git@github.com:SelecaoGlobocom/lucas-de-araujo.git > Em Credentials, selecione a credencial que configuramos para autenticar no Github > Mantenha a branch como master
6- Na aba Build Triggers, selecione Poll SCM e informe qual a periodicidade que o job irá verificar uma nova modificação no repositório do Github. No nosso caso, informe o seguinte valor para verificar a cada minuto: * * * * * 
7- Na aba Build Environment, selecione Delete workspace before build starts, para evitar "sujeiras" ao fazer o build
8- Na aba Build, selecione Execute Shell e informe o seguinte valor para fazer o lint do nosso Dockerfile que gera a imagem da API: docker run --rm -i hadolint/hadolint < ./api/Dockerfile
9- Na mesma aba, selecione Build / Publish Docker Image > Informe no Directory for Dockerfile, o valor ./api > Cloud, docker > Image, lucasdearaujo1/api_comentarios:v1 > Marque o checkbox Push Image > Selecione a credencial que definimos para autenticar no Dockerhub > Clique em Apply e Save
10- Realize o Build da imagem e publique no Dockerhub, clicando em Build Now
11- Em Build History, você pode acompoanhar o output da execução do build. Caso tenha sido feito com sucesso, a seguinte mensagem será exibida no final do console de output, Finished: SUCCESS
