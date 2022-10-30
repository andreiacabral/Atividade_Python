# --coding:latin1--
from datetime import date
current_date = date.today()
data_nascimento= int(input("Qual é o ano de seu nascimento: "))
data_corrente = current_date.year
idade =data_corrente-data_nascimento
mes = idade * 12
dias = idade * 365

print(idade,"idade em ano(s)")
print(mes,"idade em Meses" )
print (dias,"idade em Dias")

