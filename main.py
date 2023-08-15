import telebot
from telebot import types
import requests
from pprint import pprint
from config import weather
import datetime
import webbrowser


def get_weather(city, weather):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather}&units=metric')
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        dluna_dnya = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"Погода в городе: {city}\nТемпература: {cur_weather} C°\n"
              f"Влажность: {humidity} %\nДавление: {pressure} мм.рт.сс. \nВетер: {wind} м/c\n" 
              f"Восход: {sunrise} \nЗакат: {sunset} \nПродолжительность дня: {dluna_dnya} \n"
              f"***Хорошего дня***"
              )

    except Exception as ex:
        print()
        print('Ошибочка, проверьте название города.')


def main():
    city = input('Введите свой город: ')
    get_weather(city, weather)


if __name__ == '__main__':
    main()

