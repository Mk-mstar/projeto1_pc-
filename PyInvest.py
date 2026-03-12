import math
import random
import datetime
import locale
import statistics

locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')

#Entrada
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = int(input('Prazo em meses: '))
cdi_anual = float(input('Cdi Anual(%): '))/100
perc_cdb = float(input('Percetual CDI (%): '))/100
perc_lci = float(input('Percetual LCI (%): '))/100
taxa_fii = float(input('Rentabilidade mensal FII (%): '))/100
Meta = float(input('Projeção financeira (R$): '))

#Processamento
cdi_mensal = math.pow(1 + cdi_anual, 1/12) - 1

#Total investido 
total_inv = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow(1 + taxa_cdb, meses ) + (aporte * meses))
lucro_cdb = montante_cdb - total_inv
montante_cdb_liquido = total_inv + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses)) 

#Poupança
taxa_poup = 0.005 
montante_poup = capital * (1 + taxa_poup) ** meses

#FII - Simulações
variacao =  random.uniform(-3, 3) 
variacao2 =  random.uniform(-3, 3) 
variacao3 =  random.uniform(-3, 3) 
variacao4 =  random.uniform(-3, 3) 
variacao5 =  random.uniform(-3, 3) 
fii1 = capital * (1 + variacao)
fii2 = capital * (1 + variacao2)
fii3 = capital * (1 + variacao3)
fii4 = capital * (1 + variacao4)
fii5 = capital * (1 + variacao5)

#Formação Mónetaria
media = statistics.mean([fii1, fii2, fii3, fii4, fii5])
desvio_padrao = statistics.stdev([fii1, fii2, fii3, fii4, fii5])
valores = [fii1, fii2, fii3, fii4, fii5]
mediana = statistics.median(valores)

#Data Resgate
data_compra = datetime.datetime.strptime(input('Data de compra (dd/mm/yyyy): '), '%d/%m/%Y')
resgate = data_compra + datetime.timedelta(days = meses)

#Saídas

print (f'Data da simulação: {datetime.datetime.now().strftime("%d/%m/%Y")}')
print (f'Resgate previsto para: {resgate.strftime("%d/%m/%Y")}')
print(f'Total investido: { total_inv:.0f}') 

print(f'CDB: R$ {montante_cdb:.2f}') 
print("CDB:", "█" * int(montante_cdb / 1000))

print(f'LCI: R$ {montante_lci:.2f}') 
print("LCI/LCA:", "█" * int(montante_lci / 1000))

print(f'Poupança: R$ {montante_poup:.2f}') 
print("Poupança:", "█" * int(montante_poup / 1000))

print(f'FII: R$ {media:.2f}') 
print("FII:", "█" * int(media / 1000))

print(f'Mediana FII R$ {mediana:.2f}')
print(f'Desvio Padrão FII: {desvio_padrao:.2f}')

meta_batida = mediana >= Meta
print(f"Meta batida: {meta_batida}")