import requests
from config import PATH_TO_SERVER, TOKEN


data = requests.get(PATH_TO_SERVER+"/player/universe", headers=TOKEN)
print(data.text)
