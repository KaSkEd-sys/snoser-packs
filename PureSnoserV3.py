#made by wndkx with love
import aiohttp
import pystyle
import asyncio
import fake_useragent
import requests
import random
import sys
def random_number():
    country_codes = ["+1", "+7", "+374", "+375", "+380", "+994", "+995"]
    return random.choice(country_codes) + ''.join(random.choices('0123456789', k=10))
def random_email():
    providers = ["@gmail.com", '@hotmail.com', '@icloud.com', "@outlook.com", '@mail.ru', '@yahoo.com']
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._', k=random.randint(5,20))) + random.choice(providers)
async def send_post_request(url, data):
    ua = fake_useragent.UserAgent()
    user_agent = ua.random
    async with aiohttp.ClientSession(headers={"User-Agent": user_agent}) as session:
        response = await session.post(url, data=data)
        if response.status == 200:
            pystyle.Write.Print('Жалоба отправлена!\n', pystyle.Colors.green_to_white, interval=0.0001)
        else:
            pystyle.Write.Print("Не удалось отправить жалобу\n", pystyle.Colors.red, interval=0.0001)
async def send(text):
    ammount = int(pystyle.Write.Input("\nКол-во жалоб:", pystyle.Colors.green_to_white, interval=0.0001))
    for _ in range(1, ammount+1):
        email = random_email()
        number = random_number()
        await send_post_request('https://telegram.org/support', {
            "message": text,
            "email": email,
            "phone": number
        })
def menu():
    pystyle.System.Clear()
    pystyle.Write.Print("""
                            888888ba  dP     dP  888888ba   88888888b .d88888b  888888ba   .88888.  .d88888b   88888888b  888888ba  
                            88    `8b 88     88  88    `8b  88        88.    "' 88    `8b d8'   `8b 88.    "'  88         88    `8b 
                            a88aaaa8P'88     88  a88aaaa8P' a88aaaa   `Y88888b. 88     88 88     88 `Y88888b. a88aaaa    a88aaaa8P' 
                            88        88     88  88   `8b.  88              `8b 88     88 88     88       `8b  88         88   `8b. 
                            88        Y8.   .8P  88     88  88        d8'   .8P 88     88 Y8.   .8P d8'   .8P  88         88     88 
                            dP        `Y88888P'  dP     dP  88888888P  Y88888P  dP     dP  `8888P'   Y88888P   88888888P  dP     dP 
                            ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
                                             V3 by wndkx; https://t.me/wndkx ; support: https://t.me/wndkx_support_bot
                                            [1] Снос аккаунта             [3] Снос ботов             [5] Свой текст
                                            [2] Снос канала               [4] Снос чатов             [6] Выход                                                          
""", pystyle.Colors.green_to_white, interval=0.0001)
    
