import wave
import numpy as np
import matplotlib.pyplot as plt

cat = wave.open('cat.wav', 'r')
water = wave.open('water.wav', 'r')

framesCat = cat.readframes(-1)
framesWater = water.readframes(-1)
ondaconvertidaCat = np.frombuffer(framesCat, dtype='int16')
ondaconvertidaWater = np.frombuffer(framesWater, dtype='int16')

#print(frames[:10])

framerate_cat = cat.getframerate()
print (framerate_cat)
time_cat = np.linspace(start=0, stop=len(ondaconvertidaCat)/framerate_cat, num=len(ondaconvertidaCat))
print(time_cat[:10])

framerate_water = water.getframerate()
print (framerate_water)
time_water = np.linspace(start=0, stop=len(ondaconvertidaWater)/framerate_water, num=len(ondaconvertidaWater))
print(time_water[:10])

plt.title('cat vs water')

plt.xlabel('Tiempo (segundos')
plt.ylabel('Amplitud')

plt.plot(time_cat, ondaconvertidaCat, label='cat')
plt.plot(time_water, ondaconvertidaWater, label='water', alpha=0.5)

plt.legend()
plt.show()