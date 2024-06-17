import vk_api, time, random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api.utils

date_reg = time.localtime()
counter_complaint = 0

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Правила клана', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Как попаcть в чат', color=VkKeyboardColor.POSITIVE)
keyboard.add_line() 
keyboard.add_openlink_button('Играть за нас', link='https://vk.com/app7804694_-225430598')
keyboard.add_line()
keyboard.add_button('Другое', color=VkKeyboardColor.PRIMARY)

keyboard_new = VkKeyboard(one_time=True)
keyboard_new.add_button('Пожаловаться', VkKeyboardColor.NEGATIVE)
keyboard_new.add_line()
keyboard_new.add_button('Назад', VkKeyboardColor.PRIMARY)

complaint_keyboard = VkKeyboard(one_time=True)
complaint_keyboard.add_button('1')
complaint_keyboard.add_button('2')
complaint_keyboard.add_button('3')
complaint_keyboard.add_button('4')
complaint_keyboard.add_line()
complaint_keyboard.add_button('5')
complaint_keyboard.add_button('6')
complaint_keyboard.add_button('7')
complaint_keyboard.add_button('8')
complaint_keyboard.add_line()
complaint_keyboard.add_button('9')
complaint_keyboard.add_button('10')
complaint_keyboard.add_button('11')
complaint_keyboard.add_button('12')
complaint_keyboard.add_line()
complaint_keyboard.add_button('13')
complaint_keyboard.add_button('14')
complaint_keyboard.add_button('15')
complaint_keyboard.add_button('16')
complaint_keyboard.add_line()
complaint_keyboard.add_button('17')
complaint_keyboard.add_button('18')

reason_complaint = VkKeyboard(one_time=True)
reason_complaint.add_button('Скамерство')
reason_complaint.add_line()
reason_complaint.add_button('Купил рабов')
reason_complaint.add_line()
reason_complaint.add_button('Кинул камень')
reason_complaint.add_line()
reason_complaint.add_button('Оскорбил')

def write_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard.get_keyboard()})

def keyboard_none(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

def keyboard1(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard_new.get_keyboard()})

def complaint(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': complaint_keyboard.get_keyboard()})

def reason(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': reason_complaint.get_keyboard()})

token = 'vk1.a.yr6MW-cOMA7qHdj0cdllOTrHtmAZNW2ZHPmuAB6gbX0MfUXAV4HpH9KxdBmHvqoqrwkjLW37tDSFm_qlF6rPXcEHD7vrGM0L4MhpUju3oaWes_dAiesFhG_CjjyuXV5o914LMgpKPNHU3FRMnTbyuLNq6SdqX51346P8Ab4iR5lmAxJjpqMvfSlP9TbeOhTndTMFCm_zCTz74iIhgP700A'
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseive_massage = event.text
        lower_string = reseive_massage.lower()
        sender = event.user_id

        user = authorize.method("users.get", {"user_ids": sender})
        fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
        surname = user[0]['last_name']
        name = user[0]['first_name']

        print(f'{name}, воспользовался ботом!')

        if  lower_string == 'привет' or lower_string == 'начать':
            write_message(sender, 'Привет, я Vox0.6, бот этого сообщества.')

        elif event.type == VkEventType.USER_RECORDING_VOICE:
            write_message(sender, 'Извини, я не умею разпозновать голос')

        elif lower_string == 'пожаловаться':
            if counter_complaint == 0:
                counter_complaint += 1
                keyboard_none(sender, 'На какого игрока вы хотите пожаловаться?')
                complaint(sender, '1) Максимка Самоваров \n2) Романюк Даниил \n3) 自然に生まれた 優勝者BetBoom Team \n4) Егор Алексеев \n5) Сергей Анискин \n6) Pasha Stepanov \n 7) Andrey Andreevich \n8) Никита Перунов \n9) Стас Павлов \n10) Вадим Семенов \n11) Семен Семенов \n12) Роман Черников \n13) Скуби Триксов-Райнер \n14) Павел Юрьевич \n15) Артем Апельсинов \n16) Дмитрий Олегович \n17) Дикость Троп \n18) Дмитрий Бекетов')
                time.sleep(5)

            elif counter_complaint == 1:
                counter_complaint -= 1
                write_message(sender, 'Вы не закончили заявку на жалобу')
        
        elif lower_string == '1' or lower_string =='2' or lower_string == '3' or lower_string == '4' or lower_string == '5' or lower_string == '6' or lower_string == '7' or lower_string == '8' or lower_string == '9' or lower_string == '10' or lower_string == '11' or lower_string == '12' or lower_string == '13' or lower_string == '14' or lower_string == '15' or lower_string == '16' or lower_string == '17' or lower_string == '18' and counter_complaint == 1:
            reason(sender, f'{name}, укажите причину жалобы')
        
        elif lower_string == 'скамерство' or lower_string == 'купил рабов' or lower_string == 'кинул камень' or lower_string == 'оскорбил' and counter_complaint == 1:
            keyboard_none(sender, 'Ваша заявка принята, вскоре с вами свяжется админ')
            print(f'{name}, отправил жалобу')
            counter_complaint -= 1
        
        elif lower_string == 'правила клана':
            write_message(sender, 'Пожалуйста, не забывайте о следующих правилах: \n ⃣ Не размещайте оскорбительные или провокационные комментарии. \n ⃣ Уважайте точку зрения других участников и ведите диалог в конструктивной манере. \n ⃣ Не покупайте рабов у соклановцев. \n ⃣Не оскобляйте соклановцев. \n ⃣Не кидайте камни в соклановцев. \n \nСоблюдая эти простые правила, мы создадим приятную и благоприятную обстановку для всех участников нашего сообщества. Благодарим вас за внимание и поддержку! 💪👀')
            
        elif lower_string == 'пока' or lower_string == 'спасибо' or lower_string == 'спасибо!':
            write_message(sender, 'Рад помочь!')

        elif lower_string == 'как играть за клан':
            write_message(sender, 'Чтобы играть за клан тебе нужно перейти по ссылке, которая находится в меню нашего сообщества')
            keyboard.add_openlink_button('Играть за нас', link='https://vk.com/app7804694_-225430598')

        elif lower_string == 'как попасть в чат' or reseive_massage == 'Как попасть в чат':
            write_message(sender, 'Чтобы попасть в чат тебе нужно начать "Чат клана" в меню сообщества')

        elif lower_string == 'другое':
            keyboard1(sender, 'Чем могу помочь?')

        elif lower_string == '/break725326':
            break

        else:
            write_message(sender, f'{name}, внизу есть варианты ответов')
