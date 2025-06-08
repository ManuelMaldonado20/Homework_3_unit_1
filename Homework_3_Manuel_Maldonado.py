import numpy as np
import matplotlib.pyplot as plt

# Parámetros predefinidos
A = 2      # Amplitud
f = 5      # Frecuencia en Hz
phi = 0    # Fase en radianes
Ts = 0.01  # Período de muestreo
n = np.arange(0, 1, Ts)  # Generar muestras en el intervalo de 1 segundo

# Señal modificada con parámetros predefinidos
x_mod = A * np.sin(2 * np.pi * f * n + phi)

# Señal de referencia con A=1, f=1 Hz, phi=0
x_ref = np.sin(2 * np.pi * 1 * n)

# Graficar señales
plt.figure(figsize=(10, 5))
plt.plot(n, x_mod, label="Señal modificada", color="b")
plt.plot(n, x_ref, linestyle="dashed", label="Señal de referencia", color="r")

plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señales en tiempo discreto")
plt.legend()
plt.grid()
plt.show()
