from xml.etree.ElementInclude import include
from pyrogram import Client
import logging
from config import API_id,API_hash
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


# Variable
API_ID = API_id
API_HASH = API_hash


if __name__ == "__main__":
    print("Starting Bot ... !")
    plugins = dict(root="plugins")
    app = Client(session_name="LeecherBot",api_id=API_ID,api_hash=API_HASH,plugins=plugins)
    app.run()