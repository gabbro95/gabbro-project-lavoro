import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
 
from pprint import pprint
import time
import datetime
import json

 
TOKEN="875253482:AAEBGBMJsWVehz1r6uA2VM38Oc6kCdyTCDE" #da sostituire
ID =  856689208 # Gabbro
ID1 = 838210367 # Frank
ID2 = 294614221 # Fabio

def on_chat_message(msg):
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='Ciao', callback_data='ciao'),
                     InlineKeyboardButton(text='Info', callback_data='info')],
                     [InlineKeyboardButton(text='Time', callback_data='time')],
                 ]) 
    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
            
 
def on_callback_query(msg):
    
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, chat_id, query_data)

    if chat_id == ID or chat_id == ID1 or chat_id == ID2:
        if query_data == 'ciao':
            bot.sendMessage(chat_id, 'Ciao sono un bot prova!')
            bot.answerCallbackQuery(query_id, 'Cosa cosa posso fare per te?')
        elif query_data == 'info':
            info=json.dumps(bot.getUpdates(),sort_keys=True, indent=4)
            bot.sendMessage(chat_id, info)
        elif query_data == 'time':
            ts = time.time()
            bot.answerCallbackQuery(query_id, text=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')) #messaggio a comparsa
        
    else:
        
        bot.sendMessage(chat_id, 'Non sei autorizzato!')
 
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread() 
print('Listening ...')
 
 
while 1:
    
    time.sleep(10)