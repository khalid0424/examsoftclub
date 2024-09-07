tjs_amount = float(input("Қурбро ворид кунед бо TJS:  "))


rub_rate = 8.33     
usd_rate = 0.094    
eur_rate = 0.084    
uz_sum_rate = 1000  

rub_amount = tjs_amount * rub_rate
usd_amount = tjs_amount * usd_rate
eur_amount = tjs_amount * eur_rate
uz_sum_amount = tjs_amount * uz_sum_rate

print(f"Rub -> {rub_amount:.2f}")
print(f"USD -> {usd_amount:.3f}")
print(f"EUR -> {eur_amount:.3f}")
print(f"UZ_SUM -> {uz_sum_amount:.0f}")