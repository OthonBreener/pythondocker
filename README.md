## Rodando o projeto
* Para rodar o projeto:

```sh
make run
```

## Rodando o projeto através do docker

* Para iniciar o service do docker:

```sh
sudo service docker start
```

* Para criar a imagem docker a partir do Dockerfile:

```sh
docker build --tag docker-python .
```

* Para rodar a aplicação via docker e parear a porta 5000 do host com a porta 5000 da aplicação:

```sh
docker run --rm -p 5000:5000 docker-python
```
Ou, utilizando o -d para rodar a aplicação em background

```sh
docker run -p 5000:5000 -d docker-python

```
E no navegador:

```sh
localhost:5000/apidoc/swagger
```

* Adicionando a imagem do MySQL:

```sh
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=senha -d mysql:latest
```

* Podemos adicionar um volume, onde os dados do banco de dados podem ficar salvos mesmo se o container docker for deletado:

```sh
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=senha -p 3306:3306 -v mysqlVolume:/var/lib/mysql -d mysql:latest
```

* Para adicionar o arquivo do banco de dados no container docker:

```sh
docker exec -i id_do_container  mysql -u root -psenha <./schema.sql
```
## Ambientes virtuais

* Virtual env utilizada com o conda -> pydocker

* Configurando o ambiente virtual com pyenv:

1. pip install virtualenv
2. sudo apt-get install python3-venv
3. virtualenv -p python3 venv
4. . venv/bin/activate

## Informações

* Comando para criar um requirements com as versões das bibliotecas utilizadas:

```sh

pip freeze > requirements.txt
```

* Para acessar a documentação do swagger basta jogar no navegador: localhost/apidoc/swagger

* Biblioteca pre-commit foi utilizada para configurar o requirements para ser atualizado
sempre que um commit for feito. Passos para usar:

1. pre-commit install
3. git add .
2. git commit -m "Algum commit"
