from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import time
from config import ADMIN

#===================[Varible]=================#
admin = ADMIN
word = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']


#===================[Function]=================#
def check_group_id(client:Client,id:int) ->bool:
    print(id)
    try:
        status = client.get_chat(chat_id=id)
        if status.type == "group" or status.type == "supergroup":
            return True

    except Exception as ex:
        print(ex)
        return False

def write_to_file(data:list,path:str) -> None:
    file = open(path,"a+",encoding="utf-8")
    for user in data:
        info = f"{user[0]},{user[1]},{user[2]}\n"
        file.write(info)
    file.close()



# Handler
@Client.on_message(filters.private & filters.text & filters.user(admin))
def leecher(c:Client,m:Message):
    text = m.text

    if text.startswith('!leech'):
        list_users = []
        group_id = text.split('!leech')[1].strip()
        Check = check_group_id(c,group_id)
        if Check:
            m.reply("Received , Please be Patient")
            for i in word:
                print("leech : " + str(group_id)+ ": " + str(len(list_users)))
                try:
                    user = c.iter_chat_members(group_id,query=i,filter="all",limit=10000)
                    for u in user:
                        info_user = (u.user.id,u.user.username,u.user.first_name)
                        list_users.append(info_user)

                except FloodWait as ex:
                    time.sleep(ex.x)
                    user = c.iter_chat_members(group_id,query=i,filter="all")
                    for u in user:
                        info_user = (u.user.id,u.user.username,u.user.first_name)
                        list_users.append(info_user)

            list_users = list(dict.fromkeys(list_users)) 
            path = "data\\"+str(group_id)+".txt"
            write_to_file(list_users,path)

            c.send_document(m.from_user.id,path,caption=f"Leeched Group : {group_id}")
            list_users.clear()            
        else:
            m.reply("**ID inCorrect ..!**")






