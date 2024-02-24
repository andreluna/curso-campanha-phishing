
# Curso - Campanha de Phishing com GoPhish

* Criação de um servidor EC2 na AWS.
* Configuração de DNS com HTTPS.
* Configuração de serviço de disparo de e-mails.
* Instalação de Configuração do GoPhish.
* Documentação com tutorial para utilização de vários domínios em campanhas.
    - Instalação e configuração da ferramenta Caddy

https://www.udemy.com/course/campanha-de-phishing-com-gophish-aws-email-gophish/

<hr>

### Scripts

#### Instalação do Apache2

```
#!/bin/bash

# Curso Campanha de Phishing - 2023

# Atualização dos repositórios
sudo apt-get update
# sudo apt upgrade -y

# Instalação do apache2 
apt install apache2 unzip -y

# Alterando a página padrão do Apache2
rm /var/www/html/index.html
echo '[error_page]' > /var/www/html/index.html
chown www-data:www-data -R /var/www/html/

# Reload das configurações do Apache2
systemctl reload apache2

# Parando o apache2
# systemctl stop apache2

# Iniciando o apache2
#systemctl start apache2
```

#### Instalação do CertBot (Let`s Encrypt)

```
#!/bin/bash

# Instalação do Certbot e Python3-certbot-apache
apt install certbot python3-certbot-apache -y

# Instruções para emitir o certificado:
# Lembre-se de configurar no DNS para que a entrada do tipo "A" aponte para o IP Público do seu servidor.

# DOMAIN="domain.com.br"
# EMAIL="email@gmail.com"

# certbot -n --apache -d www.$DOMAIN --agree-tos --email $EMAIL --no-eff-email --hsts --redirect

# Comando para renovar o certificado pelo Certbot:
# certbot renew

# Caminho onde os arquivos do certificado estão localizados:

# /etc/letsencrypt/live/domain.com.br/fullchain.pem
# /etc/letsencrypt/live/domain.com.br/privkey.pem
```

#### Instalação do GoPhish

```
#!/bin/bash

# Instalação do Gophish

# Download GoPhish

# https://getgophish.com/
# https://github.com/gophish/gophish/releases/
# https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip

# Criando do diretório /opt/gophish :
mkdir /opt/gophish

# Download da última versão do GoPhish:
wget https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip -O /opt/gophish/gophish-v0.12.1-linux-64bit.zip 

# Descompactando os arquivos do GoPhish:
unzip /opt/gophish/gophish-v0.12.1-linux-64bit.zip -d /opt/gophish

# Alterando a permissão do arquivo para permitir que seja executádo:
cd /opt/gophish
chmod +x gophish

# Comando para rodar o GoPhish. 
# Tenha certeza que o Apache2 está desligado.
# Após iniciar o GoPhish, ele vai informar o login e senha para acesso.

# ./gophish 
```

#### Instalação do Caddy (apenas para utilização com vários domínios)

**Para mais informações, veja o conteúdo da pasta ```multiplos_dominios```**

```
#!/bin/bash

apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
apt update
apt install caddy

```