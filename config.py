import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()

PMPERMIT = getenv("PMPERMIT","ENABLE")

class API:
    API_ID = int(os.getenv("API_ID", "21455847"))
    API_HASH = os.getenv("API_HASH", "8362067b5445fd55efd6b70d78f97fbd")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7736454439:AAEByOT89tseYQGHZUgyi5XZIeIGEq_OOUI")
    STRING_SESSION = os.getenv("STRING_SESSION", "BQFHY-cAc82YPa9sLLsEzaaoAxHZtzAjJzIeO3OQeJxlAyHXndukZ1LeNTmBU7Zv03yoTk9wcT9ix1CkJTjfk6ag47Z0t8lb1jU2tHzgXepazERy8KHZrWuGIqweI-OUy7ylf3172Kk9xZhIp177FOe15RCLwRN3BBANP2csGxUQSscpHZQ_ISZ9238s-lS5DKjh2Xb7s8Fwarup20VmC2WmEWzR8TqntxeXUzrgakb6rvvaUOt1xu2bItqdA5YzVgLC03xRWT3lNTT_Mpt-RX2Wzimwy2qVxI5DFV2zoAfQlMlkpaNTptJgw1yy5GutkTwd24dAszqfBgPUDNp5vpY-sad50AAAAAGLVDWlAA")

class config:
    MONGO_DATABASE = os.getenv("MONGO_DATABASE","mongodb+srv://Alisha:Alisha123@cluster0.yqcpftw.mongodb.net/?retryWrites=true&w=majority")
class DATABASE:
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://Alisha:Alisha123@cluster0.yqcpftw.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "6632519077"))

    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    PMPERMIT = os.getenv("PMPERMIT", None)
    ALIVE_PIC = os.getenv("ALIVE_PIC", "https://telegra.ph/file/ff88788a1ae767111d500.jpg")
    HELP_PIC = os. getenv("HELP_PIC", "https://telegra.ph/file/ff88788a1ae767111d500.jpg")
    START_PIC = os. getenv("START_PIC", "https://telegra.ph/file/ff88788a1ae767111d500.jpg")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", ".")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN
