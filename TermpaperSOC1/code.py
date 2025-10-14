import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dp = 'TermpaperSOC1/Dataset_termpaper_soc1.xlsx'

p = pd.read_excel(dp)

#plt.plot(p['Year'], p["UnemploymentEU"])
plt.plot(p['Year'],p["GDPpercapitaEstonia"], c="red", label="Estonia")

plt.title("GDP per capita in Estonia")

plt.axhline(0, c='black', lw=0.5, ls='--')
plt.grid()
plt.xlabel("Year")
plt.ylabel("GDP per capita")

plt.legend(loc="lower right") 
plt.show()