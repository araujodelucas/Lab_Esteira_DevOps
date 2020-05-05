# Case DevOps Globo.com

- O planejamento inicial era utilizar o Vagrant para gerenciar uma VM Linux Ubuntu 18.04, executando em um Hypervisor Oracle VirtualBox, onde através do Vagrantfile, estaria setado os parâmetros para fazer a camada de provisionamento e gerenciamento de configuração do ambiente com o Puppet / Ansible e Shell Script. Porém, aconteceram alguns imprevistos e não consegui terminar a tempo.
- Nesse provisionamento, seria automatizado a instalação e e configuração do: . Docker-CE: Para o Jenkins conectar no daemon do Docker Host e consiga fazer o build da imagem da API . Docker-Compose: Para subir as ferramentas dessa stack DevOps . Git: Para fazer o pull do repositório remoto no Github, e trabalhar localmente

# Subindo a Stack DevOps

- Dentro do repositório na máquina local, execute o seguinte comando: docker-compose -f api/docker-compose.yml up -d
- Para confirmar que todos os serviços estão UP, digite o seguinte comando: docker-compose -f api/docker-compose.yml ps
A sua saída deve ser como o exemplo abaixo:
Name                 Command               State                 Ports              
---------------------------------------------------------------------------------------
grafana      /run.sh                          Up      0.0.0.0:3000->3000/tcp           
jenkins      /bin/tini -- /usr/local/bi ...   Up      50000/tcp, 0.0.0.0:8080->8080/tcp
prometheus   /bin/prometheus --config.f ...   Up      0.0.0.0:9090->9090/tcp           
sonarqube    ./bin/run.sh                     Up      0.0.0.0:9000->9000/tcp

# Configurando o job no Jenkins:
- Para garantir que o Jenkins seja configurado com segurança pelo administrador, uma senha foi gravada no log e será solicitado, logo após o seu primeiro acesso no browser do seu navegador, através da url http://localhost:8080. No seu terminal, digite o comando docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword, copie a saída e cole no campo Administrator password.
- Na tela exibida, escolha a opção Install suggested plugins
- Na tela exibida, preencha os campos para criar o usuário admin > Salve e finalize
- Antes de criar o nosso job, vamos fazer algumas configurações antes
- No servidor do Jenkins, vamos criar um par de chaves para autenticar o Jenkins no GitHub, onde a chave privada deve ficar no servidor do Jenkins, e a chave pública deve ser setada no console do Github.
- Dentro da opção de Credentials, vamos criar as nossas credenciais para que o Jenkins se autentique no Github (via ssh com chave privada) e no Dockerhub (através de usuário e senha).
- Em Manage Jenkins > Manage Plugins > Available > Na barra de pesquisa, digite docker > Selecione o checkbox do plugin Docker Plugin e clique no botão para instalar e reiniciar o Jenkins após a instalação
- Após reiniciar o Jenkins e logar novamente, clique em New Item para criar o nosso job com o nome de api e o projeto do tipo Freestyle > Clique em OK
- Em Manage Jenkins > Configure System > Desça até o final da página e clique em cloud > > No campo Name, digite docker > Clique em Docker Cloud details > No campo Docker Host URI, digite tcp://127.0.0.1:2376 > Habilite o Plugin, marcando o checkbox Enable > Clique em Save
- Na aba Source Code Management, selecone Git > Em Repositories, insira a URL do repositório do Github > Em Credentials, selecione a credencial que configuramos para autenticar no Github > Mantenha a branch como master
- Na aba Build Triggers, selecione Poll SCM e informe qual a periodicidade que o job irá verificar uma nova modificação no repositório do Github. No nosso caso, informe o seguinte valor para verificar a cada minuto: * * * * *
- Na aba Build Environment, selecione Delete workspace before build starts, para evitar "sujeiras" ao fazer o build
- Na aba Build, selecione Execute Shell e informe o seguinte valor para fazer o lint do nosso Dockerfile que gera a imagem Docker da API: docker run --rm -i hadolint/hadolint < ./api/Dockerfile
- Na mesma aba, selecione Build / Publish Docker Image > Informe no Directory for Dockerfile, o valor: ./api > Cloud: docker > Image: lucasdearaujo1/api_comentarios:v1 > Marque o checkbox Push Image > Selecione a credencial que definimos para autenticar no Dockerhub > Clique em Apply e Save
- Realize o Build da imagem e publique no Dockerhub, clicando em Build Now
- Em Build History, você pode acompoanhar o output da execução do build. Caso tenha sido feito com sucesso, a seguinte mensagem será exibida no final do console de output, Finished: SUCCESS
