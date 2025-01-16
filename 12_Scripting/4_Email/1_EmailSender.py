import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Matheus'
email['to'] = 'thiago.gutierrezgo@gmail.com'
email['subject'] = 'Você é um otario'

email.set_content(html.substitute({'name': 'Thiago'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mattoledo2312@gmail.com', '45265429mrt')
    smtp.send_message(email)
    print('all good')