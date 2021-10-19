import pandas as pd
from mail import Mail

# configurações do email
username = 'gabsdocompiuter'
email    = 'gabsdocompiuter@gmail.com'
password = ''

#lê a tabela
table = pd.read_excel('vendas.xlsx')

#constantes para o cabeçalho da tabela
CODIGO = "Código Venda"
DATA = "Data"
LOJA = "ID Loja"
PRODUTO = "Produto"
QUANTIDADE = "Quantidade"
VALOR_UNITARIO = "Valor Unitário"
VALOR_TOTAL = "Valor Final"
TICKET_MEDIO = "Ticket Médio"

#faturamento por loja
faturamento = table[[LOJA, VALOR_TOTAL]].groupby(LOJA).sum()

#quantidade de vendas por loja
quantidade = table[[LOJA, QUANTIDADE]].groupby(LOJA).sum()

#ticket médio
ticket_medio = (faturamento[VALOR_TOTAL] / quantidade[QUANTIDADE]).to_frame()
ticket_medio = ticket_medio.rename(columns={0: TICKET_MEDIO})

#monta o relatório para ser enviado por email
body = f'''
<h1>Relatório</h1>

<h3>Faturamento por loja</h3>
{faturamento.to_html(formatters={VALOR_TOTAL: 'R$ {:,.2f}'.format})}

<h3>Quantidade vendas por loja</h3>
{quantidade.to_html(formatters={QUANTIDADE: '{:,.0f}'.format})}

<h3>Ticket médio</h3
{ticket_medio.to_html(formatters={TICKET_MEDIO: 'R$ {:,.2f}'.format})}
'''

#Envia o email
mail = Mail(email, username, password, 'smtp.gmail.com', 587)
mail.set_default_headers()
mail.send_mail(to='gabsdocompiuter@gmail.com', to_name='Gabriel', subject='Relatorio Vendas (python)', body=body)