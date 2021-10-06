# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import pickle

pickle_in = open("raspberrypi/X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("raspberrypi/y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0

model=tf.keras.models.Sequential([
                                tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(150,150,1)),
                                tf.keras.layers.MaxPool2D(2,2),

                                tf.keras.layers.Conv2D(128,(3,3),activation='relu'),
                                tf.keras.layers.MaxPool2D(2,2), 

                                tf.keras.layers.Conv2D(128,(3,3),activation='relu'),
                                tf.keras.layers.MaxPool2D(2,2), 
                                
                                tf.keras.layers.Conv2D(256,(3,3),activation='relu'),
                                tf.keras.layers.MaxPool2D(2,2), 

                                tf.keras.layers.Flatten(),
                                tf.keras.layers.Dense(128,activation='relu'),
                                tf.keras.layers.Dense(128,activation='relu'),
                                tf.keras.layers.Dense(1,activation='sigmoid'),
                                
])

print(model.summary())
model.compile(loss='binary_crossentropy',metrics=['accuracy'],optimizer='adam')




history = model.fit(X,y,epochs=10,validation_split=0.3,verbose=1)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'g', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.plot(epochs, loss, 'k', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')

plt.title('Training and validation accuracy')
plt.legend(loc="lower left")
plt.show()
plt.savefig('raspberrypi/plot.jpg')

model.save('raspberrypi/trained_model_raspberrypi.model')
