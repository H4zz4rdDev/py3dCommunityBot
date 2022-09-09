import os
import asyncio
import configparser
import logging
import ChatBot
from utils.fonthelper import FontHelper
from ChatBot import ChatBot

# Reading config file
config = configparser.ConfigParser()
config.read('settings.ini')

working_directory = os.path.abspath(os.curdir)
os.chdir(working_directory + config['MAIN']['logfile_path'])
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    filename=config['MAIN']['logfile_name'], filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def chatBotMainThread():
    bot = ChatBot(config)
    bot.start()


# Starting all threads
loop = asyncio.get_event_loop()
loop.create_task(chatBotMainThread())
loop.run_forever()
