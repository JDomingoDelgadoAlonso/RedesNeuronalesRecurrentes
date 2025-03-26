import yfinance as yf
import pandas as pd

# Descargar los datos históricos de TTWO
ticker = "TTWO"
data = yf.download(ticker, start="1997-04-15", end="2025-03-26")

# Guardar el CSV con encabezados limpios
data.reset_index(inplace=True)  # Asegura que la fecha esté como columna y no como índice
data.to_csv("TTWO_historical_data.csv", index=False)

print("Datos descargados y guardados en TTWO_historical_data.csv")