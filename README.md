* Para rodar o projeto:

```sh
make run
```

* Virtual env utilizada -> pydocker

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

* Para iniciar o service do docker:

```sh
sudo service docker start
```

* Para criar a imagem docker a partir do Dockerfile:

```sh
docker build --tag docker-python .
```

* Para rodar a aplicação via docker:

```sh
docker run --rm -p 5000:5000 docker-python
```
E no navegador:

```sh
localhost:5000/apidoc/swagger
```