if __name__ == '__main__':
    while True:
        try:
            menu()
            main_choice = int(pystyle.Write.Input("""                           Выбери опцию:""", pystyle.Colors.green_to_white, interval=0.0001))
            if main_choice == 1:
                pystyle.Write.pystyle.Write.Print("Следуйте указаниям")
                username = pystyle.Write.Input("юзернейм: ", pystyle.Colors.green_to_white, interval=0.0001)
                userid = pystyle.Write.Input("айди: ", pystyle.Colors.green_to_white, interval=0.0001)
                chat_link = pystyle.Write.Input("ссылка на чат: ", pystyle.Colors.green_to_white, interval=0.0001)
                violation_link = pystyle.Write.Input("ссылка на нарушение: ", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("Теперь выбери одну из этих опций: \n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("1. Спам.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("2. Доксинг.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("3. Троллинг.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("4. Снос сессий.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("5. С премкой.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("6. С вирт номером.\n", pystyle.Colors.green_to_white, interval=0.0001)
                option = int(pystyle.Write.Input(">"))
                if option > 1 and option < 4:
                    comp_texts = {
                            1: f"Здравствуйте, уважаемая поддержка. На вашей платформе я недавно столкнулся с пользователем, который, как мне кажется, занимается массовой рассылкой спама. Его юзернейм - {username}, его айди - {userid}, ссылка на чат, где я это наблюдал, - {chat_link}, а вот ссылка на примеры нарушений - {violation_link}. Я бы очень просил вас разобраться с этим случаем и принять необходимые меры в отношении данного пользователя.",
                            2: f"Уважаемая поддержка, на вашей платформе я обнаружил пользователя, который, судя по всему, занимается распространением чужих личных данных без согласия владельцев. Его юзернейм - {username}, айди - {userid}, ссылка на чат, где я это заметил, - {chat_link}, а вот ссылка на примеры таких нарушений - {violation_link}. Я прошу вас тщательно разобраться в этом инциденте и предпринять соответствующие меры, вплоть до блокировки аккаунта этого пользователя.",
                            3: f"Добрый день, уважаемая поддержка Telegram. Недавно мне довелось наблюдать, как один из пользователей вашей платформы активно использует нецензурную лексику и занимается спамом в чатах. Его юзернейм - {username}, айди - {userid}, ссылка на чат, где я это видел, - {chat_link}, а вот примеры таких нарушений - {violation_link}. Я очень рассчитываю, что вы отреагируете на этот случай и примете надлежащие меры, включая возможную блокировку аккаунта данного пользователя."
                    }
                    asyncio.run(send(comp_texts[option]))
                elif option == 4:
                    pystyle.Write.pystyle.Write.Print("следуйте указаниям:\n", pystyle.Colors.green_to_white, interval=0.0001)
                    username = pystyle.Write.Input("юзернейм: ", pystyle.Colors.green_to_white, interval=0.0001)
                    userid = pystyle.Write.Input("айди: ")
                    asyncio.run(send(f"Уважаемая поддержка, прошу вас о помощи. Вчера я случайно перешел по ссылке, которая оказалась фишинговой, и в результате потерял доступ к своему аккаунту. Мой юзернейм - {username}, айди - {userid}. Я очень прошу вас как можно скорее удалить этот аккаунт или сбросить все сессии, чтобы я мог восстановить доступ и обезопасить свою учетную запись. Заранее благодарен за оперативное рассмотрение моего обращения."))
                elif option == 5 or option == 6:
                    pystyle.Write.pystyle.Write.Print("следуйте указаниям:\n", pystyle.Colors.green_to_white, interval=0.0001)
                    username = pystyle.Write.Input("юзернейм: ")
                    userid = pystyle.Write.Input("айди: ")
                    comp_texts = {
                        5: f"Добрый день, поддержка Telegram! Я хотел бы сообщить вам, что пользователь с аккаунтом {username} ({userid}) использует виртуальный номер, приобретенный на специализированном сайте по активации номеров. Насколько я могу судить, этот номер не имеет к нему никакого отношения. Я очень прошу вас разобраться в этой ситуации. Заранее благодарю за содействие!",
                        6: f"Уважаемая поддержка Telegram! Мне стало известно, что пользователь с аккаунтом {username} ({userid}) приобрел премиум-аккаунт в вашем мессенджере с целью рассылки спам-сообщений и обхода ограничений Telegram. Я настоятельно прошу вас проверить эту информацию и принять необходимые меры. Заранее признателен за ваше внимание к данному вопросу."
                    }
                    asyncio.run(send(comp_texts[option]))
            if main_choice == 2:
                pystyle.Write.Print("1. Личные данные.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("2. Живодерство.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("3. Цп.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("4. Прайс каналы.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("5. Наркотики.\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("6. 18+(шок контент, порнография и др. подобные материалы).\n", pystyle.Colors.green_to_white, interval=0.0001)
                ch_choice = int(pystyle.Write.Input("выбор: ", pystyle.Colors.green_to_white, interval=0.0001))

                if ch_choice in [1, 2, 3, 4, 5, 6]:
                    channel_link = pystyle.Write.Input("ссылка на канал: ", pystyle.Colors.green_to_white, interval=0.0001)
                    channel_violation = pystyle.Write.Input("ссылка на нарушение (в канале): ", pystyle.Colors.green_to_white, interval=0.0001)
                    pystyle.Write.Print("Ожидайте...", pystyle.Colors.green_to_white, interval=0.0001)
                    comp_texts = {
                        1: f"Уважаемая поддержка Telegram, я обнаружил на вашей платформе канал, который, по всей видимости, занимается распространением личных данных невинных людей. Ссылка на этот канал - {channel_link}, а вот ссылки на конкретные примеры нарушений - {channel_violation}. Убедительно прошу вас оперативно заблокировать данный канал.",
                        2: f"Здравствуйте, уважаемая поддержка Telegram. К сожалению, на вашей платформе я наткнулся на канал, который, кажется, занимается распространением контента, связанного с жестоким обращением с животными. Ссылка на этот канал - {channel_link}, а ссылки на подтверждающие материалы - {channel_violation}. Я очень надеюсь, что вы примете срочные меры по блокировке этого канала.",
                        3: f"Уважаемая поддержка Telegram, мною был обнаружен на вашей платформе канал, который, по имеющимся данным, распространяет порнографический контент с участием несовершеннолетних. Ссылка на этот канал - {channel_link}, а вот ссылки на конкретные примеры таких нарушений - {channel_violation}. Убедительно прошу вас как можно скорее заблокировать данный канал.",
                        4: f"Здравствуйте, уважаемый модератор Telegram. Я хотел бы пожаловаться на канал в вашем мессенджере, который, как мне стало известно, предоставляет услуги по доксингу и сваттингу. Ссылка на этот канал - {channel_link}, а ссылки на подтверждающие материалы - {channel_violation}. Прошу вас незамедлительно заблокировать данный канал.",
                        5: f"Уважаемая поддержка, в вашем мессенджере Telegram я обнаружил канал, который, судя по всему, занимается незаконной продажей наркотических веществ. Айди этого канала - {channel_link}, а вот ссылка на конкретное нарушение - {channel_violation}. Убедительно прошу вас рассмотреть этот вопрос и принять соответствующие меры по блокировке данного канала.",
                        6: f"Здраствуйте, уважаемый модератор Telegram. Я бы хотел пожаловаться на канал в вашем мессенджере, который распространяет 18+ и шок материалы на публичное обозрение. Прошу как можно быстрее принять меры. Ссылка на канал: {channel_link}. Ссылка на нарушение: {channel_violation}"
                    }
                    asyncio.run(send(comp_texts[ch_choice]))
            if main_choice == 3:
                pystyle.Write.Print("1. Осинт\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("2. Наркошоп\n", pystyle.Colors.green_to_white, interval=0.0001)
                bt_choice = int(input(">>"))
                if bt_choice in [1,2]:
                    bot_user = pystyle.Write.Input("юз бота: ", pystyle.Colors.green_to_white, interval=0.0001)
                    pystyle.Write.Print("Ожидайте...", pystyle.Colors.green_to_white, interval=0.0001)
                    comp_texts = {
                        1: f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                        2 :f"Здравствуйте, в вашем мессенджере я наткнулся на бота который производит незаконную торговлю наркотиками. Прошу отреагировать на мою жалобу и принять меры по блокировке данного бота."
                    }
                    asyncio.run(send(comp_texts[bt_choice]))
            if main_choice == 4:
                pystyle.Write.Print("1. Спам\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("2. За аву или название\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("3. Пропаганда насилия и тп\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("4. Накрутка\n", pystyle.Colors.green_to_white, interval=0.0001)
                pystyle.Write.Print("5. Оски\n", pystyle.Colors.green_to_white, interval=0.0001)
                ch = int(pystyle.Write.Input('Выбирай> ', pystyle.Colors.green_to_white, interval=0.0001))
                if ch in [1,2,3,4]:
                    user_chat = pystyle.Write.Input('Ссылка на чат: ', pystyle.Colors.green_to_white)
                    id_chat = pystyle.Write.Input('Айди чата: ', pystyle.Colors.green_to_white)
                    comp_texts = {1: f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой проходят спам-рассылки. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее.",
                        2: f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой стоит вызывающая аватарка и имя, разжигающее конфликты. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее.",
                        3: f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой пропогондируется насилие и другие подобные жестокости. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее",
                        4: f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел группу в которой происходит накрутка подписчиков. Ссылка на группу - {user_chat}, Айди группы - {id_chat}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее"
                    }
                    asyncio.run(send(comp_texts[ch]))
                if ch in [5]:
                    user_chat = pystyle.Write.Input('Ссылка на чат: ', pystyle.Colors.green_to_white)
                    id_chat = pystyle.Write.Input('Айди чата: ', pystyle.Colors.green_to_white)
                    link = pystyle.Write.Input('Ссылка на нарушение: ', pystyle.Colors.green_to_white)
                    asyncio.run(send(f"Здравствуйте, уважаемая поддержка телеграмма. Я нашел группу с которой оскорбляют людей и используют ненормативную лексику в их сторону. Ссылка на группу - {user_chat}, Айди группы - {id_chat}, Ссылка на нарушение - {link}. Пожалуйста примите меры в сторону этой группы и заблокируйте ее как можно скорее"))
            if main_choice == 5:
                inp = pystyle.Write.Input('Введи свой текст: ', pystyle.Colors.green_to_white, interval=0.0001)
                asyncio.run(send(inp))
            if main_choice == 6:
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()
        except ValueError:
            menu()
        except Exception as e:
            pystyle.Write.Print(f"Произошла ошибка! {str(e)}\n", pystyle.Colors.red, interval=0.0001)
            input()