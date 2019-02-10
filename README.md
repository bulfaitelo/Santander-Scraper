Select Language: [English](https://github.com/bulfaitelo/Santander-Scraper/blob/master/README-pt.md), **Portuguese**
========
# Santander Scraper

The scripts using Selenium extract the data from the Santander savings account, extracting the extract and the anniversary day of the application.

## Installation  

If you prefer to install by Composer: [composer](http://getcomposer.org/download/).

```
composer require bulfaitelo/santander-scraper

```
or add to the `composer.json`

```json

"bulfaitelo/santander-scraper": "^1.0",

```

## Requeriments
  

- **selenium** (`$ pip install selenium`)
 

## To use
 

Run `santander_poupanca.py` with cpf amd password, to get o extract and birthday dates.

#### Optional
You can add a third parameter, to create a print screen error, defining file path. You can define erro name on `default_file_name = 'erro.png'`

### Example

`$ python santander_poupanca.py 1234567890 pass123`

`$ python santander_poupanca.py 1234567890 pass123 c:\error\dir/`


## Return  

Return `json` with the data: 

### Extrato:  

- data
- documento
- historico
- valor_movimento
- saldo

### Birthday
- data
- valor