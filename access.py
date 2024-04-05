import requests
from config import PATH_TO_SERVER, TOKEN


headers = {
    ApiKeyAuth
}

data = requests.get(PATH_TO_SERVER+"/player/universe", headers=headers)
print(data.text)
