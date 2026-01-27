# Exercício: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de cada parcela é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta


valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
data_final = datetime(2025, 12, 20)

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final: # laço vai usar a data inicial e "andar" de mês em mês e colocar a cada dia vinte dentro do array data_parcela.
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
# OBS: também funciona sem a data_parcela, usar só a data_emprestimo funciona igualm, mas o código fica pior de ler

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas
print(valor_total)
print(len(data_parcelas))

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'até {data_final.year} '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)