import numpy as np
from keras.models import load_model
from PIL import Image
import sys

model = load_model('soundbutler_model.h5')

img = Image.open(sys.argv[1]).resize((244, 244))
img = np.array(img).reshape((1, 244, 244, 3))

result = model.predict(img)

if np.argmax(result) == 0:
    sys.exit(1)
else:
    sys.exit(0)
