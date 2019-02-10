Select Language: [English](https://github.com/bulfaitelo/Santander-Scraper/blob/master/README.md), **Portuguese**
========
# Santander Scraper

Os scripts com uso de Selenium, extraem os dados da poupansa do Santander, extraindo o extrato eo dia de aniversário da aplicação.

## Instalação  

Caso prefira instalar pelo Composer: [composer](http://getcomposer.org/download/).

Rode o comando? 

```
composer require bulfaitelo/santander-scraper

```
ou adicione ao `composer.json`

```json

"bulfaitelo/santander-scraper": "^1.0",

```

## Requerimentos
  

- **selenium** (`$ pip install selenium`)
 

## Para Usar
 

Execute o `santander_poupanca.py` com cpf e senha, para pegar o extrato e os dias de aniversário.

#### Opicional
Você pode adicionar um terceiro paraletro para que seja criado um printscrenn do erro (caso ocorra) basta passa como terceiri parametro o caminho de onde queria que seja salvo o erro. Você pode definir o nome do erro na da variavel :`default_file_name = 'erro.png'`

### Exemplo

`$ python santander_poupanca.py 1234567890 pass123`

`$ python santander_poupanca.py 1234567890 pass123 c:\error\dir/`


## Retorno  

Retorna o `json` com os seguintes dados:

### Extrato:  

- data
- documento
- historico
- valor_movimento
- saldo

### Aniversário
- data
- valor