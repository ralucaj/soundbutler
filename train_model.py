from keras.applications import vgg16
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, BatchNormalization, Flatten, Dropout
from keras.models import Model
import numpy as np


vgg_mean = np.array([123.68, 116.779, 103.939], dtype=np.float32).reshape((1, 1, 3))
# I tried using this and not using this in the image loading, makes no difference


def vgg_preprocess(x):
    x = x - vgg_mean
    return x


def get_custom_vgg():
    model = vgg16.VGG16(include_top=False, input_shape=(244, 244, 3))

    for layer in model.layers:
        layer.trainable = False

    x = Flatten()(model.output)
    x = Dense(124, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.5)(x)
    x = Dense(124, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.5)(x)
    x = Dense(2, activation='softmax')(x)

    return Model(model.input, outputs=x)


def get_train_generator(path_to_dir, batch_size, target_size=(244, 244)):
    data_generator = ImageDataGenerator(preprocessing_function=vgg_preprocess)

    generator = data_generator.flow_from_directory(
        path_to_dir,
        batch_size=batch_size,
        target_size=target_size
    )

    return generator


batch_size = 16
model = get_custom_vgg()
train_gen = get_train_generator('store/soundbutler/train', batch_size)
valid_gen = get_train_generator('store/soundbutler/valid', batch_size)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit_generator(train_gen,
                    steps_per_epoch=int(len(train_gen.filenames) / batch_size),
                    validation_steps=int(len(valid_gen.filenames) / batch_size),
                    validation_data=valid_gen,
                    epochs=10,
                    verbose=2
                    )

model.save('soundbutler_model.h5')
