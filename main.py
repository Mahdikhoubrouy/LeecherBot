from pyrogram import Client
import logging
import os.path
import os
from config import API_id,API_hash
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



if __name__ == "__main__":
    print("Starting Bot ... !")
    print("Please report any problems, thanks : Telegram : @Sir_miti")
    if not os.path.exists('data'):
        os.mkdir("data")

    plugins = dict(root="plugins")
    app = Client(name="LeecherBot",api_id=API_id,api_hash=API_hash,plugins=plugins)
    app.run()