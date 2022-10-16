import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

env_variables = load_dotenv(".env")

password_email = os.environ['email_password']
email_receiver = 'giljv@stbcaps.com'

email_body = """
Este es un correo automatizado.

Creado por: Gilberto JV Skirlo.

Saludos.
"""

em = EmailMessage()
em['From'] = os.environ['email_user']
em['To'] = 'giljv@stbcaps.com'
em['Subject'] = email_receiver
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp_instance:
  smtp_instance.login(os.environ['email_user'], os.environ['email_password'])
  smtp_instance.sendmail(os.environ['email_user'], email_receiver, em.as_string())