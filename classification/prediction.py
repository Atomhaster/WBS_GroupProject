import tensorflow as tf
import numpy as np
from tensorflow import keras

# wird eingesetzt, wenn Layer sequenziell hinzugefügt werden. Dabei spielt die Reihenfolge eine entscheidene Rolle
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])


# Mit Hilfe von "compile" werden die Ergebnisse der vorangegangen Layers zusammengestellt
# Der optimizer findet die perfekte Gewichte bis keine numerische Verbresserung mehr erzielt wird
# D.h er könnte ausgelassen werden, wenn die zu prüfenden Daten klar getrennt sind
# Loss kündigt Fehler an
model.compile(optimizer='sgd', loss='mean_squared_error')

# y = 3x + 1
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Das Modell wird hier mit Daten gefüttert! 
model.fit(xs, ys, epochs=500)

# Hier wird eine Prognose abgegeben 
print(model.predict([5.0]))


