import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.signal import find_peaks

# Arrays til bruk senere i koden
y = []
x = []
z = []


# Funksjon moving average som bruker numpy sin convolve funksjon
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w


# CSV leser; åpner og leser filen, og deretter setter dem i
# arrays via en for løkke
with open(r"csv(75)") as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(str(row[2]))

# Setter rawdata inn i et numpy array for brukt til moving average
arrY = np.array(y)

# Plotter verdiene fra x og y array. (k for svart, . for prikker, ms er størrelse)
plt.plot(x, y, 'k.', ms=1.5)

# Lager moving average av raw dataen via en funksjon
plt.plot(x, moving_average(arrY, 5), label='Moving average 5')
plt.plot(x, moving_average(arrY, 3), label='Moving average 3')

# Setter et tekstfelt til x-aksen og hoved y-aksen
plt.xlabel('Tid (ms)')
plt.ylabel('Spenning', color="blue")

# Viser utsnitt av målingene på y-aksen
plt.ylim([0.0085, 0.009])

# viser utsnitt av tidsmålingene
plt.xlim(10000, 20000)

# Lager en ekstra y-akse på høyresiden til temperaturmålingene
axe2 = plt.twinx()
axe2.plot(x, z, color="red", label="temp")
axe2.set_ylabel("Temperatur", color="red")

# Finner alle toppene til grafen
peaks = find_peaks(moving_average(arrY, 5))

# Tittel på diagrammet
plt.title('Fotopletysmograf')

# Regner ut hjerteslag per minutt
BPM = 'Slag per minutt: ' + str(int((len(peaks[0])) / (x[-1] / 1000) * 60))

# Setter opp en fylt, farget tekstboks
plt.text(14000, 0.2, BPM,
         bbox=dict(boxstyle="square",
                   ec=(0.015, 0.239, 0.964),
                   fc=(0.588, 0.678, 0.972),
                   )
         )

# Viser diagrammet på skjerm
plt.show()
