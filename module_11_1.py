from pprint import pprint
from time import sleep

#Библиотека PANDAS
import pandas as pn

file = 'data.csv'
data = pn.read_csv(file, encoding='cp1252')
row_count = data.count(axis=1).count()

print(f"Первые 5 строк данных в файле: {file}")
print(data.head())

print(f"\nВсе строки данных из файла: {file}:")
print(data.head(row_count + 1))

print("\nИнформация о данных файла:")
print(data.info())

print("\nОбщая статистика по всем данным в файле:")
print(data.describe())

print("\nКоличество уникальных значений в каждом столбце:")
print(data.nunique())

print("\nПропущенные значения в данных:")
print(data.isnull().sum())

print("\nФильтрация данных (значение в колонке 'Sex' = Female):")
filtered_data = data[data['Sex'] == 'Female']
print(filtered_data)


# Библиотека REQUESTS
import requests as rq

ACCESS_TOKEN = 'Lgm3zETbCrYMbhUIMGsG-K02YHdlH8-jaAVIDWHecndEBwDxvOYAYq5ZErzn-i_P'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'

while True:
    genre = rq.get(RANDOM_GENRE_API_URL).json()
    data = rq.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre}).json()
    if len(data['response']) > 0:
        pprint(data['response']['hits'])
        break
        sleep(1)


#Библиотека Pillow

from PIL import Image, ImageFilter, ImageDraw, ImageFont

image = Image.open('grey-cat.jpg')


image.thumbnail ((800, 800))

image = image.filter(ImageFilter.CONTOUR)
#
draw_image = ImageDraw.Draw(image)
font = ImageFont.truetype('a_Albionic.ttf', 36)
draw_image.text((20, 30), "Это Кот!", font=font, fill='red')

image.save('img_2.jpg')
image.show()




