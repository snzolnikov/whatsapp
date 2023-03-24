# https://github.com/pythontoday/wasendmsg/blob/master/main.py


import pywhatkit as pwk
# import os
from config import MOBILE


def send_message_inst():
    # input('Введите номер получателя: ')
    # mobile = "+79829475224"
    mobile = MOBILE

    message = input('Введите текст сообщения: ')
    try:
        pwk.sendwhatmsg_instantly(phone_no=mobile, message=message)
    except:
        print("Error in sending the message")


def send_message():
    #mobile = input('Введите номер получателя: ')
    mobile = "+79829475224"
    # mobile = os.getenv('MOBILE')
    message = input('Введите текст сообщения: ')
    hour = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))

    pwk.sendwhatmsg(phone_no=mobile, message=message, time_hour=hour, time_min=minutes)


def main():
    send_message_inst()
    #send_message()
    #pwk.image_to_ascii_art(img_path='hack_achiv.png')


if __name__ == '__main__':
    main()
