from dotenv import load_dotenv
import os


load_dotenv()


TOKEN = os.environ.get("TOKEN")

PATH_TO_SERVER = os.environ.get("SERVER")

GET_UNIVERSE = "/player/universe"
