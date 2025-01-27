# DECODED BY HYPER X SQUAD >>> TOP 1 
# @decoded_softs

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import string
import requests
import colored
import json
from colorama import init
init()
from colorama import Fore, Back, Style
from pystyle import *
import webbrowser



banner = """                                                                                                                                                                         
"""

text = """  
      ██╗   ██╗ █████╗ ██████╗  ██████╗ ██╗   ██╗██████╗     
      ██║   ██║██╔══██╗██╔══██╗██╔═══██╗██║   ██║██╔══██╗    
      ██║   ██║███████║██████╔╝██║   ██║██║   ██║██████╔╝    
      ╚██╗ ██╔╝██╔══██║██╔═══╝ ██║   ██║██║   ██║██╔══██╗    
       ╚████╔╝ ██║  ██║██║     ╚██████╔╝╚██████╔╝██║  ██║    
        ╚═══╝  ╚═╝  ╚═╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝  
                    made - Захотел
                     Channel @FreeBestSoft 
                      Channel @FREE_TOP_SOFT
                 Любовь это страх..........
                                  . . .  . 
                                   . .  .  .
                                   . .  . . .
                                   .  . .  . .
                                  
                                                       
                  
              1 Snos Account         4 Your text
       
 .            2 Snos Chanell         5 info
      
              3 Snos bot             6 made
  >>>>>>                                   
                   
"""
print()
print(Colorate.Vertical(Colors.red_to_black, Center.XCenter(banner)))
print(Colorate.Vertical(Colors.red_to_black, Center.XCenter(text)))



COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

senders = {
"DaianaVolovikova1988@list.ru": "RBq7KvDpfwGePV48bYWr",
"ZavoruevEdoardo2005@list.ru": "1YS6sHWQijRDE3av6tk9",
"LupovaAlbbina1990@list.ru": "h8Z1gjbubVeV9n2sTLay",
"FirmVershilo@bk.ru": "sjptmTVLXzV1x3it9s0S",
"StepushkinKlint2005@inbox.ru": "eADEUp0QkEz8P8840bFh",
"LiliyaGorodnikova@inbox.ru": "NBTYyEcCi8cBCb1FJ1MY",
"VideniktBalamutkin95@list.ru": "wwsKYUcqwTrNsYXdnSH4",
"MalkovKeri2000@bk.ru": "SCciRkzkUaw3GxLqLsq3",
"ZahmetGrishutov@inbox.ru": "df9TbquCZNbedDfPdEQp",
"DaianaVolovikova1988@list.ru": "RBq7KvDpfwGePV48bYWr",
"ZavoruevEdoardo2005@list.ru": "1YS6sHWQijRDE3av6tk9",
"LupovaAlbbina1990@list.ru": "h8Z1gjbubVeV9n2sTLay",
"FirmVershilo@bk.ru": "sjptmTVLXzV1x3it9s0S",
"StepushkinKlint2005@inbox.ru": "eADEUp0QkEz8P8840bFh",
"LiliyaGorodnikova@inbox.ru": "NBTYyEcCi8cBCb1FJ1MY",
"VideniktBalamutkin95@list.ru": "wwsKYUcqwTrNsYXdnSH4",
"MalkovKeri2000@bk.ru": "SCciRkzkUaw3GxLqLsq3",
"ZahmetGrishutov@inbox.ru": "df9TbquCZNbedDfPdEQp",
"DaianaVolovikova1988@list.ru": "RBq7KvDpfwGePV48bYWr",
"ZavoruevEdoardo2005@list.ru": "1YS6sHWQijRDE3av6tk9",
"LupovaAlbbina1990@list.ru": "h8Z1gjbubVeV9n2sTLay",
"FirmVershilo@bk.ru": "sjptmTVLXzV1x3it9s0S",
"StepushkinKlint2005@inbox.ru": "eADEUp0QkEz8P8840bFh",
"LiliyaGorodnikova@inbox.ru": "NBTYyEcCi8cBCb1FJ1MY",
"VideniktBalamutkin95@list.ru": "wwsKYUcqwTrNsYXdnSH4",
"MalkovKeri2000@bk.ru": "SCciRkzkUaw3GxLqLsq3",
"ZahmetGrishutov@inbox.ru": "df9TbquCZNbedDfPdEQp"

}
receivers = ['stopca@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org', 'sticker@telegram.org', 'support@telegram.org', 'security@telegram.org', 'sms@telegram.org', 'info@telegram.org', 'org', 'spam@telegram.org', 'alex@telegram.org', 'pavel@telegram.org', 'durov@telegram.org', 'elies@telegram.org', 'ceo@telegram.org', 'mr@telegram.org', 'levlam@telegram.org', 'perekopsky@telegram.org', 'recover@telegram.org', 'germany@telegram.org', 'hyman@telegram.org', 'qa@telegram.org', 'stickers@telegram.org', 'ir@telegram.org', 'vadim@telegram.org', 'shyam@telegram.org', 'ask@telegram.org', '125support@telegram.org', 'me@telegram.org', 'enquiries@telegram.org', 'api_support@telegram.org', 'marketing@telegram.org', 'ca@telegram.org', 'recovery@telegram.org', 'http@telegram.org', 'corp@telegram.org', 'corona@telegram.org', 'ton@telegram.org']


