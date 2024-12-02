# "pip install yfinance" 
# "pip install matplotlib"

import yfinance as yf
import matplotlib.pyplot as plt

banco_do_brasil = yf.download("BBAS3.SA",
                    start="2017-01-01",
                    end="2024-12-02",
                    progress="False")

banco_do_brasil["Close"].plot(figsize=(10,5)) 

plt.xlabel("Ano")
plt.ylabel("Valor em reais")
plt.show()
