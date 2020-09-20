# Задача
Постройка модели класификации пола по изображению человека

![002026.jpg](https://github.com/Valdert-13/NtechLab/blob/master/img/002026.jpg)
# Инструкция по запуску
Поместите файл process.py и model.h5 в нутрь папки со средой python /even/python/process.py

# Build the cnn model
Модель использует 3 слоя для извлечения карты признаков и один для класификации

![flatten.jpg](https://github.com/Valdert-13/NtechLab/blob/master/img/3%20conv%20%2B%201%20flatten.jpg)
```python
# 3 conv layer
model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=IMG_SHAPE)) # Свертка
model.add(BatchNormalization()) # Нормализация данных
model.add(MaxPooling2D(pool_size=(2, 2))) # Уплотнение карыт признаков
model.add(Dropout(0.25)) # Удаление доли взаимосвязи случайным образом при каждой итерации

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
```
#Резултат
Точность модели составила 0.975

![Screenshot](https://github.com/Valdert-13/NtechLab/blob/master/img/Screenshot%202020-09-20%20120320.jpg)

В предобработке изображений был использован ImageDataGenerator.flow_from_dataframe(), 
что позволило боротся с переобучением, созданием дополнительных вариантов изображения 
