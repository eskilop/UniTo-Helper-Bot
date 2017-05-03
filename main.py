#!/usr/bin/python3

'''
   Copyright 2016-2017 Eskilop

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

import telebot
from telebot import types
import urllib.request
from bs4 import BeautifulSoup
from options import *
import datetime
import sys
from user import User
from dbhelper import DBHelper
import signal

bot = telebot.TeleBot(api_token)

# take the current day and save it +1 (Mon = 1)
dow = datetime.datetime.today().weekday()+1

@bot.message_handler(func=lambda m: True, content_types=['new_chat_member'])
def new_member(message):
    bot.reply_to(message, general_info.format(message.new_chat_member.first_name), parse_mode="markdown")
    setup(message)

@bot.message_handler(commands=['start'])
def send_inline(message):
    u = User(message.chat.id, message.chat.username, message.chat.first_name, 1, "")
    if (u.check()):
        bot.reply_to(message, welcome_back.format(message.chat.first_name), parse_mode="markdown")
    else:
        u.save_user()
        bot.reply_to(message, general_info.format(message.chat.first_name))
        setup(message)
        
@bot.message_handler(commands=['bug'])
def send_bug(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, bug_msg, reply_markup=markup)

@bot.message_handler(commands=['feature'])
def send_feature(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, feature_msg, reply_markup=markup)

@bot.message_handler(commands=['setup'])
def get_settings(message):
    u = User(message.chat.id, message.chat.username, message.chat.first_name, 1, "")
    setup(message)


def setup(message):
    # start with the year
    year_kb = types.InlineKeyboardMarkup()
    y1 = types.InlineKeyboardButton("1", callback_data='year1')
    y2 = types.InlineKeyboardButton("2", callback_data='year2')
    y3 = types.InlineKeyboardButton("3", callback_data='year3')
    y4 = types.InlineKeyboardButton("4", callback_data='year4')
    y5 = types.InlineKeyboardButton("5", callback_data='year5')
    year_kb.row(y1, y2, y3)
    year_kb.row(y4, y5)
    bot.send_message(message.chat.id, "Di che anno sei?", reply_markup=year_kb)

@bot.callback_query_handler(func=lambda call: call.data)
def command_click_inline(call):
    tocourse = False;
    u = User(call.from_user.id, call.from_user.username, call.from_user.first_name, 1, "")
    if(call.data == "A"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso A")
        u.update_user("course", "A", call.from_user.id)
        tocourse=False;
    elif (call.data == "B"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso B")
        u.update_user("course", "B", call.from_user.id)
        tocourse=False
    elif (call.data == "E"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso di Informazione e Conoscenza")
        u.update_user("course", "E", call.from_user.id)
        tocourse=False
    elif (call.data == "N"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso di Linguaggi e Sistemi")
        u.update_user("course", "N", call.from_user.id)
        tocourse=False
    elif (call.data == "S"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso di Reti e Sistemi Informatici")
        u.update_user("course", "S", call.from_user.id)
        tocourse=False
    elif (call.data == "DI-STI"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso di Sistemi per il Trattamento dell'Icall.from_user.idnformazione")
        u.update_user("course", "DI-STI", call.from_user.id)
        tocourse=False
    elif (call.data == "DI-RVM"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso di Realtà Virtuale e Multimedialità")
        u.update_user("course", "DI-RVM", call.from_user.id)
        tocourse=False
    elif (call.data == "DI-RSI"):
        bot.answer_callback_query(call.id, text="Ora fai parte del corso di Reti e Sistemi Informatici")
        u.update_user("course", "DI-RSI", call.from_user.id)
        tocourse=False
    elif(call.data == "year1"):
        bot.answer_callback_query(call.id, text="Ora fai parte del 1° anno")
        u.update_user("year", 1, call.from_user.id)
        tocourse = True
    elif (call.data == "year2"):
        bot.answer_callback_query(call.id, text="Ora fai parte del 2° anno")
        u.update_user("year", 2, call.from_user.id)
        tocourse = True
    elif (call.data == "year3"):
        bot.answer_callback_query(call.id, text="Ora fai parte del 3° anno")
        u.update_user("year", 3, call.from_user.id)
        tocourse = True
    elif (call.data == "year4"):
        bot.answer_callback_query(call.id, text="Ora fai parte del 4° anno")
        u.update_user("year", 4, call.from_user.id)
        tocourse = True
    elif (call.data == "year5"):
        bot.answer_callback_query(call.id, text="Ora fai parte del 5° anno")
        u.update_user("year", 5, call.from_user.id)
        tocourse = True

    if(tocourse):
        m = types.InlineKeyboardMarkup()
        
        # based on the previously acquired year, we can show pertinent courses
        if (u.getYear() == 1 or u.getYear() == 2):
            # Just show 'A' and 'B' courses
            abtn = types.InlineKeyboardButton('A', callback_data="A")
            bbtn = types.InlineKeyboardButton('B', callback_data="B")
            m.row(abtn, bbtn)
        elif(u.getYear() == 3):
            # Just show remaining 3 courses
            ebtn = types.InlineKeyboardButton('Informazione e Conoscenza', callback_data="E")
            nbtn = types.InlineKeyboardButton('Linguaggi e Sistemi', callback_data="N")
            sbtn = types.InlineKeyboardButton('Reti e Sistemi Informatici', callback_data="S")
            m.add(ebtn)
            m.add(nbtn)
            m.add(sbtn)
        else:
            # Show masterly courses
            sti = types.InlineKeyboardButton('Sistemi per il trattamento dell\'informazione', callback_data="DI-STI")
            rvm = types.InlineKeyboardButton('Realtà Virtuale e Multimedialità', callback_data="DI-RVM")
            rsi = types.InlineKeyboardButton('Reti e Sistemi Informatici', callback_data="DI-RSI")
            m.add(sti)
            m.add(rvm)
            m.add(rsi)
        bot.edit_message_text("Che corso frequenti?", call.message.chat.id, call.message.message_id, reply_markup=m)
    else:
        bot.edit_message_text("Ottimo {}, ora sono al tuo servizio, in caso servisse aiuto, digita /help".format(call.from_user.first_name), call.message.chat.id, call.message.message_id)
        keyboard_insert(call.message)

@bot.message_handler(commands=['today'])
def get_today(message):
    u = User(message.chat.id, message.chat.username, message.chat.first_name, 1, "")
    dow = datetime.datetime.today().weekday()+1
    if dow > 5:
        bot.send_message(message.chat.id, "Non mi risulta che tu abbia lezione oggi \U0001F600")
    else:
        bot.send_message(message.chat.id, get_hours(dow, u.getYear(), u), parse_mode="html")

@bot.message_handler(commands=['tomorrow'])
def get_tomorrow(message):
    u = User(message.chat.id, message.chat.username, message.chat.first_name, 1, "")
    dow = datetime.datetime.today().weekday()+1
    if(dow >= 5):
        bot.send_message(message.chat.id, get_hours(1, u.getYear(), u), parse_mode="html")
    else:
        bot.send_message(message.chat.id, get_hours(dow+1, u.getYear(), u), parse_mode="html")

@bot.message_handler(commands=['yesterday'])
def get_yesterday(message):
    u = User(message.chat.id, message.chat.username, message.chat.first_name, 1, "")
    dow = datetime.datetime.today().weekday()+1
    if (dow == 1):
        bot.send_message(message.chat.id, get_hours(dow+5-1, u.getYear(), u), parse_mode="html")
    elif(dow == 7):
        bot.send_message(message.chat.id, get_hours(dow-2, u.getYear(), u), parse_mode="html")
    else:
        bot.send_message(message.chat.id, get_hours(dow-1, u.getYear(), u), parse_mode="html")

@bot.message_handler(commands=['week'])
def get_week(message):
    u = User(message.chat.id, message.chat.username, message.chat.first_name, 1, "")
    for i in range(1, 6):
        bot.send_message(message.chat.id, get_hours(i, u.getYear(), u), parse_mode="html")
    
@bot.message_handler(commands=['krem'])
def keyboard_remove(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Tastiera rimossa, per riutilizzarla, digita /kins", reply_markup=markup)

@bot.message_handler(commands=['kins'])
def keyboard_insert(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    todaybtn = types.KeyboardButton('Oggi')
    yesterdaybtn = types.KeyboardButton('Ieri')
    tomorrowbtn = types.KeyboardButton('Domani')
    weekbtn = types.KeyboardButton('Orario')
    settingsbtn = types.KeyboardButton('Impostazioni')
    helpbtn = types.KeyboardButton('Aiuto')
    markup.add(todaybtn, yesterdaybtn, tomorrowbtn, weekbtn, settingsbtn, helpbtn)
    bot.send_message(message.chat.id, "Tastiera inserita, se ti da fastidio, digita /krem", reply_markup=markup)

def get_hours(day_of_week, year, user, flag=None):
    message = ""

    courseLetter = user.getCourseLetter()

    index = 0;
    if(year <= 2):
        wpage, headers = urllib.request.urlretrieve(di_first_years.format("L", str(year), str(datetime.datetime.today().year-1))) # pagina del primo/secondo anno
        html = open(wpage).read()
        soup = BeautifulSoup(html, "html.parser")
        
        if (courseLetter == "B"):
            index = 2;
        else:
            index = 0;

    elif(year == 3):
        wpage, headers = urllib.request.urlretrieve(di_third_year.format("L", str(courseLetter), str(datetime.datetime.today().year-1))) # pagina del terzo anno
        html = open(wpage).read()
        soup = BeautifulSoup(html, "html.parser")
    elif(year >= 4):
        wpage, headers = urllib.request.urlretrieve(di_masterly.format(str(datetime.datetime.today().year-1))) # pagina del quarto/quinto anno
        html = open(wpage, encoding='ISO-8859-1').read()    # utf-8 won't read this
        soup = BeautifulSoup(html, "html.parser")
        
        if (user.getCourseLetter() == "DI-RVM"):
            index = 2
        elif(user.getCourseLetter() == "DI-RSI"):
            index = 4

    # Days
    if (day_of_week == 1):
        message += "<b>Lunedì</b>\n====================\n"
    elif (day_of_week == 2):
        message += "<b>Martedì</b>\n====================\n"
    elif (day_of_week == 3):
        message += "<b>Mercoledì</b>\n====================\n"
    elif (day_of_week == 4):
        message += "<b>Giovedì</b>\n====================\n"
    elif (day_of_week == 5):
        message += "<b>Venerdì</b>\n====================\n"

    table = soup.find_all('table')

    # Crawler-core
    for row in table[index].find_all('tr')[1:11]:
        ora = row.find_all_next('td')
        materia = row.find_all_next('td')
        space = "    "

        if (ora[0].text == "9-10"):
            space += "  "

        #              hour                        subject
        message += ora[0].text + space  + materia[day_of_week].text + "\n"

    return message


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id, "<b>Ciao</b>, sono <b> UniTo Helper.</b>\n" \
                        "Questi sono i comandi che puoi usare:\n" \
                        "'/help': mostra questo messaggio.\n" \
                        "'/kins': Inserisce una tastiera interattiva. \n" \
                        "'/krem': Rimuove la tastiera interattiva. \n" \
                        "'/bug': Segnala un malfunzionamento allo sviluppatore \n" \
                        "'/feature': Richiedi una particolare funzionalità (ciò non garantisce la sua effettiva implementazione) \n" \
                        "'/week': Ti mostro l'orario di questa settimana. <b>[attenzione: spamma]</b> \n" \
                        "'/yesterday': Ti mostro l'orario di ieri.\n" \
                        "'/tomorrow': Ti mostro l'orario di domani.\n" \
                        "'/today': Ti mostro cos'hai per oggi.\n"
                        "'/setup': Impostazioni"
                        "\n\n" \
                        "<b>Informazioni sul mio 'creatore':</b>\n" \
                        "Il mio creatore si chiama <b>Luca</b>, ed è uno studente proprio come te, ha anche altri progetti in mente" \
                        " elencati di seguito. Di tanto in tanto mi aggiornerà, Unisciti @eskilopchan, per sapere quando, e qualcosa in più. \n" \
                        "\n\n" \
                        "<b>Varie:</b>\n" \
                        "Unisciti a @eskilopchan se vuoi rimanere aggiornato su questo, e tanti altri progetti del mio padrone :D \n" \
                        "", parse_mode="HTML")
    bot.reply_to(message, "<b>Codice sorgente</b>\n" \
                        "Il codice sorgente di @unitohelperbot è su <a href=\"gitlab.com/eskilop/unitohelperbot\">GitLab</a>\n" \
                        "<b>Cosa puoi fare:</b>\n" \
                        "Questo bot è rilasciato sotto una licenza open-source, il che vuol dire che (se ne hai voglia) puoi 'copiarlo' e usarlo sotto i termini della sua licenza: <a href=\"https://www.apache.org/licenses/LICENSE-2.0\">APACHE 2.0</a>" \
                        " che ti invito caldamente a leggere. Questa licenza non ti obbliga a distribuire il tuo prodotto sotto la stessa licenza, ma devi mettere una nota sul Copyright anche nel caso in cui il tuo prodotto sia closed-source." \
                        "", parse_mode="html")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if(message.text == "#userdump"):  
        if(str(message.chat.id) == super_user):
            dbh = DBHelper("data_new.db")
            bot.send_message(message.chat.id, "<b>"+str(dbh.count())+"</b>", parse_mode="html")
        else:
            bot.send_message(message.chat.id, "<b>Non sei autorizzato ad eseguire questo comando.</b>", parse_mode="html")
    if (message.text == "Oggi"):
        get_today(message)
    if (message.text == "Domani"):
        get_tomorrow(message)
    if (message.text == "Ieri"):
        get_yesterday(message)
    if (message.text == "Orario"):
    	get_week(message)
    if (message.text == "Impostazioni"):
        get_settings(message)
    if (message.text == "Aiuto"):
        get_help(message)
    
    if(message.reply_to_message):
        if (message.reply_to_message.text == bug_msg):
            bot.send_message(log_channel, "<b>Tipo: </b>#BUG\n"+"<b>Utente:</b> "+message.from_user.first_name+"\n<b>ID: </b>"+str(message.from_user.id)+"\n<b>Username: </b>@"+message.from_user.username+"\n<b>Messaggio: </b>"+message.text, parse_mode="html")
            bot.send_message(message.chat.id, "<b>Fatto!</b> Il tuo bug verrà preso in considerazione appena possibile", parse_mode="html")
            
        if (message.reply_to_message.text == feature_msg):
            bot.send_message(log_channel, "<b>Tipo: </b>#FEATURE\n"+"<b>Utente:</b> "+message.from_user.first_name+"\n<b>ID: </b>"+str(message.from_user.id)+"\n<b>Username: </b>@"+message.from_user.username+"\n<b>Messaggio: </b>"+message.text, parse_mode="html")
            bot.send_message(message.chat.id, "<b>Fatto!</b> La tua richiesta verrà presa in considerazione appena possibile", parse_mode="html")
            
def handler(signum, frame):
    print("Termination code received, terminating...")
    quit()  # That's how we exit

# SIGINT is the ^C key, so we can exit the script anytime
# even in a while True loop, by calling the handler() function
signal.signal(signal.SIGINT, handler)

try:
    bot.polling(none_stop=True)
except requests.exceptions.ConnectionError as e:
    print >> sys.stderr, str(e)
    datetime.time.sleep(15)
