import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc402e413fa0ecc42c80536de6a7feb7c"
# Your Auth Token from twilio.com/console
auth_token  = "f99aadf7041f6f65cb6a1b98c2a222a6"

client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000) .any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'] .values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'] .values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}. Vendas: {vendas}')
        message = client.messages.create(
            to="+5532984026220",
            from_="+12192717943",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}. Vendas: {vendas}')
        print(message.sid)
# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor



