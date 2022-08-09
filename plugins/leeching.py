import imp
from re import U
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.enums.chat_type import ChatType
from pyrogram.enums.chat_members_filter import ChatMembersFilter
import time
from config import ADMIN
import string
#===================[Varible]=================#
word = string.ascii_lowercase


#===================[Function]=================#
def check_group_id(client:Client,id:int) ->bool:
    try:
        status = client.get_chat(id)
        if status.type == ChatType.GROUP or status.type == ChatType.SUPERGROUP:
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
@Client.on_message(filters.private & filters.text & filters.user(ADMIN))
def leecher(c:Client,m:Message):
    text = m.text

    if text.startswith('!leech'):
        list_users = []
        group_id = text.split('!leech')[1].strip()
        Check =  check_group_id(c,int(group_id))
        if Check:
            m.reply("Received , Please be Patient")
            for i in word:
                print("leech : " + str(group_id)+ ": " + str(len(list_users)))
                try:
                    u = c.get_chat_members(group_id,query=i,filter=ChatMembersFilter.SEARCH,limit=0)
                    for user in u:
                        info_user = (user.user.id,user.user.username,user.user.first_name)
                        list_users.append(info_user)

                except FloodWait as ex:
                    time.sleep(ex.x)
                    u = c.get_chat_members(group_id,query=i,filter=ChatMembersFilter.SEARCH,limit=0)
                    for user in u:
                        info_user = (user.user.id,user.user.username,user.user.first_name)
                        list_users.append(info_user)

            list_users = list(dict.fromkeys(list_users)) 
            path = "data\\"+str(group_id)+".txt"
            write_to_file(list_users,path)

            c.send_document(m.from_user.id,path,caption=f"Leeched Group : {group_id}")
            list_users.clear()            
        else:
            m.reply("**ID inCorrect ..!**")






