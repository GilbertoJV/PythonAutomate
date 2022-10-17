import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr
from dotenv import load_dotenv

# take env variables from a .env file
env_variables = load_dotenv(".env")

email_receiver = 'email@example.com,email2@example.com'


email_body = """
Este es un correo automatizado.

Creado por: Gilberto JV Skirlo.

Saludos.
"""

#Add img to email
with open('Firma.png','rb') as file:
  file_data = file.read()
  file_type = imghdr.what(file.name)
  file_name = file.name

#Make email instance
em = EmailMessage()
em['From'] = os.environ['email_user']
em['To'] = email_receiver
em['Subject'] = 'Correo Automatizado 2'
em.set_content(email_body)
em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

#add ssl certificate
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp_instance:
  smtp_instance.login(os.environ['email_user'], os.environ['email_password'])
  smtp_instance.sendmail(os.environ['email_user'], email_receiver, em.as_string())