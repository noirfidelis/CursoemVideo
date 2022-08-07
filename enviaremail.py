import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = 'luansantos1950@hotmail.com'
email.Subject = 'E-mail automático do Python'
email.HTMLBody = """
<p>Olá, Mundo</p>
"""

email.Send()
print('Email Enviado')