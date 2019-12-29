import json 
import requests
import time
import urllib

TOKEN = "692104879:AAGQTj56lk1_QooxeO4kJbpoHOdXdw5Qz3A"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


# downloads the content from URL and returns a string
def get_url(url): 
    response = requests.get(url)

    # decode for some python versions
    content = response.content.decode("utf8") 
    return content


# gets the string response and parses it into python dictionary
def get_json_from_url(url): 
    content = get_url(url)
    js = json.loads(content)
    return js


# calls the API command to get the list of updates and the newly sent messages from the user
def get_updates(offset=None): 
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


# calculates the highest ID of all the updates we recieve
def get_last_update_id(updates): 
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


# returns a tuple of the chat id and message
def get_last_chat_id_and_text(updates): 
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

# sends the message through the bot
def send_message(text, chat_id): 
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

# the process of handling inputs -> processing it -> sending output
def updatesHandler(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]

            if not text.startswith('/'):
                send_message('Please use one of the defined commands', chat)
            
            elif text == '/start':
                send_message('use /frankotoarabic to translate into Arabic\nuse /arabictofranko to translate into franko', chat)
                
            elif text == '/help':
                send_message('WTF! there is only two commands!!', chat)
            

            # from franko to arabic translation
            elif text.startswith('/frankotoarabic '):
                input_message = ' '.join(text.split(' ')[1:])
                output_message = [None] * len(input_message)
                i = 0
                while i < len(input_message):
                    if input_message[i] == ' ': # space
                        output_message[i] = ' '
                    if input_message[i] == 'w': # w
                        output_message[i] = 'و'
                    if input_message[i] == 'g': # g
                        output_message[i] = 'ج'
                    if input_message[i] == 'e': # e
                        output_message[i] = 'ي'
                    if input_message[i] == 'a': # a
                        output_message[i] = 'ا'
                    if input_message[i] == 's': # s
                        output_message[i] = 'س'
                    if input_message[i] == 'd': # d
                        output_message[i] = 'د'
                    if input_message[i] == 't': # t
                        output_message[i] = 'ت'
                    if input_message[i] == 'n': # n
                        output_message[i] = 'ن'
                    if input_message[i] == 'm': # m
                        output_message[i] = 'م'
                    if input_message[i] == 'l': # l
                        output_message[i] = 'ل'
                    if input_message[i] == 'k': # k
                        output_message[i] = 'ك'
                    if input_message[i] == '3': # m
                        output_message[i] = 'ع'
                    if input_message[i] == '2': # m
                        output_message[i] = 'ق'
                    if input_message[i] == '4': # m
                        output_message[i] = 'ش'
                    if input_message[i] == '7': # m
                        output_message[i] = 'ح'
                    if input_message[i] == 'h': # m
                        output_message[i] = 'ه'
                    if input_message[i] == 'f': # m
                        output_message[i] = 'ف'
                    if input_message[i] == 'o': # m
                        output_message[i] = ''
                    if input_message[i] == 'y': # m
                        output_message[i] = 'ي'
                    if input_message[i] == 'z': # m
                        output_message[i] = 'ز'
                    if input_message[i] == 'b': # m
                        output_message[i] = 'ب'
                    if input_message[i] == '5': # m
                        output_message[i] = 'خ'
                    
                    i += 1
                st = ''.join(output_message)
                send_message(st,chat) 
            
            # from arabic to franco translation
            elif text.startswith('/arabictofranko '):
                a = ' '.join(text.split(' ')[1:])
                b = [None] * len(a)
                i = 0
                while i < len(a):
                    if a[i] == ' ': # space
                        b[i] = ' '
                    if a[i] == 'و': # w
                        b[i] = 'w'
                    if a[i] == 'ج': # g
                        b[i] = 'g'
                    if a[i] == 'ي': # e
                        b[i] = 'e'
                    if a[i] == 'ا': # a
                        b[i] = 'a'
                    if a[i] == 'س': # s
                        b[i] = 's'
                    if a[i] == 'د': # d
                        b[i] = 'd'
                    if a[i] == 'ت': # t
                        b[i] = 't'
                    if a[i] == 'ن': # n
                        b[i] = 'n'
                    if a[i] == 'م': # m
                        b[i] = 'm'
                    if a[i] == 'ل': # l
                        b[i] = 'l'
                    if a[i] == 'ك': # k
                        b[i] = 'k'
                    if a[i] == 'ع': # 3
                        b[i] = '3'
                    if a[i] == 'ق': # 2
                        b[i] = '2'
                    if a[i] == 'ش': # 4
                        b[i] = '4'
                    if a[i] == 'ح': # 7
                        b[i] = '7'
                    if a[i] == 'ه': # h
                        b[i] = 'h'
                    if a[i] == 'ف': # f
                        b[i] = 'f'
                    if a[i] == 'o': # o
                        b[i] = ''
                    if a[i] == 'ي': # y
                        b[i] = 'y'
                    if a[i] == 'ا': # y
                        b[i] = 'a'
                    if a[i] == 'ز': # y
                        b[i] = 'z'
                    if a[i] == 'ب': # y
                        b[i] = 'b'
                    if a[i] == 'ر': # y
                        b[i] = 'r'
                    if a[i] == 'ص': # y
                        b[i] = 's'
                            
                    i +=1
                
                st = ''.join(b)
                send_message(st,chat) 
        except Exception as e:
            print(e)
            

# checks every half a second for new messages
def main(): 
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            updatesHandler(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()