import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_server = 'smtp.sendgrid.net' 
port = 587  
sender_email = 'qualquer-coisa@meudominio.com.br'  # Seu endereço de e-mail

# apikey token criado conforme documentação:
# https://docs.sendgrid.com/for-developers/sending-email/integrating-with-the-smtp-api
apikey_password = ''  # Seu token da apikey no SendGrid
apikey_username = 'apikey' # Username criado para a API 


# Destinatário
receiver_email = 'meu-email@gmail.com'

# Criando o objeto da mensagem
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Teste de e-mail via SMTP e SendGrid'

# Corpo da mensagem
body = 'Este é um e-mail de teste enviado via SMTP pela plataforma SendGrid'
message.attach(MIMEText(body, 'plain'))

# Estabelecendo conexão segura com o servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    # Autenticando
    server.login(apikey_username, apikey_password)
    # Enviando e-mail
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
finally:
    # Fechando a conexão com o servidor SMTP
    server.quit()
