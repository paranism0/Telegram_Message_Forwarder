# In The Name Of God
# Coded By Paranism
from pyrogram import Client , idle , filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.raw.functions.messages import GetDialogFilters
from sys import exit
import json
import os
import asyncio
import random

send_mode = False

def loading_configs_of_login_credential():
    global account , proxy_for_connecting_to_telegram , rand_range
    with open("login_credential",'r',encoding="utf-8") as login_config:
       cred_config = login_config.read()
       cred_config = json.loads(cred_config)
       rand_range = cred_config["randint_range"]
       item = cred_config["account"]
       try:
        account = [item["phone_number"],item["password"],item["api_id"] ,item["api_hash"],item["folder_name"]]
       except:
           print("you don't have any active accounts ... ")
           exit()
       else:
           item = cred_config["proxy"]
           if item["enable"]==1:
               proxy_for_connecting_to_telegram = [item["type"],item["host"],item["port"],item["username"],item["password"]]
               proxy_for_connecting_to_telegram = {
                "scheme": proxy_for_connecting_to_telegram[0],
                "hostname": proxy_for_connecting_to_telegram[1],
                "port": int(proxy_for_connecting_to_telegram[2]),
                "username": proxy_for_connecting_to_telegram[3],
                "password": proxy_for_connecting_to_telegram[4]
               }
           else:
               proxy_for_connecting_to_telegram = None
       login_config.close()

def authentication(mysession,phone_number,pwd = ""):
 is_authorized = mysession.connect()
 if not is_authorized:
  phone_code_hash = mysession.send_code(phone_number)
  phone_code = input("please input the phone code you have received-> ")
  try:
   mysession.sign_in(phone_number = phone_number ,phone_code_hash= phone_code_hash.phone_code_hash, phone_code=phone_code)
   print("login successfully done[+]")
  except:
   try:
    mysession.check_password(password=pwd)
    print("login successfully done[+]")
   except:
    print("Authenctication Failed[-]")
 else:
  print("you are already in account")

def helper2(chat):
          global chats_to_scrape , resolve_list
          try:
              ch_id = chat.channel_id
              chats_to_scrape[int('-100'+str(ch_id))] = resolve_list[int("-100"+str(ch_id))]
          except:
              usr_id = chat.user_id
              chats_to_scrape[int(usr_id)] = resolve_list[int(usr_id)]

def helper_function(folder):
    global chats_to_scrape
    for pinned in folder.pinned_peers:
        helper2(pinned)
    for include_p in folder.include_peers:
        helper2(include_p)

def scrape_all_chats(session):
  global chats_to_scrape , resolve_list
  cnt = 0
  resolve_list = {}
  authentication(session , account[0] , account[1])
  cnt+=1
  for item in session.get_dialogs():
    name = item.chat.title
    name = name if name!=None and name!="" else item.chat.first_name
    resolve_list[item.chat.id] = name
  folders_data = session.invoke(GetDialogFilters())
  for folder in list(folders_data):
     if folder.title in folders_you_wanna_scrape:
      helper_function(folder)

loading_configs_of_login_credential()
folders_you_wanna_scrape = []
chats_to_scrape = {}
folders_you_wanna_scrape.extend(account[-1])
if proxy_for_connecting_to_telegram==None:
    app = Client(f"{account[0]}",api_id=account[2],api_hash=f"{account[3]}")
else:
    app = Client(f"{account[0]}",api_id=account[2],api_hash=f"{account[3]}",proxy = proxy_for_connecting_to_telegram )
scrape_all_chats(app)
print("successfully logged in to account [+] ")
print(chats_to_scrape)

@app.on_message(filters.me)
async def all_message(_:Client , m:Message):
   global send_mode
   not_send_start_stop = False
   if m.media == None:
    get_text = m.text
    if get_text == "/start":
        await m.reply_text("ready for forwarding your post .... ", quote=True)
        send_mode = True
        not_send_start_stop = True
    elif get_text == "/stop":
        send_mode = False
        not_send_start_stop = True
        await m.reply_text("disable forwarding your post .... ", quote=True)
   if send_mode and not_send_start_stop == False :
     for chat in chats_to_scrape.items():
       await m.forward(chat[0])
       print(f"message successfully forwarded to {chat[1]}")
       await asyncio.sleep(random.randint(rand_range[0],rand_range[1]))

while True:
 try:
  try:
     app.disconnect()
     app.add_handler(MessageHandler(all_message))
     app.start()
  except:
     pass
  idle()
  try:
     app.stop()
  except:
     pass
 except:
     pass