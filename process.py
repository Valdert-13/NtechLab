import pandas as pd
import numpy as np
import os

import json
import argparse
from config import * #Файл настроек

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model



def list_files(directory: str, extension: str) -> list:
    """
    Получения списка файлов по указанному пути с определенным расширением
    :param directory: str
    путь к искомой директории
    :param extension: str
    формат расширения файла
    :return: list
    список файлов
    """

    list_filenames = []
    for filenames in os.listdir(directory):
        if filenames.split('.')[-1] == extension:
            list_filenames.append(filenames)

    return list_filenames

parser = argparse.ArgumentParser(description='Предсказания пола человека по изображению .jpg')
parser.add_argument('string', metavar='Path', type=str,
                    help='Path to test files')


path = parser.parse_args()
assert os.path.isdir(path) == True, 'Укажите существующую директорию'
assert os.path.isfile('model.h5') == True, 'Поместите модель в одну дерикторию с исполяемым файлом'

test_filenames = list_files(path, 'jpg')

test_df = pd.DataFrame({
    'filename': test_filenames
    })

nb_samples = test_df.shape[0]

test_gen = ImageDataGenerator(rescale=1./255)
test_generator = test_gen.flow_from_dataframe(
    test_df,
    path,
    x_col='filename',
    y_col=None,
    class_mode=None,
    target_size=IMG_SHAPE[:2],
    batch_size=BATCH_SIZE,
    shuffle=False
)

model = load_model("model.h5")
predict = model.predict(test_generator, steps=np.ceil(nb_samples/BATCH_SIZE))
test_df['category'] = np.argmax(predict, axis=-1)
test_df['category'] = test_df['category'].replace({ 1:'male', 0:'female' })
dic = test_df.set_index('filename').T.to_dict('records')[0]
with open('process_results.json', 'w') as fp:
    json.dump(dic, fp)
