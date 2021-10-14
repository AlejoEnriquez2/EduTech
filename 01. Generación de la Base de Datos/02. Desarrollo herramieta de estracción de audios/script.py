import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from pydub import AudioSegment

path = 'C:/Users/domer/OneDrive/UPS/ERASMUS/EduTech/01. Generación de la Base de Datos/02. Desarrollo herramieta de estracción de audios/extraer/'
archivo = path + 'resultado.wav'
muestreo, sonido = waves.read(archivo)

tamano = np.shape(sonido)
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

inicia = 0
termina = 59

a = int(inicia*muestreo)
b = int(termina*muestreo)
amplitud = uncanal[a:b]
#amplitud = abs(amplitud)

y = 50
t_min = 10
dt = 1/muestreo
ta = a*dt
tb = (b)*dt
tiempo = np.arange(ta,tb,dt)
vals = []
inicio = 0
grabando = False

"""
plt.figure(figsize=(80,30))
plt.plot(tiempo, amplitud)
plt.xlabel('tiempo (s)')
plt.ylabel('Amplitud')
plt.xticks(np.arange(inicia,termina,0.1))
#plt.yticks(np.arange(-1000, 1000, 100))

plt.grid(True)
"""
silencio = 0

for i, t in enumerate(amplitud):
    if (t > y or t < -y):
        if grabando and silencio != 0:
            if tiempo[i] - silencio >= 0.1:
                grabando = False
                fin = (tiempo[i] + silencio) / 2
                tupla = (inicio, fin)
                print(tupla)
                vals.append(tupla)
                silencio = 0
#                plt.axvline(x = fin, color = 'r', label = 'axvline - full height')
            else:
                silencio = 0
        elif not grabando:
            grabando = True
            inicio = tiempo[i]
        
    if grabando and tiempo[i]-inicio>=t_min:
        m = (amplitud[i]-amplitud[i-1])/(tiempo[i]-tiempo[i-1])
#        print(m)
        if (m < 0.1 and m > -0.1) and (t < y and t > -y):
            if silencio == 0:
                silencio = tiempo[i]
            
            
#plt.savefig(path+"img.png")

for i, val in enumerate(vals):
    newAudio = AudioSegment.from_wav(archivo)
    newAudio = newAudio[val[0]*1000:val[1]*1000]
    name = path+'audios/'+str(i)+'.wav'
    newAudio.export(name, format="wav")