import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

archivo = 'parte.wav'
muestreo, sonido = waves.read(archivo)

tamano = np.shape(sonido)
muestras = tamano[0]
m = len(tamano)
canales = 1  # monofónico

if (m > 1):  # estéreo
    canales = tamano[1]
# experimento con un canal
if (canales > 1):
    canal = 0
    uncanal = sonido[:,canal] 
else:
    uncanal = sonido

inicia = 1.600
termina = 6.002

a = int(inicia*muestreo)
b = int(termina*muestreo)
parte = uncanal[a:b]

waves.write('salida.wav', muestreo, parte)

y = 100

dt = 1/muestreo
ta = a*dt
tb = (b-1)*dt
tab = np.arange(ta,tb,dt)
vals = []
bandera = False
for i, t in enumerate(parte):
    if t < y and t > -y:
        if (not bandera):
            vals.append(tab[i])
            bandera = True
    else:
        if (bandera and tab[i]-vals[-1] > 0.05):
            vals.append(tab[i])
            bandera = False
print(vals)

plt.figure(figsize=(50,30))
plt.plot(tab, parte)
plt.xlabel('tiempo (s)')
plt.ylabel('Amplitud')
plt.xticks(np.arange(1,6.2,0.1))

plt.grid(True)
#plt.savefig("img.png")