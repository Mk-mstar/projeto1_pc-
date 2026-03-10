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
cdi_mensal =  math.pow((1+cdi_anual, 1/12) ) -1 

#Total investido 
total_inv = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb =( (capital * math.pow(1 + taxa_cdb), meses ) + (aporte * meses))
lucro_cdb = montante_cdb - total_inv
montante_cdb_liquido = total_inv + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses)) 

#Poupança
taxa_poup = 0.005 
montante_poup = ( capital * math.pow((1 + taxa_poup), meses + (aporte * meses)) )

#FII - Simulações