def menu():
    choice = input(f'{COLOR_CODE["PINK"]} Выбери пункт ➤ {COLOR_CODE["RED"]} ')
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(0.5)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    choice = menu()
    if choice == '1':
        print("1. [СПАМ].")
        print("2. [Доксинг].")
        print("3. [Троллинг]")
        print("5. [С вирт номером.]")
        print("6. [С премиумом.]")
        comp_choice = input("-> ")
        if comp_choice in ["1", "2", "3"]:
            print("следуй за указаниям")
            username = input("[юзернейм] ")
            id = input("[айди] ")
            chat_link = input(" Ссылка на чат ")
            violation_link = input("[ссылка на нарушение] ")
            print("ОТПРАВКА")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я недавно столкнулся с пользователем, который, как мне кажется, занимается массовой рассылкой спама. Его юзернейм - {username}, его айди - {id}, ссылка на чат, где я это наблюдал, - {chat_link}, а вот ссылка на примеры нарушений - {violation_link}. Я бы очень просил вас разобраться с этим случаем и принять необходимые меры в отношении данного пользователя.",
                "2": f"Уважаемая поддержка, на вашей платформе я обнаружил пользователя, который, судя по всему, занимается распространением чужих личных данных без согласия владельцев. Его юзернейм - {username}, айди - {id}, ссылка на чат, где я это заметил, - {chat_link}, а вот ссылка на примеры таких нарушений - {violation_link}. Я прошу вас тщательно разобраться в этом инциденте и предпринять соответствующие меры, вплоть до блокировки аккаунта этого пользователя.",
                "3": f"Добрый день, уважаемая поддержка Telegram. Недавно мне довелось наблюдать, как один из пользователей вашей платформы активно использует нецензурную лексику и занимается спамом в чатах. Его юзернейм - {username}, айди - {id}, ссылка на чат, где я это видел, - {chat_link}, а вот примеры таких нарушений - {violation_link}. Я очень рассчитываю, что вы отреагируете на этот случай и примете надлежащие меры, включая возможную блокировку аккаунта данного пользователя."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    try:
                        comp_text = comp_texts[comp_choice]
                        comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                        violation_link=violation_link.strip())
                        send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                    except Exception as e:
                        print("Не удалось отправить письмо")
                        sent_emails += 14888
                        time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print("следуйте указаниям:")
            username = input("юзернейм: ")
            id = input("айди: ")
            comp_texts = {
                "5": f"Добрый день, поддержка Telegram! Я хотел бы сообщить вам, что пользователь с аккаунтом {username} ({id}) использует виртуальный номер, приобретенный на специализированном сайте по активации номеров. Насколько я могу судить, этот номер не имеет к нему никакого отношения. Я очень прошу вас разобраться в этой ситуации. Заранее благодарю за содействие!",
                "6": f"Уважаемая поддержка Telegram! Мне стало известно, что пользователь с аккаунтом {username} ({id}) приобрел премиум-аккаунт в вашем мессенджере с целью рассылки спам-сообщений и обхода ограничений Telegram. Я настоятельно прошу вас проверить эту информацию и принять необходимые меры. Заранее признателен за ваше внимание к данному вопросу."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    try:
                        send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    except Exception as e:
                        print("Не удалось отправить письмо")
                        time.sleep(5)



    elif choice == "2":
        
        print("1. [Докс]")
        print("2. [Живодёрство]")
        print("3. [Детское]")
        print("4. [Прайс]")
        ch_choice = input("[выбор] ")
        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("[ссылка на канал]")
            channel_violation = input("[ссылка на нарушение] (в канале): ")
            print("Осталось совсем чучуть.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(0.5)


    elif choice == "3":
        print("1. [Осинт]")
        print("2. [Наркошоп]")
        bot_ch = input("[Выберите вариант]")

        if bot_ch == "1":
            bot_user = input("[юз бота] ")
            print("ожидание")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "2" :f"Здравствуйте, в вашем мессенджере я наткнулся на бота который производит незаконную торговлю наркотиками. Прошу отреагировать на мою жалобу и принять меры по блокировке данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    try:
                        send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    except Exception as e:
                        print("Не удалось отправить письмо")
                        time.sleep(5)
    elif choice == "5":
        print("снос это - удаление аккаунта человеку за жалобу  в это входит порно дп цп нарушение правил и тд входят оски но очень редко еще существуют ботнет боты для сноса сносят они не большие отлеги до 2 лет у нас есть ботнет okov snoser в нашем тгк функция 6")
        
    elif choice == "6":
        print("сделал софт захотел больше софтов тут https://t.me/FREE_TOP_SOFT")
    
    elif choice == "7":
        exit
        
        

  
if __name__ == "__main__":
    main()

