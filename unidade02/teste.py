parcela = float(input("DIGITE VALOR DA MENSALIDADE: R$ "))
atraso = float(input("DIGITE DIAS DE ATRASO "))

dia = 2
mes = 5
ano = 10

desc = 10
acres = atraso

if atraso <= 0:
    valor = parcela - (parcela * desc/100)

elif atraso >= 367:
    valor = valor = parcela + (parcela * ano/100) * acres

elif atraso >= 32:
    valor = valor = parcela + (parcela * mes/100) * acres

elif atraso >= 31:
    valor = valor = parcela + (parcela * dia/100) * acres

else:
    valor = parcela

print(atraso)



print(f"VALOR DA PARCELA R$ {valor:.2f}")
print(f"JUROS DIARIO {dia:.2f} %")
print(f"JUROS MENSAL {mes:.2f} %")
print(f"JUROS ANUAL {ano:.2f} %")
print(f"PAGAMENTO ANTECIPADO DESC {desc:.2f} %")

print(f"ATRASO DE {atraso} DIAS")

print(f"VALOR TOTAL DA PARCELA R$ {valor:.2f}")